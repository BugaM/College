#ifndef TSP_SOLVER
#define TSP_SOLVER


#include <TspReader.h>
#include <vector>
#include <queue>

class TspSolver {
public:
    // you should fill percourse with a permutation that represents the TSP solution
    void solve(TspReader &tr,std::vector<int> &percourse);
    void visit(std::vector<std::vector<int>> &tree, std::vector<int> &percourse, std::vector<bool> &visited, int i);
    struct Vert;
    struct CompDist;
    
        


}; 



#endif
