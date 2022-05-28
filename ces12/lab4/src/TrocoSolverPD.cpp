#include <TrocoSolver.h>

void TrocoSolverPD::solve(const std::vector<unsigned int> &denom,unsigned int value, std::vector<unsigned int> &coins) {
    coins.resize(denom.size(),0);
    std::vector<unsigned int> quant;
    std::vector<unsigned int> ultima;
    quant.resize(value+1, 0);
    ultima.resize(value+1, 0);
    unsigned int quantProv, ultProv, ult, curr;

    for (int cents = 1; cents <= value; cents++) {
        quantProv = cents; // solução provisória: todas de 1 centavo
        ultProv = 0; // última moeda dessa solução
        for (int j = 0; j < denom.size(); j++) {
            if (denom[j] > cents) continue; // essa moeda não serve
            if (quant[cents - denom[j]] + 1 < quantProv) {
                quantProv = quant[cents - denom[j]] + 1;
                ultProv = j;
            }
        }
        quant[cents] = quantProv; // solução para troco == cents
        ultima[cents] = ultProv; // última moeda dessa solução
    }
    curr = value;
    ult = ultProv;
    while (curr != 0){
        coins[ult] ++;
        curr = curr - denom[ult];
        ult = ultima[curr];

    }
}//solve
