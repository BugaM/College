#include <gtest/gtest.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h> 
#include <stdlib.h> 
#include <time.h>
#include <sstream>
#include <cstdio>
//// ces12 lib code
#include <Tick.h> 
#include <Point3.h>
#include <PointReader.h>
#include <IndexPointsAbstract.h>
#include <IndexFactory.h>


/// generates random long, value from 0 to N
long randomUptoN(long N) {
    float ratio = (float)rand() / (float)RAND_MAX;
    return round(ratio * N);
}



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
class TreeTest : public ::testing::Test {
public: 
  // Per-test-suite set-up.
  // Called before the first test in this test suite.
  // Can be omitted if not needed.
  static void SetUpTestSuite() {
    // Use current time as seed for random generator 
    srand(time(0));  
            
    PointReader preader("../data/oakland_part2_complete.asc");
    preader.read(oak);
    
  }

  // Per-test-suite tear-down.
  // Called after the last test in this test suite.
  // Can be omitted if not needed.
  static void TearDownTestSuite() {
    oak.clear(); // if not cleared, next test suite will fill it again
    // and get double the data, repeated
  }

 protected:
  void SetUp() override {
  
    //result_dump.open(FILENAME,std::ios_base::app);
  }
  
  void TearDown() override {
    //result_dump.close();  
  }
  
  
  static std::vector<Point3> oak;
  
};// class TreeTest

std::vector<Point3> TreeTest::oak;

/// parameter functions


////////////// ACTUAL TESTS /////////////////////////

typedef TreeTest SanityTests;
typedef TreeTest OakTests;

#define MILI 1e-3
#define MICRO 1e-6

TEST_F(SanityTests, readAscFile) {
    std::vector<Point3> pp;
    
    PointReader preader("../data/oakland100lines.asc");
    preader.read(pp);
    // check if we have read 100 points
    ASSERT_EQ(pp.size(),100);
        
}//read readAscFile

/// this doesn't test student code. it only tests the lib and the stl based solution
TEST_F(SanityTests, indexFile) {
    std::vector<Point3> pp;
    
    PointReader preader("../data/oakland100lines.asc");
    preader.read(pp);
    
    ASSERT_EQ(pp.size(),100); // we have read 100 points
    
    IndexPointsAbstract* idx = IndexFactory::makeIndex("MMP");
    
    // key to index is only the x coordinate
    for (int i = 0; i < pp.size() ; i++) idx->add( pp[i].x(), i );
    
    ASSERT_EQ(idx->size(),100);
    
    std::vector<long> res; 
    idx->find(res,-16.975,-16.965); // look for the first point
    ASSERT_EQ(res.size(),1); // it is the only point returned
    ASSERT_NEAR(pp[res[0]].x(),-16.97,MILI);
    ASSERT_NEAR(pp[res[0]].y(),-27.84,MILI);
    ASSERT_NEAR(pp[res[0]].z(),  5.72,MILI);
    ASSERT_EQ(pp[res[0]].cat(),1400);
    
    res.clear();
    idx->find(res,-16.76,-16.7); // look for 3 points -16.71 72 75
    ASSERT_EQ(res.size(),3); // check if we got 3 points
    
    delete idx;
}//read readAscFile

// repeat the sanity test with student code
// but with only 100 points, there is no fun
TEST_F(SanityTests, indexFileALU) {
    std::vector<Point3> pp;
    
    PointReader preader("../data/oakland100lines.asc");
    preader.read(pp);
    
    ASSERT_EQ(pp.size(),100);
    
    IndexPointsAbstract* idx = IndexFactory::makeIndex("ALU");
    
    // key to index is only the x coordinate
    for (int i = 0; i < pp.size() ; i++) idx->add( pp[i].x(), i );
    
    ASSERT_EQ(idx->size(),100);
    
    std::vector<long> res; 
    idx->find(res,-16.975,-16.965); // look for the first point, only it
    ASSERT_EQ(res.size(),1);
    ASSERT_NEAR(pp[res[0]].x(),-16.97,MILI);
    ASSERT_NEAR(pp[res[0]].y(),-27.84,MILI);
    ASSERT_NEAR(pp[res[0]].z(),  5.72,MILI);
    ASSERT_EQ(pp[res[0]].cat(),1400);
    
    res.clear();
    idx->find(res,-16.76,-16.7); // look for 3 points -16.71 72 75
    ASSERT_EQ(res.size(),3);
    
    delete idx;
}//read readAscFile

//  reads large file, performs 10 searches, look for randomly chosen points
TEST_F(OakTests, OakReadFile) {
    
    int step_number = 10; // inserts 1/10th of file each time
    long stepsize = oak.size() / step_number;
    IndexPointsAbstract* idx = IndexFactory::makeIndex("ALU");
    
    long next = 0;
    for (int step = 1; step <= step_number ; step++) {
        // add stepsize elements
        for (int i = 0 ; (i < stepsize) && (next < oak.size()) ; i++) {
            idx->add(oak[next].x(),next);
            next++;
        }
        
        long randomptidx = randomUptoN(next-1); 
        std::vector<long> res; 
        
        idx->find(res,oak[randomptidx].x()); // look for the randompoint
        
        ASSERT_NEAR(oak[res[0]].x(),oak[randomptidx].x(),MILI); // assert we found the same x coord
        
        /// interesting: there are some dozens of points with the same x coord
        //std::cerr << "\n step "<< step <<" looked for: " << oak[randomptidx] << " found : " ; 
        //for (int i = 0 ; i < res.size() ;  i++) std::cerr << oak[res[i]] << " ";
        //std::cerr << "\n";
        
    
    }//for step
    
    delete idx;
    
}//OakReadFile

// reads 1/100th of the file each time
// inserts in index
// searches for a randomly choosen point
// checks if point was found
// measures time for insertion and for search
TEST_F(OakTests, OakByNorm) {
    
    std::ofstream result_dump; // output test results
    result_dump.open("oak_search.csv",std::ios_base::trunc);
    int step_number = 100;
    long stepsize = oak.size() / step_number;
    IndexPointsAbstract* idx = IndexFactory::makeIndex("MMP");
    IndexPointsAbstract* idxaluno = IndexFactory::makeIndex("ALU");
    idx->setTolerance(MICRO); // small tolerance, otherwise many points would be found
    idxaluno->setTolerance(MICRO);
    ces12::Tick tick;
    
    long next = 0;
    for (int step = 1; step <= step_number ; step++) {
        // add stepsize elements
        long old_next = next;
        tick.tickMicro();
        for (long i = 0 ; (i < stepsize) && (next < oak.size()) ; i++) {
            idx->add(oak[next].norm(),next);
            next++;
        }
        float t_ins_stl = (float)tick.tickMicro() / (float)stepsize; // time for insertions
        next = old_next;
        // add stepsize elements
        tick.tickMicro();
        for (long i = 0 ; (i < stepsize) && (next < oak.size()) ; i++) {
            idxaluno->add(oak[next].norm(),next);
            next++;
        }
        float t_ins_aluno = (float)tick.tickMicro()/ (float)stepsize;// time for insertions
        
        
        /// do a number of searches and average times
        std::vector<long> res;
        std::vector<long> resaluno;
        float timeus = 0.0f;
        float timeusaluno = 0.0f;
        int NUMBER_OF_SEARCHES = 10;
        std::vector<long> randomptidx(NUMBER_OF_SEARCHES);
        for ( int i=0 ; i<NUMBER_OF_SEARCHES ; i++) // ids of random points
            randomptidx[i] = randomUptoN(next-1);
        
        
        for (int i=0 ; i<NUMBER_OF_SEARCHES ; i++) { // ids of random points
            res.clear(); resaluno.clear();
            tick.tickMicro();
            idx->find(res, oak[randomptidx[i]].norm()); // look for the randompoint
            timeus += tick.tickMicro();// time for one search
            idxaluno->find(resaluno, oak[randomptidx[i]].norm()); // look for the randompoint
            timeusaluno += tick.tickMicro(); // time for one search
            
            ASSERT_NEAR(oak[res[0]].norm(),oak[randomptidx[i]].norm(),MILI); // assert we found the same norm
            ASSERT_NEAR(oak[resaluno[0]].norm(),oak[randomptidx[i]].norm(),MILI);
            // tolerance here could be MICRO instead of MILI, but it is ok as MILI
        } //endfor searches
        timeus /= NUMBER_OF_SEARCHES; // average time for a search
        timeusaluno /= NUMBER_OF_SEARCHES; // average time for a search
        
        result_dump << step << ", "<< next << ", "<< timeus << ", " << timeusaluno << ", " << t_ins_stl << ", " << t_ins_aluno << std::endl; 
        
        
        /*
        /// need to decrease tolerance to avoid finding many points
        std::cerr << "\n step "<< step <<" looked for: " << oak[randomptidx] << 
            " found "<< res.size() << ": " ; 
        for (int i = 0 ; i < res.size() ;  i++)
            std::cerr << i << ":("<<res[i]<<") " << oak[res[i]] << " ";
        std::cerr << "\n";
        */
        
    
    }//for step
    
    //std::cerr << "\n size oak: " << oak.size()<< " | next: " << next << std::endl;
    
    result_dump.close();
    delete idx; delete idxaluno;
    
}//OakReadFile


// indexes with distance from given point, searches for an interval
// so it accepts a sphere with spherical hole inside
// what is the correct name for this figure? is it a thorus?
// does this for the student index and for the STL one, and writes down both results
TEST_F(OakTests, VoidSphereSelection) {
    
    std::ofstream result_dump; // output test results
    result_dump.open("torusMMP.asc",std::ios_base::trunc);
    std::ofstream result_dump_aluno; // output test results
    result_dump_aluno.open("torusALU.asc",std::ios_base::trunc);
    
    IndexPointsAbstract* idx = IndexFactory::makeIndex("MMP");
    IndexPointsAbstract* idxaluno = IndexFactory::makeIndex("ALU");
    
    ces12::Tick tick;
    
    // near this point there are 1 tree and 2 cars 
    Point3 center(-74,-67,-6,1400);
    // adds all points to both indexes (the whole file)
    for (long i = 0 ; i < oak.size() ; i++ ) {
        idx->add(center.dist(oak[i]),i);
        idxaluno->add(center.dist(oak[i]),i);
    }
    
    std::vector<long> res;
    std::vector<long> resaluno;
    res.clear(); resaluno.clear();
    tick.tickMili();
    idx->find(res, 5,13); // look 
    float timems = tick.tickMili(); // time to search
    idxaluno->find(resaluno, 5,13); // look 
    float timemsaluno = tick.tickMili();// time to search
    
    ASSERT_EQ(resaluno.size(),res.size()); // both must return the same number of points
        
    for (long i = 0 ; i < res.size() ; i++ ) {
        result_dump << oak[res[i]].x() << " " << oak[res[i]].y() << " " << oak[res[i]].z() << std::endl ;
        result_dump_aluno << oak[resaluno[i]].x() << " " << oak[resaluno[i]].y() << " " << oak[resaluno[i]].z() << std::endl ;;
    }
    
    std::cout << " VoidSphere time (ms) MMP: " << timems << " aluno: " << timemsaluno << std::endl;
    
    result_dump.close();
    result_dump_aluno.close();
    delete idx; delete idxaluno;
    
}//OakReadFile





