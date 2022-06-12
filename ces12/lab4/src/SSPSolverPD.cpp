#include <SubsetSumSolver.h>



 bool SSPSolverPD::solve(const std::vector< long> &input,
                            long value, std::vector< char> &output) {
    
    int n = input.size();
    long c = value;
    output.resize(n);
    std::vector<std::vector<long>> B;
    B.resize(n + 1, std::vector<long>(c+1,0));
    for (int k=1; k<=n; k++) // incremento nos itens
         for (int i=0; i<=c; i++) // incremento na capacidade
            if (input[k-1] > i){
                B[k][i] = B[k-1][i];
            }
            else B[k][i] = std::max(B[k-1][i], B[k-1][i-input[k-1]] + input[k-1]);


    long s = B[n][c];
    if (c != s) return false;

    // obtains vector
    for (long i = n -1; i>=0; i--){
        if( B[i][s] == s)
            output[i] = false;
        else {
            output[i] = true;
            s -= input[i];
        }
    }
    return true;
}
