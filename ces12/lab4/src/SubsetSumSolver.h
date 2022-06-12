#ifndef SSP_SOLVER
#define SSP_SOLVER


#include <vector>
#include <string>
#include <algorithm>
#include <SubsetSumSolverAbstract.h>


class SSPSolverAluno2 : public SubsetSumSolverAbstract {

    
public:
    
    virtual bool solve(const std::vector< long> &input,
                        long value, std::vector< char> &output);
        
    virtual std::string getName() { return "A2"; }

    class Set;

    static void bruteForce(const std::vector< long> &input, std::vector<Set> &subsets,
                    Set &found, long value);


}; 

class SSPSolverExtra : public SubsetSumSolverAbstract {

    
public:
    
    virtual bool solve(const std::vector< long> &input,
                        long value, std::vector< char> &output);
        
    virtual std::string getName() { return "EX"; }
    
}; 

class SSPSolverPD : public SubsetSumSolverAbstract {

public:
    
    virtual bool solve(const std::vector< long> &input,
                        long value, std::vector< char> &output);
    
    virtual std::string getName() { return "PD"; }

}; 

#endif
