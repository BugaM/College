
#include <mysortfunctions.h>
#include <queue>

void myradixsort(std::vector<int> &v, SortStats &stats) {
    std::vector<std::queue<int>> queues;
    queues.resize(16);
    unsigned long maxSize = v.size();
    unsigned int maxBits = 0;
    while (maxSize){
        maxBits++;
        maxSize >>= 1;
    }

    for (int b = 0, factor = 0; b < maxBits/4 + 1; b++, factor+=4){
        for (int i : v){
            int key = i >> factor & 0x0F;
            queues[key].push(i);
        }
        for (int j=0, k=0; j<16; j++){
            while(! queues[j].empty()){
                v[k++] = queues[j].front();
                queues[j].pop();
            }
        }


    }
    // not recursive
    stats.recursive_calls = 1;
    stats.depth_recursion_stack = 1;
}
