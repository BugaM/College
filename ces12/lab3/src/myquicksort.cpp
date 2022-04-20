
#include <mysortfunctions.h>

int partition(std::vector<int> &v, int left, int right, int pivotIndex){
    int pivot = v[pivotIndex];
    // moving pivot to the left
    v[pivotIndex] = v[left];
    v[left] = pivot;

    int aux;
    int l = left + 1;
    int r = right;

    while (true){
        while (l < right && v[l] < pivot) l++;
        while (r > left && v[r] >= pivot) r--;
        if (l >= r) break;
        aux = v[l];
        v[l] = v[r];
        v[r] = aux;
    }
    v[left] = v[r];
    v[r] = pivot;
    return r;
}

int medianOf3 (std::vector<int> &v, int min,int max){
    int center = (min + max)/2;
    int a = v[min];
    int b = v[center];
    int c = v[max];
    if (a>= b){
        if (b >= c) return center;
        else if (c >= a) return  min;
        else return max;
    }
    else{
        if (a >= c) return min;
        else if(c >= b) return center;
        else return max;
    }
}

void quickSortMedianOf3_2Rec (std::vector<int> &v, SortStats &stats, int min, int max, int depth){
    if (depth > stats.depth_recursion_stack){
        stats.depth_recursion_stack = depth;
    }
    if (min < max) {
        int pivotIndex = medianOf3(v, min, max);
        int p = partition(v, min, max, pivotIndex);
        stats.recursive_calls ++;
        quickSortMedianOf3_2Rec(v, stats, min, p - 1, depth + 1);
        stats.recursive_calls++;
        quickSortMedianOf3_2Rec(v, stats, p + 1, max, depth + 1);
    }
}

void quickSortMedianOf3_1Rec (std::vector<int> &v, SortStats &stats, int min, int max, int depth){
    if (depth > stats.depth_recursion_stack){
        stats.depth_recursion_stack = depth;
    }
    while (min < max) {
        int pivotIndex = medianOf3(v, min, max);
        int p = partition(v, min, max, pivotIndex);
        if (p-min < max - p){
            stats.recursive_calls ++;
            quickSortMedianOf3_1Rec(v, stats, min, p - 1, depth + 1);
            min = p+1;
        }
        else {
            stats.recursive_calls++;
            quickSortMedianOf3_1Rec(v, stats, p + 1, max, depth + 1);
            max = p-1;
        }
    }
}

void quickSortPivot2Rec (std::vector<int> &v, SortStats &stats, int min, int max, int depth){
    if (depth > stats.depth_recursion_stack){
        stats.depth_recursion_stack = depth;
    }
    if (min < max) {
        int p = partition(v, min, max, min);
        stats.recursive_calls ++;
        quickSortPivot2Rec(v, stats, min, p - 1, depth + 1);
        stats.recursive_calls++;
        quickSortPivot2Rec(v, stats, p + 1, max, depth + 1);
    }
}

/// the most common quicksort, with 2 recursive calls
void myquicksort_2recursion_medianOf3(std::vector<int> &v, SortStats &stats) {
    stats.recursive_calls = 0;
    stats.depth_recursion_stack = 0;

    quickSortMedianOf3_2Rec(v, stats, 0, v.size() - 1, 1);
}// function myquicksort_2recursion_medianOf3



/// quicksort with one recursive call
void myquicksort_1recursion_medianOf3(std::vector<int> &v, SortStats &stats) {
    // you need to set the counting of recursive recursive_calls
    stats.recursive_calls = 0;
    // you need to set the depth = the maximum height of the tree of recursion calls. 
    stats.depth_recursion_stack = 0;
    // the tester already knows the size of v and the algorithm name, it already measures time
    // you may set custom1 field if you want to measure anything else.
    quickSortMedianOf3_1Rec(v, stats, 0, v.size() - 1, 1);
} // function myquicksort_1recursion_medianOf3

/// quicksort with fixed pivot 
/// be sure to compare with equivalent implementation 
/// e.g., if you do 1 recursive call, compare with the 1recursion version

void myquicksort_fixedPivot(std::vector<int> &v, SortStats &stats) {
    stats.recursive_calls = 0;
    stats.depth_recursion_stack = 0;
    quickSortPivot2Rec(v, stats, 0, v.size() - 1, 1);
} // myquicksort_fixedPivot





