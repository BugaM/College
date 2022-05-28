#include <TrocoSolver.h>

void TrocoSolverDivConquer::solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins) {

    coins.resize(denom.size(),0);
    unsigned int troco = value;
    recursion(denom, value, coins, troco);
}//solve

unsigned int TrocoSolverDivConquer::recursion(const std::vector<unsigned int> &denom ,unsigned int value,
                                              std::vector<unsigned int> &coins, unsigned int troco){
    recursivecalls ++;
    if (troco == 0){
        return 0;
    }
    if (troco < denom[1]){
        coins[0] = troco;
        return troco;
    }
    unsigned int q = troco;
    unsigned int aux;
    auto vec = coins;
    auto best = coins;
    for (int i = 0; i < denom.size(); i++){
        if (denom[i] > troco) continue;
        aux = q;
        vec = coins;
        q = std::min(q, 1 + recursion(denom , value, vec, troco - denom[i]));
        if (aux != q){
            vec[i] ++;
            best = vec;
        }
    }
    coins = best;
    return q;
}