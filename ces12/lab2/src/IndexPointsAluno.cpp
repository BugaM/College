
#include <IndexPointsAluno.h>

/// returns the number of elements in the index
long IndexPointsAluno::size() { return _tree.size(_tree.getRoot()); }

/// adds new element to the index. 
void IndexPointsAluno::add (double key, long idx ) { _tree.add(key,idx, _tree.getRoot()); }


void IndexPointsAluno::find(std::vector<long> &res, double first, double last ) {
    
    
  // it is float, so it is not possible to compare with ==
  // the only thing that makes sense is too look for a range from
  // a min value to a max value. 
  // stl::multimap implements this using iterators 
  // you do not need to use iterators, but you need to fill the answer in O(k + logn)
  // where k is the number of elements in the range from first to last
  // in other words: NAO VALE FAZER INORDER COMPLETO E SELECIONAR O RANGE
  // PRECISA UM INORDER ESPERTO QUE ACHA O FIRST em O(log n) E CONTINUA ATE O LAST
  auto itlow = _map.lower_bound (first);  // itlow points to first
  auto itup = _map.upper_bound (last);   // itup points to next after last (not to last)

  // covers range [itlow,itup), which is the same as [itlow, last] or [first, last]
  for (auto it=itlow; it!=itup; ++it)
    //std::cout << (*it).first << " => " << (*it).second << '\n';
    res.push_back((*it).second);

        
}//find
