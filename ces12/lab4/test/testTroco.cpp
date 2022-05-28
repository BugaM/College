#include <gtest/gtest.h>
#include <fstream> // file output
//// student code
#include <TrocoSolver.h>
#include <TrocoSolverFactory.h>
//// ces12 lib code
#include <Tick.h> 
#include <solveTroco.h> // closed lib with solution

#define TROCO_FILENAME "troco_"


  
void streamInstance(std::ostream &os, const std::vector<unsigned int> &denom,
                                     const unsigned int value,
                                     const std::vector<unsigned int> &coins ) {
    os << " D: [ " ;
    for (int i : denom) 
        os << i << " " ;
    os << "] val: " << value << std::endl ;
    os << " C: [ " ;
    int countcoins = 0;
    for (int i : coins) { 
        os << i << " " ;
        countcoins += i;
    }
    os << "] #coins= " << countcoins << std::endl ;
    
}


// test if answer has the correct value
::testing::AssertionResult isSumEqualToValue(const std::vector<unsigned int> &denom,
                                             const unsigned int value,
                                             const std::vector<unsigned int> &coins) {
    
    if ( denom.size() != coins.size() ) {
        std::stringstream ss;
        ss << "answer has size " << coins.size() << " but denom[] has size " << denom.size() << std::endl ;
        streamInstance(ss,denom,value,coins);
        return ::testing::AssertionFailure() << ss.str();
    }
        
    int sum = 0;
    for (int i = 0; i < coins.size() ; i++ ) {
        sum += coins[i] * denom[i];    
    }
    if (sum != value) {
        std::stringstream ss;
        ss << " answer value " << sum << " != " << value << " requested value "  << std::endl;
        streamInstance(ss,denom,value,coins);
        return ::testing::AssertionFailure() << ss.str();
    }//if
    
    
    
    // if no check failed, we are happy
    return ::testing::AssertionSuccess();
}//isSumEqualToValue

// test if answer has the correct number of coins
::testing::AssertionResult isNumberCoinsMinimal(const std::vector<unsigned int> &denom,
                                             const unsigned int value,
                                             const std::vector<unsigned int> &coins) {
    
    int countcoins = 0 ;
    for (int i : coins) countcoins += i; // count the number of coins
    
    std::vector<unsigned int> truecoins;
    solveTroco(denom,value,truecoins);
        int truecountcoins = 0 ;
    for (int i : truecoins) truecountcoins += i; // count the number of coins
    
        
    if (countcoins != truecountcoins) {
        std::stringstream ss;
        ss << " #coins your: " << countcoins << " != " << truecountcoins << " optimal #coins "  << std::endl;
        ss << "your solution: " << std::endl;
        streamInstance(ss,denom,value,coins);
        ss << "optimal solution: " << std::endl;
        streamInstance(ss,denom,value,truecoins);
        return ::testing::AssertionFailure() << ss.str();
    }//if
    
    
    
    // if no check failed, we are happy
    return ::testing::AssertionSuccess();
}//isNumberCoinsMinimal



// test fixture: create data and open file before each test
class TrocoTest : public ::testing::TestWithParam<std::string> {
public: 
  // Per-test-suite set-up.
  // Called before the first test in this test suite.
  // Can be omitted if not needed.
  static void SetUpTestSuite() {
    
  }

  // Per-test-suite tear-down.
  // Called after the last test in this test suite.
  // Can be omitted if not needed.
  static void TearDownTestSuite() {
    
  }

protected:
  void SetUp() override {
    
    
  }
  void TearDown() {
     result_dump.close();
  }

  

  
  std::vector<unsigned int> c ; // coins vector
  std::ofstream result_dump; // output test results
  ces12::Tick tick;
  
  
void testTroco( std::vector<unsigned int> &denom,
                unsigned int value,
                std::vector<unsigned int> &coins, 
                TrocoSolverAbstract *ts,
                bool doprint = false
                ) {
    coins.clear();
    ces12::Tick localtick;
    localtick.tickMili();
    ts->solve(denom,value,coins);
    double time_ms = localtick.tickMili();
    ASSERT_TRUE(isSumEqualToValue(denom,value,coins)) << " ALGORITHM: " << ts->getName();
    
    int countcoins = 0 ;
    for (int i : coins) countcoins += i; // count the number of coins
      
    if (ts->getName() != "GR") {
        ASSERT_TRUE(isNumberCoinsMinimal(denom,value,coins)) << " ALGORITHM: " << ts->getName();
    }//if
    
    if (doprint) {
        //int countcoins = 0 ;
        //for (int i : coins) countcoins += i; // count the number of coins
        result_dump << value << "," << time_ms << "," << countcoins << "," << ts->countRecursiveCalls() << std::endl;
    }//if
    
}//testTroco

  
};//class  Setup



void printIntVector(std::vector<int> &v) {
std::cout << std::endl << "[ ";
for (int i : v)
    std::cout << i << " ";
std::cout << " ]" << std::endl;
    
}

  
  

typedef TrocoTest TrocoTrivialTest;
typedef TrocoTest TrocoDCTest;
typedef TrocoTest TrocoNotSoTrivialTest;
typedef TrocoTest TrocoBrasilTest;
typedef TrocoTest TrocoGreedyTest;
typedef TrocoTest TrocoPrimoTest;

#define ALG_NAMES_ALL "PD","GR","DC"
#define ALG_NAMES_HARD "PD","GR"
  
TEST_P(TrocoTrivialTest, OneCoin ) {
    std::vector<unsigned int> d = { 1, 5, 10, 25, 50 };
    int value = 25;
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    delete ts;
}//// OneCoin

TEST_P(TrocoTrivialTest, OneCoinEach8 ) {
    std::vector<unsigned int> d = { 1,2,5 };
    int value = 8;
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    delete ts;
}//// OneCoinEach8

TEST_P(TrocoTrivialTest, Cents14 ) {
    std::vector<unsigned int> d = { 1,5, 10,25,50 };
    int value = 14 ;
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    delete ts;
}//// cents14
TEST_P(TrocoTrivialTest, Cents1 ) {
    std::vector<unsigned int> d = { 1,5, 10,25,50 };
    int value = 1; // checks initialization and trivial case
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    delete ts;
}//// cents1

TEST_P(TrocoDCTest, CentsUpto40 ) {
    std::vector<unsigned int> d = { 1,5, 10,25,50 };
    std::string fname(TROCO_FILENAME);
    fname.append("DC40.csv");
    result_dump.open(fname,std::ios_base::trunc);
    
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    tick.tickMili();
    for (int value = 1 ; value <= 40 ; value++ )  
        ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts,true));
    double time_ms = tick.tickMili();
    result_dump << "-1, " << time_ms << ",0 , 0" << std::endl; 
    delete ts;
}//// CentsUp



TEST_P(TrocoNotSoTrivialTest, OneCoinOfEach ) {
    std::vector<unsigned int> d = { 1, 5, 10, 25, 50 };
    
    int value = 91;
    
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    delete ts;
}//// OneCoinOfEach
  
TEST_P(TrocoTrivialTest, GreedyFails ) {
    std::vector<unsigned int> d = { 1, 10, 25, 50 };
    
    int value = 30; // example in the class slides 
    
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    
    //streamInstance(std::cerr,d,value,c);
    delete ts;
}//// GreedyFails


TEST_P(TrocoBrasilTest, MoedasBR200 ) {
    std::vector<unsigned int> d = { 1, 5, 10, 25, 50, 100 };
    
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    std::string fname(TROCO_FILENAME);
    fname.append(ts->getName());
    fname.append("_BR200.csv");
    result_dump.open(fname,std::ios_base::trunc);
    tick.tickMili();
    for (int value = 1 ; value <= 200 ; value++ )  
        ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts,true));
    double time_ms = tick.tickMili();
    result_dump << "-1, " << time_ms << ",0 , 0" << std::endl; 
    
    delete ts;
}//// 

/// teste escrito pela Thayna P. Baldao 
TEST_P(TrocoGreedyTest, GRLoses ) {
    std::vector<unsigned int> d = { 1, 10, 25 };
    
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    std::string fname(TROCO_FILENAME);
    fname.append(ts->getName());
    fname.append("_GRLoses.csv");
    result_dump.open(fname,std::ios_base::trunc);
    tick.tickMili();
    for (int value = 1 ; value <= 200 ; value++ )  
        ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts,true));
    double time_ms = tick.tickMili();
    result_dump << "-1, " << time_ms << ",0 , 0" << std::endl; 
    
    delete ts;
}//// 

TEST_P(TrocoPrimoTest, Primo200 ) {
    std::vector<unsigned int> d = { 1, 2, 7, 11, 23, 53, 97 };
    TrocoSolverAbstract* ts = TrocoSolverFactory::make(GetParam());
    
    tick.tickMili();
    
    for (int value = 1 ; value <= 200 ; value++ )  
        ASSERT_NO_FATAL_FAILURE(testTroco(d,value,c,ts));
    double time_ms = tick.tickMili();
    
    delete ts;
}//// 


INSTANTIATE_TEST_SUITE_P(TrocoT,
                        TrocoTrivialTest,
                        ::testing::Values(ALG_NAMES_ALL ));

INSTANTIATE_TEST_SUITE_P(TrocoT,
                        TrocoDCTest,
                        ::testing::Values("DC"));


INSTANTIATE_TEST_SUITE_P(TrocoN,
                        TrocoNotSoTrivialTest,
                        ::testing::Values(ALG_NAMES_HARD ));

INSTANTIATE_TEST_SUITE_P(TrocoB,
                        TrocoBrasilTest,
                        ::testing::Values(ALG_NAMES_HARD));

INSTANTIATE_TEST_SUITE_P(TrocoG,
                        TrocoGreedyTest,
                        ::testing::Values(ALG_NAMES_HARD));

INSTANTIATE_TEST_SUITE_P(TrocoP,
                        TrocoPrimoTest,
                        ::testing::Values(ALG_NAMES_HARD));
