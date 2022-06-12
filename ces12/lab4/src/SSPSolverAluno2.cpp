#include <SubsetSumSolver.h>


/// Aluno2: segunda solucao do aluno = Meet-in-the-Middle OU Branch & Bound
class SSPSolverAluno2::Set{
public:
    Set(){
        sum = 0;
    }
    bool operator < ( const Set& val ) const {
        return sum < val.sum;
    }
    void add(int index, long value){
        elements.push_back(index);
        sum += value;
    }
    void shift_elements(long value){
        for (auto &element : elements)
            element+= value;
    }
    void merge(Set b){
        elements.insert(elements.end(), b.elements.begin(), b.elements.end());
        sum += b.sum;
    }
    std::vector<long> elements;
    long sum;
};

bool SSPSolverAluno2::solve(const std::vector< long> &input,
                            long value, std::vector< char> &output) {

    std::vector<Set> leftSubsets;
    std::vector<Set> rightSubsets;
    Set found = Set();
    output.resize(input.size(), false);

    // divide input in two
    long halfSize = input.size() / 2;
    std::vector<long> lowerInput(input.begin(), input.begin() + halfSize);
    std::vector<long> higherInput(input.begin() + halfSize, input.end());

    // bruteForce left vector
    bruteForce(lowerInput, leftSubsets, found, value);
    // case solution not only in left vector
    if (found.sum != value){
        bruteForce(higherInput, rightSubsets, found, value);
        // shift to make indexes correct
        if (found.sum == value) {
            found.shift_elements(halfSize);
        }
        // case answer also isnt only in right vector
        else {
            std::vector<long> sumsLeft, sumsRight;
            sumsLeft.resize(leftSubsets.size());
            sumsRight.resize(rightSubsets.size());

            // sorting subsets by sum
            std::sort(leftSubsets.begin(), leftSubsets.end());
            std::sort(rightSubsets.begin(), rightSubsets.end());

            long p1 = 0;
            long p2 = rightSubsets.size() - 1;
            long total;
            while (p1 < leftSubsets.size() and p2 >= 0){
                total = leftSubsets[p1].sum + rightSubsets[p2].sum;
                if (total == value){ // solution found
                    rightSubsets[p2].shift_elements(halfSize);
                    leftSubsets[p1].merge(rightSubsets[p2]);
                    found = leftSubsets[p1];
                    break;
                }
                else if (total < value) p1 ++; // increase total by increasing left sum values
                else p2 --; // decrease total by decreasing right sum
            }
            if (found.sum != value){
                return false;
            }
        }
    }
    // completing output
    for (auto element : found.elements){
        output[element] = true;
    }
    return true;

}

void SSPSolverAluno2::bruteForce(const std::vector< long> &input, std::vector<Set> &subsets,
                                 Set &found, long value) {
    Set empty_set = Set();
    subsets.push_back(empty_set);

    int n = input.size();
    for (int i=0; i<n; i++){
        std::vector<Set> newSubsets;
        for (const auto &oldSet: subsets){
            Set newSet = oldSet;
            newSet.add(i, input[i]);
            if (newSet.sum == value){
                found = newSet;
                return;
            }
            newSubsets.push_back(newSet);
            newSubsets.push_back(oldSet);
        }
        subsets = newSubsets;
    }
}

