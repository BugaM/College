//
// Created by buga on 05/04/2022.
//

#ifndef LABTREE_REDBLACKTREE_H
#define LABTREE_REDBLACKTREE_H

#ifndef shp
#define shp  std::shared_ptr
#endif

#ifndef mshp
#define mshp std::make_shared
#endif

#include "Node.h"
#include <memory>
#include <vector>

class RedBlackTree {
public:
        RedBlackTree();
        ~RedBlackTree() = default;
        void add(double key, long idx);
        void leftRotate(shp<Node> x);
        void rightRotate(shp<Node> x);
        void insertFixUp(shp<Node> z);
        long size();
        void find(std::vector<long> &res, double first, double last );
        void smartInOrder(shp<Node> &node, std::vector<long> &res, double first, double last);
private:
        shp<Node> _root;
        shp<Node> NIL;
        long size(shp<Node> &node);

};


#endif //LABTREE_REDBLACKTREE_H
