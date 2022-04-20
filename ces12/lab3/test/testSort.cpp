#include <gtest/gtest.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h> 
#include <stdlib.h> 
#include <time.h>
#include <sstream>
#include <sortauxfuncs.h>
//// ces12 lib code
#include <Tick.h> 
#include <stl_sort.h>
//// ces12 student code
#include <mysortfunctions.h>
#include <cstdio>


#define FILENAME "testresults.csv"

typedef void (*sort_function)(std::vector<int> &v , SortStats &stats) ;


/// adds environment to store strings with results
class SortEnvironment : public ::testing::Environment {
public:
   void SetUp() override {
    // Use current time as seed for random generator 
    srand(time(0));    
    // remove data file
    remove(FILENAME);
  } 
  
  void TearDown() override {
    std::cout << "*********************************" << std::endl << "******** END OF TESTS" << std::endl;
  }
    
}; // environment class


::testing::Environment* const sort_env = ::testing::AddGlobalTestEnvironment(new SortEnvironment);


// test if vector is sorted and report errors
::testing::AssertionResult isSorted(std::vector<int> &v) {
    bool issorted = true;
    
    if (v.size() > 1)// always sorted if length is 0 or 1
        // move i from the first to the penultimate position
        // stop also if already found it to be not sorted
        for (int i=0; (i <= v.size()-2) && issorted ; i++ )  
            if (v[i] > v[i+1])  issorted = false;
            
    if (issorted)
     return ::testing::AssertionSuccess();
    else {
        std::stringstream ss;
        ss << "vector NOT sorted  " << std::endl << "[ ";
        for (int val : v) 
            ss << val << " " ;
        ss << "]" << std::endl;
        return ::testing::AssertionFailure() << ss.str();
    }
        
}//IsSorted





// test fixture: create data and open file before each test
class SortTest : public ::testing::Test {
 protected:
  void SetUp() override {
    resetInputData();
    result_dump.open(FILENAME,std::ios_base::app);
  }
  
  void TearDown() override {
    result_dump.close();  
  }
  
  void resetInputData() {
    generateOrderedVector(vOrd10,10);
    generateReverseVector(vRev10,10);
    generateAlmostOrderedVector(vAlm10,10,0.2);
    generateOrderedVector(v10,10);
    randomPermutation(v10);
    generateOrderedVector(vOrd1e3,1e3);
    generateReverseVector(vRev1e3,1e3);
    generateAlmostOrderedVector(vAlm1e3,1e3,0.02);
    generateOrderedVector(v1e3,1e3);
    randomPermutation(v1e3);
    v1.resize(1); v1[0] = 1;
    v2.resize(2); v2[0] = 1; v2[1] = 2;
    v0.clear() ; // size after clear is zero
  }
  
  void test_small_vector( sort_function sf ) {
    SortStats unused_stats;
    
    // trivial vectors, size 0, 1, and 2
    EXPECT_NO_THROW(sf(v0,unused_stats));
    EXPECT_EQ(v0.size(),0);
    
    EXPECT_NO_THROW(sf(v1,unused_stats));
    EXPECT_EQ(v1.size(),1);     
    EXPECT_EQ(v1[0],1);
    
    EXPECT_NO_THROW(sf(v2,unused_stats));
    EXPECT_EQ(v2.size(),2);     
    EXPECT_EQ(v2[0],1);
    EXPECT_EQ(v2[1],2);
    
    // ten times sorting vectors of size 10
    for (int i=0; i < 10; i++) {
        ASSERT_FALSE(isSorted(v10));
        sf(v10,unused_stats);
        ASSERT_TRUE(isSorted(v10));
        randomPermutation(v10);
    }
    
    sf(vAlm10,unused_stats);
    EXPECT_TRUE(isSorted(vAlm10));
    
    sf(vRev10,unused_stats);
    EXPECT_TRUE(isSorted(vRev10));
    
    sf(vOrd10,unused_stats);
    EXPECT_TRUE(isSorted(vOrd10));     
    
    
}//test_small_vector

  void test_and_log_1Kvector( sort_function sf, std::string alg_name ) {
    SortStats average_stats;
    SortStats current_run;
    ces12::Tick tick;
    
    
    for (int i=0; i < 40; i++) {
        ASSERT_FALSE(isSorted(v1e3));
        tick.tickMili();
        sf(v1e3,current_run);
        current_run.ms_time = tick.tickMili();
        current_run.vector_size = v1e3.size();
        current_run.number_runs=1;
        //result_dump << current_run;
        average_stats.add2Average(current_run);
        ASSERT_TRUE(isSorted(v1e3));
        randomPermutation(v1e3);
    }
    
    average_stats.name = alg_name;
    //result_dump << "-------- average ----------" << std::endl;
    result_dump << average_stats;
        
    sf(vAlm1e3,current_run);
    EXPECT_TRUE(isSorted(vAlm1e3));
    
    sf(vRev1e3,current_run);
    EXPECT_TRUE(isSorted(vRev1e3));
    
    sf(vOrd1e3,current_run);
    EXPECT_TRUE(isSorted(vOrd1e3));    
      
  }//test_and_log_1Kvector
  
  
  void test_and_log_AlmostOrdered1Kvector( sort_function sf, std::string alg_name ) {
    SortStats average_stats;
    SortStats current_run;
    ces12::Tick tick;
    
    
    for (int i=0; i < 40; i++) {
        ASSERT_FALSE(isSorted(vAlm1e3));
        tick.tickMili();
        sf(vAlm1e3,current_run);
        current_run.ms_time = tick.tickMili();
        current_run.vector_size = vAlm1e3.size();
        current_run.number_runs=1;
        //result_dump << current_run;
        average_stats.add2Average(current_run);
        ASSERT_TRUE(isSorted(vAlm1e3));
        generateAlmostOrderedVector(vAlm1e3,1e3,0.02);
    }
    
    average_stats.name = alg_name;
    //result_dump << "-------- average ----------" << std::endl;
    result_dump << average_stats;
      
  }//test_and_log_1Kvector
  
  
  void test_log_ManySizes( sort_function sf, std::string alg_name, bool almostOrd = false) {
    SortStats average_stats; 
    SortStats current_run;
    ces12::Tick tick;
    int maxsize = 2e4;
    int stepsize = maxsize/100;
    std::stringstream ss;
    ss << alg_name << (almostOrd?"_AO_":"_RAND_") << stepsize << "_" << maxsize << ".csv";
    std::ofstream result_file;
    result_file.open(ss.str(),std::ios_base::trunc); //delete file if it exists
    std::vector<int> v;
    
    for (int size = stepsize; size <= maxsize; size+=stepsize) {
        average_stats.clear();
        
        for (int i=0; i < 5; i++) {
            if (almostOrd)
                generateAlmostOrderedVector(v,size,0.02);
            else {
                generateOrderedVector(v,size);
                randomPermutation(v);
            }
        
            current_run.clear();
            tick.tickMili();
            sf(v,current_run);
            current_run.ms_time = tick.tickMili();
            current_run.vector_size = v.size();
            current_run.number_runs=1;
            average_stats.add2Average(current_run);
            ASSERT_TRUE(isSorted(v));
        }//for
        average_stats.name = ""; // wont print name, it is in the filename
        result_file << average_stats;
    }//for
      
  }//test_log_ManySizes
  
  
  
  std::vector<int> vOrd10;
  std::vector<int> vRev10;
  std::vector<int> vAlm10;
  std::vector<int> v10;
  std::vector<int> vOrd1e3;
  std::vector<int> vRev1e3;
  std::vector<int> vAlm1e3;
  std::vector<int> v1e3;
  std::vector<int> v0;
  std::vector<int> v1;
  std::vector<int> v2;
  

  std::ofstream result_dump;
  
};// class SortTest



////////////// ACTUAL TESTS /////////////////////////

typedef SortTest SmallTests;
typedef SortTest STL_Tests;

TEST_F(SmallTests, Sort10_stl_sort) {
    test_small_vector(stl_sort);
}//Sort10

TEST_F(SmallTests, Sort10_myquicksort_2recursion) {
    test_small_vector(myquicksort_2recursion_medianOf3);
}//Sort10

TEST_F(SmallTests, Sort10_myquicksort_1recursion) {
    test_small_vector(myquicksort_1recursion_medianOf3);
}//Sort10

TEST_F(SmallTests, Sort10_myquicksort_fixpivot) {
    test_small_vector(myquicksort_fixedPivot);
}//Sort10

TEST_F(SmallTests, Sort10_radix_sort) {
    test_small_vector(myradixsort);
}//Sort10

TEST_F(SmallTests, Sort10_mymergesort_recursive) {
    test_small_vector(mymergesort_recursive);
}//Sort10

TEST_F(SmallTests, Sort10_mymergesort_iterative) {
    test_small_vector(mymergesort_iterative);
}//Sort10

/*
/// tests with 1k vector

TEST_F(STL_Tests, Sort1K_stl_sort) {
    test_and_log_1Kvector(stl_sort,"STL_SORT_1K ");
}//Sort1K

TEST_F(SortTest, Sort1K_myquicksort_2recursion) {
    test_and_log_1Kvector(myquicksort_2recursion_medianOf3,"QS_2R_1K");
}//Sort1K

TEST_F(SortTest, Sort1K_myquicksort_1recursion) {
    test_and_log_1Kvector(myquicksort_1recursion_medianOf3,"QS_1R_1K");
}//Sort1K

TEST_F(SortTest, Sort1K_myquicksort_fixpivot) {
    test_and_log_1Kvector(myquicksort_fixedPivot,"QS_FP_1K");
}//Sort1K

///  tests with almost ordered vector (quicksort variations only)

TEST_F(STL_Tests, Sort1K_stl_sort_AlmostOrdered) {
    test_and_log_AlmostOrdered1Kvector(stl_sort,"STLST_AO");
}//Sort1K


TEST_F(SortTest, Sort1K_QS_2recursion_AlmostOrdered) {
    test_and_log_AlmostOrdered1Kvector(myquicksort_2recursion_medianOf3,"QS_2R_AO");
}//Sort1K

TEST_F(SortTest, Sort1K_QS_1recursion_AlmostOdered) {
    test_and_log_AlmostOrdered1Kvector(myquicksort_1recursion_medianOf3,"QS_1R_AO");
}//Sort1K

TEST_F(SortTest, Sort1K_QS_fixpivot_AlmostOrdered) {
    test_and_log_AlmostOrdered1Kvector(myquicksort_fixedPivot,"QS_FP_AO");
}//Sort1K


/// raddix and mergesort with 1K vector

TEST_F(SortTest, Sort1K_radix_sort) {
    test_and_log_1Kvector(myradixsort,"RADIX_1K");
}//Sort1K

TEST_F(SortTest, Sort1K_mymergesort_recursive) {
    test_and_log_1Kvector(mymergesort_recursive,"MRG_R_1K");
}//Sort1K

TEST_F(SortTest, Sort1K_mymergesort_iterative) {
    test_and_log_1Kvector(mymergesort_iterative,"MRG_I_1K");
}//Sort1K
*/

/// tests with many sizes vector

TEST_F(STL_Tests, SortMS_stl_sort) {
    test_log_ManySizes(stl_sort,"STL_SORT_MS");
}//SortMS

TEST_F(SortTest, SortMS_myquicksort_2recursion) {
    test_log_ManySizes(myquicksort_2recursion_medianOf3,"QS_2R_MS");
}//SortMS

TEST_F(SortTest, SortMS_myquicksort_1recursion) {
    test_log_ManySizes(myquicksort_1recursion_medianOf3,"QS_1R_MS");
}//SortMS

TEST_F(SortTest, SortMS_myquicksort_fixpivot) {
    test_log_ManySizes(myquicksort_fixedPivot,"QS_FP_MS");
}//SortMS

TEST_F(SortTest, SortMS_radix_sort) {
    test_log_ManySizes(myradixsort,"RADIX_MS");
}//SortMS

TEST_F(SortTest, SortMS_mymergesort_recursive) {
    test_log_ManySizes(mymergesort_recursive,"MRG_R_MS");
}//SortMS

TEST_F(SortTest, SortMS_mymergesort_iterative) {
    test_log_ManySizes(mymergesort_iterative,"MRG_I_MS");
}//SortMS

// quicksort also needs to test the almost ordenred case
TEST_F(STL_Tests, SortMS_stl_sort_AO) {
    test_log_ManySizes(stl_sort,"STL_SORT_MS",true);
}//SortMS


TEST_F(SortTest, SortMS_myquicksort_2recursion_AO) {
    test_log_ManySizes(myquicksort_2recursion_medianOf3,"QS_2R_MS",true);
}//SortMS

TEST_F(SortTest, SortMS_myquicksort_1recursion_AO) {
    test_log_ManySizes(myquicksort_1recursion_medianOf3,"QS_1R_MS",true);
}//SortMS

TEST_F(SortTest, SortMS_myquicksort_fixpivot_AO) {
    test_log_ManySizes(myquicksort_fixedPivot,"QS_FP_MS",true);
}//SortMS
