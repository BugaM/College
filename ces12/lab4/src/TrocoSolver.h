#ifndef TROCO_SOLVER
#define TROCO_SOLVER


#include <vector>
#include <string>
#include <TrocoSolverAbstract.h>


class TrocoSolverDivConquer : public TrocoSolverAbstract {
private:
    long recursivecalls;

public:
    
    virtual void solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins); 
    
     /// how many recursive calls in the last run of solve()
    virtual long countRecursiveCalls() { return recursivecalls; }
    virtual unsigned int recursion(const std::vector<unsigned int> &denom,unsigned int value,
                                   std::vector<unsigned int> &coins, unsigned int troco);
    
    virtual std::string getName() { return "DC"; }
    
}; 

class TrocoSolverPD : public TrocoSolverAbstract {

public:
    
    virtual void solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins);
    
    virtual std::string getName() { return "PD"; }
    
}; 

class TrocoSolverGreedy : public TrocoSolverAbstract {

public:
    
    virtual void solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins); 

    virtual std::string getName() { return "GR"; }    
}; 


#endif
