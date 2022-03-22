#include "hash.h"

// LOOK FOR THE COMMENTS IN THE .H 
// TO UNDERSTAND WHAT EACH FUNCTION MUST DO

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

    // porque existe 'return 0' neste codigo? 
    // para executar os testes, mesmo falhando, eh preciso compilar
    // assim, eh preciso retornar algum valor.
    // ** o aluno deve implementar a funcao completa e retornar o valor correto **
    return 1;
    
}//add

int Hash::remove(std::string str, int &collisions) { 
    
    if (contains(str, collisions)){
        int bucket = hash(str);
        _table[bucket].remove(str);
        return 1;
    }
    return 0;
}//remove


int Hash::hash(std::string str) { 
    
    return _hash_func(str);
    
}//hash
    
int Hash::contains(std::string str, int &collisions) { 

    int bucket = hash(str);
    std::forward_list<std::string> list = _table[bucket];

    //Create an iterator of std::list
    std::forward_list<std::string>::iterator it;
    collisions = 0;
    for (it = list.begin(); it!= list.end(); it++){
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

