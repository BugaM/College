
#include <mysortfunctions.h>

void merge(std::vector<int> &v, std::vector<int> &aux, int i, int m, int f){
    int i1 = i;
    int i2 = i;
    int i3 = m + 1;
    while (i2 <= m && i3 <= f)
        if (v[i2] < v[i3])
            aux[i1++] = v[i2++];
        else
            aux[i1++] = v[i3++];
    while (i2 <= m)
        aux[i1++] = v[i2++];
    while (i3 <= f)
        aux[i1++] = v[i3++];
    for (int j=i; j<=f; j++)
        v[j] = aux[j];
}

void mergeSortRecursive(std::vector<int> &v, std::vector<int> &aux, SortStats &stats, int i, int f, int depth){
    if (depth > stats.depth_recursion_stack){
        stats.depth_recursion_stack = depth;
    }
    if (i < f) {
        int m = (i+f)/2;
        stats.recursive_calls ++;
        mergeSortRecursive(v, aux, stats, i, m, depth + 1);
        stats.recursive_calls ++;
        mergeSortRecursive(v, aux, stats, m+1, f, depth + 1);
        merge(v, aux, i, m, f);
    }
}


void mymergesort_recursive(std::vector<int> &v, SortStats &stats) {
    std::vector<int> aux;
    aux.resize(v.size());

    stats.depth_recursion_stack = 0;
    stats.recursive_calls = 1;
    mergeSortRecursive(v, aux, stats, 0, v.size() -1, 1);
}

void mymergesort_iterative(std::vector<int> &v, SortStats &stats) {
    std::vector<int> aux;
    aux.resize(v.size());
    int i = 0;
    int f = v.size() - 1;
    int b = 1; // b: tamanho de cada bloco
    int p, r ,m;
    while (b < f) {
        p = i; // p: posição inicial do 1º bloco
        while (p+b <= f) {
            r = (f < p-1 + 2*b) ? f:(p-1+2*b); // r: posição final do 2º bloco
            m = p+b-1; // m: posição final do 1º bloco
            merge(v, aux, p, m, r);
            p += 2*b;
        }
        b *= 2; // tamanho dos blocos é duplicado
    }

    // no recursion
    stats.recursive_calls = 0;
    stats.depth_recursion_stack = 0;
}
    
