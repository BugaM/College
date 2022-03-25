#include "hash.h"

Hash::Hash(int tablesize, int (*hf) (std::string) ) {
    _table.resize(tablesize);
    _hash_func = hf;

 // CONSTRUTOR 
}

int Hash::add(std::string str, int &collisions) { 
    int bucket = hash(str);
    if (contains(str, collisions)){
        return 0;
    }
    _table[bucket].push_front(str);
    return 1;
    
}//add

int Hash::remove(std::string str, int &collisions) { 
    
    if (contains(str, collisions)){
        int bucket = hash(str);
        std::forward_list<std::string> *list = &_table[bucket];
        auto it = list->begin();
        if (collisions == 1){
            list->pop_front();
        }
        else{
            std::advance(it, collisions-2);
            list->erase_after(it);
        }
        return 1;
    }
    return 0;
}//remove


int Hash::hash(std::string str) { 
    
    return _hash_func(str);
    
}//hash
    
int Hash::contains(std::string str, int &collisions) { 

    int bucket = hash(str);
    std::forward_list<std::string> *list = &_table[bucket];

    //Create an iterator of std::list
    std::forward_list<std::string>::iterator it;
    collisions = 0;
    for (it = list->begin(); it!= list->end(); it++){
        collisions ++;
        if (*it == str){
            return 1;
        }
    }
    return 0;
    
}//contains


int Hash::worst_case() {

    int collisions;
    int max = 0;
    std::forward_list<std::string> list;
    std::forward_list<std::string>::iterator it;

    for (std::forward_list<std::string> & i : _table){
        collisions = 0;
        list = i;
        for (it = list.begin(); it!= list.end(); it++, collisions++);
        if (collisions > max){
            max = collisions;
        }
    }

    return max;
    
}//worst_case

int Hash::size() {

    int collisions = 0;
    std::forward_list<std::string> list;
    std::forward_list<std::string>::iterator it;

    for (std::forward_list<std::string> & i : _table){
        list = i;
        for (it = list.begin(); it!= list.end(); it++, collisions++);
    }

    return collisions;
    
}//size

