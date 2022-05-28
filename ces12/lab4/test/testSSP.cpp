#include <gtest/gtest.h>
#include <fstream> // file output
#include <sstream> // string stream
#include <time.h>

//// ces12 lib code
#include <Tick.h> 
#include <SSPInstanceGenerator.h>
#include <SubsetSumSolverAbstract.h>
#include <SSPSolverFactory.h>
#include <balsub.h> // closed lib with solution
#include <subsum.h>
#include <SSP_Exp.h>
//// student test definition
#include <testesAluno.h>

#define SSP_FILENAME "SSP_"
/*
struct SSP_Exp {
    SSP_Exp(std::vector<std::string> _algs, 
            std::vector<int> _sizes,
            std::vector<std::string> _data, int _rep) : algs(_algs), sizes(_sizes), data(_data), repeat(_rep) { }
    
    std::vector<std::string> algs;
    std::vector<int> sizes;
    std::vector<std::string> data;
    int repeat;
    
    
}; // class

   ostream& operator<<(ostream& os, const SSP_Exp& e)
{
    os << std::endl << "SSPx" << e.repeat << " ALG[ " ;
    for (std::string s : e.algs)
        os << s << " ";
    os << "]"<<std::endl << "siz[ " ;
    for (int i : e.sizes)
        os << i << " ";
    os << "]"<<std::endl << "Dat[ " ;
    for (std::string s : e.data)
        os << s << " ";
    os << "]"<<std::endl ;
    return os;
}
 
*/

// test if answer has the correct value
::testing::AssertionResult isSSPCorrect(const std::vector< long> &input,
                                             const  long value,
                                             const std::vector<char> &x) {
    
    if ( input.size() != x.size() ) {
        std::stringstream ss;
        streamSSP(ss,input,value,x);
        ss << "answer has size " << x.size() << " but input[] has size " << input.size() << std::endl ;
        return ::testing::AssertionFailure() << ss.str();
    }
        
    long sumsol = 0;
    for (int i=0; i < x.size(); i++) {
        if (x[i]) sumsol+=input[i];
    }//for
        
    if (sumsol != value) {
        std::stringstream ss;
        streamSSP(ss,input,value,x);
        ss << " answer value " << sumsol << " != " << value << " requested value "  << std::endl;
        return ::testing::AssertionFailure() << ss.str();
    }//if
            
    // if no check failed, we are happy
    return ::testing::AssertionSuccess();
}//isSumEqualToValue


// test fixture: create data and open file before each test
class SSPTest : public ::testing::TestWithParam<SSP_Exp> {
public: 
  // Per-test-suite set-up.
  // Called before the first test in this test suite.
  // Can be omitted if not needed.
  static void SetUpTestSuite() {
        srand(time(0));    // Use current time as seed for random generator 
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
     //result_dump.close();
  }
  
  
  
}; // class

typedef SSPTest SSPTimedT;
typedef SSPTest InstanceView;


TEST_P(InstanceView, T_InstanceViewer ) {
    SSP_Exp e = GetParam();
    SSPInstanceGenerator g;
    std::vector< long> i ;
    std::vector<char> x ;
    //long size = 50;
    long val = 0;
    for (std::string d : e.data ) {
        for (int size : e.sizes ) {
            g.generate(d,size,i,val); // generate input
            std::cout << d << " ";
            streamSSP(std::cout,i,val);   
        }//for
    }//for
}//test



TEST_P(SSPTest, T_ParamTest ) {
    SSP_Exp e = GetParam();
    //std::cerr << "T_PARAMTEST:: " << e;
    std::vector< long> i ;
    //std::vector<char> x ;
    //std::vector<char> xref ;
    long val; 
    SSPInstanceGenerator g;
    SubsetSumSolverAbstract *sspgab = SSPSolverFactory::makeSSP("DD");
    
    for (std::string alg : e.algs ) {
        SubsetSumSolverAbstract *ssp = SSPSolverFactory::makeSSP(alg);
        for (int s : e.sizes) {
            for (std::string d : e.data) {
                for (int r = 0 ; r < e.repeat ; r++) {
                    ASSERT_TRUE(sspgab) << " NULL solver gabarito!";
                    ASSERT_TRUE(ssp) << " NULL solver aluno!";
                    std::vector<char> x ;
                    std::vector<char> xref ;
                    g.generate(d,s,i,val); // generate input
                    bool aluno_yesno = ssp->solve(i,val,x); // solve
                    bool reference_yesno = sspgab->solve(i,val,xref); // solve w/ ref implementation
                    
                    //std::cout << "\n A:" << aluno_yesno << " R:" << reference_yesno << " " << d << " " << alg << " refx / x" ;
                    //streamSSP(std::cout,i,val,xref);
                    //streamSSP(std::cout,i,val,x);
                    
                    if (reference_yesno) {
                        if (!aluno_yesno) {
                            std::stringstream ss; 
                            ss << " (Alg:" << alg << ") Instance has solution but your answer is negative. Solution: ";
                            streamSSP(ss,i,val,xref);
                            ss << " Your answer: ";
                            streamSSP(ss,i,val,x);
                            FAIL() << ss.str();
                        }
                        
                        ASSERT_TRUE(isSSPCorrect(i,val,x)) << " (Alg:" << alg  << ") Instance has solution but your solution is wrong. ";
                    } else {
                        std::stringstream ss; 
                        if (aluno_yesno ) {
                            ss << std::endl << 
                            "this instance has no solution but you answered YES with this solution:" ;
                            streamSSP(ss,i,val,x);
                            FAIL() << ss.str();
                        }//if
                        ss << std::endl << 
                            "the answer from DD was:";
                        streamSSP(ss,i,val,xref);
                        ASSERT_FALSE(isSSPCorrect(i,val,x)) << " Alg:" << alg << " " << ss.str();
                    }//if
                } // for repetitions
            } // for data
            
        }//for sizes
        
        delete ssp;
        
    }//for alg
    delete sspgab;
}// T_ParamTest


TEST_P(SSPTimedT, Timed) {
    SSP_Exp e = GetParam();
    ces12::Tick tick;
    std::vector< long> i ;
    std::vector<char> x ;
    //std::vector<char> xref ;
    long val; 
    SSPInstanceGenerator g;
    std::ofstream result_dump;
    
    const ::testing::TestInfo* const test_info = ::testing::UnitTest::GetInstance()->current_test_info();
    std::string tname(test_info->test_suite_name());
    
    //cout << "\n\n***************************** " << tname << "@@@ \n";
    
    std::size_t found = tname.find_first_of("//");
    if (found != std::string::npos)
        tname=tname.substr(0,found); // cut stuff after / it messes with file names
    
    //cout << "\n\n***************************** " << tname << "!!! \n";
    
    if (e.algs.empty()) return;
    if (e.data.empty()) return;
    if (e.sizes.empty()) return;
    
    
    for (std::string alg : e.algs ) {
        SubsetSumSolverAbstract *ssp = SSPSolverFactory::makeSSP(alg);
        for (std::string d : e.data) {
            result_dump.open(SSP_FILENAME+tname+"_"+alg+"_"+d+".dat",std::ios_base::trunc);
            for (int s : e.sizes) {
                double sum_times = 0.0; 
                int count_yes = 0;
                for (int r = 0 ; r < e.repeat ; r++) {
                    g.generate(d,s,i,val); // generate input
                    tick.tickMili();
                    bool aluno_yesno = ssp->solve(i,val,x); // solve
                    if (aluno_yesno) count_yes++;
                    sum_times += tick.tickMili();
                    
                    //std::cout << "\n A:" << aluno_yesno <<  " " << d;
                    //streamSSP(std::cout,i,val,x);
                } // for repetitions
                result_dump << s <<","<< sum_times/(float)e.repeat 
                            <<","<< count_yes<<","<<e.repeat<<std::endl;
            } // for sizes
            result_dump.close();
        }//for data
        
        delete ssp; 
        
    }//for alg      
}//


INSTANTIATE_TEST_SUITE_P(Tests50VerySmall5_6,
                         SSPTest,
                         ::testing::Values(SSP_Exp({"DD","PD","A2"},{5,6},
                                                   {"P3","P4","P5","RAND","EVOD"}
                                                   ,28)
                                            ));


INSTANTIATE_TEST_SUITE_P(TestsManyUpto15,
                         SSPTest,
                         ::testing::Values(SSP_Exp({"DD","PD","A2"},
                                                   {10,11,12,13,15},
                                                   {"P3","P4","P5","RAND","EVOD"}
                                                   ,10)
                                            ));

/* // too large for simpler algorithms. 
INSTANTIATE_TEST_SUITE_P(TestsFewLargeUpto50,
                         SSPTest,
                         ::testing::Values(SSP_Exp({"DD","PD","A2"},{30,40,50},
                                                   {"P3","P6","P9","RAND","EVOD","AVIS",}
                                                   ,2)
                                            ));
*/
                                            
INSTANTIATE_TEST_SUITE_P(TestsNoSolution,
                         SSPTest,
                         ::testing::Values(SSP_Exp({"DD","PD","A2"},
                                                   {10,11,12,13,14},
                                                   {"AVIS"}
                                                   ,1) // TODD, AVIS are NOT random.
                                            ));

INSTANTIATE_TEST_SUITE_P(Tests_Timed_DD,
                         SSPTimedT,
                         ::testing::Values(SSP_Exp({"DD"},
                                                   {5,7,8,10,12,13,15},
                                                   {"P3","P4","P5","RAND","EVOD","AVIS"}
                                                   ,3) // TODD and AVIS are not random.
                                                       // TODD size > 25 => long overflow
                                            ));
INSTANTIATE_TEST_SUITE_P(Tests_Timed_PD,
                         SSPTimedT,
                         ::testing::Values(SSP_Exp({"PD"},
                                                   {5,7,8,10,12,13,15},
                                                   {"P3","P4","P5","RAND","EVOD","AVIS"}
                                                   ,3) // TODD and AVIS are not random.
                                                       // TODD size > 25 => long overflow
                                            ));
INSTANTIATE_TEST_SUITE_P(Tests_Timed_A2,
                         SSPTimedT,
                         ::testing::Values(SSP_Exp({"A2"},
                                                   {5,7,8,10,12,13,15},
                                                   {"P3","P4","P5","RAND","EVOD","AVIS"}
                                                   ,3) // TODD and AVIS are not random.
                                                       // TODD size > 25 => long overflow
                                            ));
/*
INSTANTIATE_TEST_SUITE_P(Tests_Timed_TODD,
                         SSPTimedT,
                         ::testing::Values(SSP_Exp({"DD","PD","A2"},
                                                   {10,12,15,17,20},
                                                   {"TODD"}
                                                   ,2) // TODD and AVIS are not random.
                                                       // TODD size > 25 => long overflow
                                            ));
*/
/*
INSTANTIATE_TEST_SUITE_P(InstanceViewer,
                         InstanceView,
                         ::testing::Values(SSP_Exp({"DD"}, // ignored for instance viewer
                                                   {},//{10,15}, // if empty, test output nothing
                                                   {"TODD","P3","P6","P9","RAND", "EVOD","AVIS"}
                                                   ,3)  // ignored for instance viewer
                                            ));
*/

INSTANTIATE_TEST_SUITE_P(InstanceViewerAluno,
                         InstanceView,
                         ::testing::Values( alunoViewInstance() ) 
                        );

INSTANTIATE_TEST_SUITE_P(Tests_Aluno1,
                         SSPTest,
                         ::testing::Values( alunoTestSSP1() ) 
                        );

INSTANTIATE_TEST_SUITE_P(Tests_Aluno2,
                         SSPTest,
                         ::testing::Values( alunoTestSSP2() ) 
                        );

INSTANTIATE_TEST_SUITE_P(Tests_Aluno3,
                         SSPTest,
                         ::testing::Values( alunoTestSSP3() ) 
                        );

INSTANTIATE_TEST_SUITE_P(Tests_AlunoTimed1,
                         SSPTimedT,
                         ::testing::Values( alunoTestTimed1() ) 
                        );
INSTANTIATE_TEST_SUITE_P(Tests_AlunoTimed2,
                         SSPTimedT,
                         ::testing::Values( alunoTestTimed2() ) 
                        );


