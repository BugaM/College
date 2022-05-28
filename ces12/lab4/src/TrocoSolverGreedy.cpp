#include <TrocoSolver.h>

void TrocoSolverGreedy::solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins) {
    coins.resize(denom.size(),0);
    unsigned int troco = 0;
    auto curr = denom.size() - 1;
    while (curr >= 0 and troco < value){
        while (denom[curr] > value){
            curr --;
        }
        while (troco < value){
            troco += denom[curr];
            coins[curr] ++;
        }
        if (troco == value) return;
        troco -= denom[curr];
        coins[curr] --;
        curr --;
    }
}//solve

// dica: iterar um vetor de tras pra frente
//https://stackoverflow.com/questions/3610933/iterating-c-vector-from-the-end-to-the-begin
//http://www.cplusplus.com/reference/vector/vector/rbegin/
