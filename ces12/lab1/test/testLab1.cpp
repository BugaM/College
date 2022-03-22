#include <gtest/gtest.h>
#include "hash.h"
#include "hashfunctions.h"
#include <fstream>
#include <sstream>
#include <string>

TEST(Lab1Hash, AddOneElement){
    int collisions; int isthere; int result;
    
    Hash *H = new Hash(29,hashdiv29);
    
    // before inserting, it must be empty
    isthere = H->contains("abc",collisions);
    EXPECT_EQ(0,isthere);
    EXPECT_EQ(0,collisions);
    EXPECT_EQ(0,H->worst_case());
    EXPECT_EQ(0,H->size());
    
    result = H->add("abc", collisions);
    EXPECT_EQ(1,result); // it was empty.
    EXPECT_EQ(0,collisions); // if it was empty, there could be no collisions
    EXPECT_EQ(1,H->worst_case());
    EXPECT_EQ(1,H->size());
    
    // check if inserted element is really there.
    isthere = H->contains("abc",collisions);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(1,collisions); // 1 element, 1 collision to find it
    
    // note that sum of chars of abd is just 1 + sum(abc)
    // so this would check the next bucket
    isthere = H->contains("abd",collisions);
    EXPECT_EQ(0,isthere);
    EXPECT_EQ(0,collisions);
    
    // note that we just changed the order, the sum must be the same
    isthere = H->contains("cab",collisions);
    EXPECT_EQ(0,isthere);
    EXPECT_EQ(1,collisions); // this queue has 1 element
         
    delete H;
      
}// AddOneElement


TEST(AuxLab1Hash, HashValueIsInsideVector){
    
    int tsize=29;
    Hash *H = new Hash(tsize,hashdiv29);
    
    int hval;
    hval = H->hash("abc");
    EXPECT_LE(hval, tsize);
    EXPECT_GE(hval, 0);
    
    // generate different strings and
    // check if hashvalue is not out of vector bounds
    std::string str = "a";
    char c = 'a';
    for (int i=0; i < 50 ; i++) {
        hval = H->hash(str);
        EXPECT_LE(hval, tsize) << " with input [" << str << " ]" ;
        EXPECT_GE(hval, 0) << " with input [" << str << " ]" ; 
        str += c; 
        c++; // adds another char to str
        if (c > 126) c = 'a'; // do not allow c to be negative
    }
    
    delete H;
}//HashValueIsInsideVector


TEST(Lab1Hash, Add4Elements){
    int collisions; int isthere; int result;
    
    Hash *H = new Hash(29,hashdiv29);
    
    // 3 elements in the same bucket, 1 element in a different bucket
    result = H->add("abc", collisions);
    EXPECT_EQ(0,collisions); // if it was empty, there could be no collisions
    EXPECT_EQ(1,H->worst_case());
    EXPECT_EQ(1,H->size());
    EXPECT_EQ(1,result);
    result = H->add("abd", collisions); // different bucket
    EXPECT_EQ(0,collisions); // different bucket, there could be no collisions
    EXPECT_EQ(1,H->worst_case()); // one element on each bucket
    EXPECT_EQ(2,H->size());
    EXPECT_EQ(1,result);
    result = H->add("bca", collisions); // same bucket
    EXPECT_EQ(1,collisions); // bucket already had 1 element
    EXPECT_EQ(2,H->worst_case());
    EXPECT_EQ(3,H->size());
    EXPECT_EQ(1,result);
    result = H->add("cab", collisions); // same bucket
    EXPECT_EQ(2,collisions); // bucket already had 2 elements
    EXPECT_EQ(3,H->worst_case()); // now  bucket has 3 elements
    EXPECT_EQ(4,H->size());
    EXPECT_EQ(1,result);
    
    // the number of collisions depend on the order elements were inserted in the bucket
    // check if inserted element is really there.
    isthere = H->contains("abc",collisions);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(3,collisions); // the first element inserted is at 3rd place in the list
    // node that we just changed the order, the sum must be the same
    isthere = H->contains("bca",collisions);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(2,collisions);// the 2nd element inserted is at 2nd place in the list
    // node that we just changed the order, the sum must be the same
    isthere = H->contains("cab",collisions);
    EXPECT_EQ(1,isthere);// the 3rd element inserted is at 1st place in the list
    EXPECT_EQ(1,collisions);
    
    // node that sum of chars of abd is just 1 + sum(abc)
    isthere = H->contains("abd",collisions);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(1,collisions);
         
    delete H;
      
}// Add4Elements

TEST(Lab1Hash, AddAndRemoveMany){
    int collisions; int isthere; int result;
    char c[3]; c[2] = '\0'; int hashsize = 0;
    Hash *H = new Hash(29,hashdiv29);
    char lastchar = 'j';    
    
    // add a lot of strings
    for (c[0] = 'a'; c[0] <= lastchar ; c[0]++) { 
        for (c[1] = 'a'; c[1] <= lastchar ; c[1]++) {
            std::string s(c);
            result = H->add(s, collisions); 
            hashsize++; // every add increases size
            ASSERT_EQ(hashsize,H->size());
            ASSERT_EQ(1,result);
        } // for c2
    }//for c1
    // check if all strings are there
    for (c[0] = 'a'; c[0] <= lastchar ; c[0]++) { 
        for (c[1] = 'a'; c[1] <= lastchar ; c[1]++) {
            std::string s(c);
            isthere = H->contains(s,collisions);
            ASSERT_EQ(1,isthere);
        } // for c2
    }//for c1
    // remove half of them
    for (c[0] = 'a'; c[0] <= lastchar ; c[0]+=2) { 
        for (c[1] = 'a'; c[1] <= lastchar ; c[1]+=2) {
            std::string s(c);
            result = H->remove(s, collisions); 
            hashsize--; // each removal must be successfull
            ASSERT_EQ(hashsize,H->size());
            ASSERT_EQ(1,result);
            result = H->remove(s, collisions); // but we can not remove again
            ASSERT_EQ(0,result);
            ASSERT_EQ(hashsize,H->size());
        } // for c2
    }//for c1
    // remove all
    for (c[0] = 'a'; c[0] <= lastchar ; c[0]++) { 
        for (c[1] = 'a'; c[1] <= lastchar ; c[1]++) {
            std::string s(c);
            result = H->remove(s, collisions); 
            if (result) hashsize--; // removal may or may not be sucessfull
            ASSERT_EQ(hashsize,H->size());
            result = H->remove(s, collisions); // but we can not remove again
            ASSERT_EQ(0,result);
            ASSERT_EQ(hashsize,H->size());
        } // for c2
    }//for c1
    
    // at the end it must be empty
    EXPECT_EQ(0,H->size());
    EXPECT_EQ(0,H->worst_case());
} // AddAndremove

/*
 * reads of file of strings and adds the strings to the Hash H
 */
int HashFile(Hash* H,std::string filename) {
    std::ifstream infile(filename);
    
    int readlines = 0; int collisions = 0;
    std::string line;
    while (std::getline(infile, line)) {
        H->add(line, collisions);
        readlines++;
    }
    infile.close();
    return readlines;
}

std::string getDataDir() { return "../data/"; }


TEST(Lab1Hash, AddFileRandom){
    
    std::string datadir = getDataDir();
    
    int collisons; int isthere; int readlines;
    Hash *H = new Hash(29,hashdiv29);
    readlines = HashFile(H,datadir+"random.txt");
    EXPECT_EQ(700, readlines);
    EXPECT_EQ(42, H->worst_case());
    isthere = H->contains("Paris",collisons);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(23,collisons);
    isthere = H->contains("thy",collisons);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(3,collisons);
    isthere = H->contains("ITA",collisons);
    EXPECT_EQ(0,isthere);
    EXPECT_EQ(19,collisons);   
    delete H;
    
    
} //  AddFile

TEST(Lab1Hash, AddFilelength8){
    
    std::string datadir = getDataDir();
    
    int collisons; int isthere; int readlines;
    Hash *H = new Hash(29,hashdiv29);
    readlines = HashFile(H,datadir+"length8.txt");
    EXPECT_EQ(700, readlines);
    EXPECT_EQ(34, H->worst_case());
    isthere = H->contains("sidewalk",collisons);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(27,collisons);
    isthere = H->contains("epilogue",collisons);
    EXPECT_EQ(1,isthere);
    EXPECT_EQ(18,collisons);
    isthere = H->contains("ITA",collisons);
    EXPECT_EQ(0,isthere);
    EXPECT_EQ(20,collisons);   
    delete H;    
    
} //  AddFile



