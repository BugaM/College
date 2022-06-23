#include <TspSolver.h>


struct TspSolver::Vert{
    int index, to, dist;
};

struct TspSolver::CompDist{
    bool operator()(const Vert& a, const Vert& b){
        if (a.dist != b.dist)
            return a.dist > b.dist;
        else if (a.to != b.to){
            return a.to > b.to;
        }
        else return a.index > b.index;
    }
};

void TspSolver::visit(std::vector<std::vector<int>> &tree, std::vector<int> &percourse, std::vector<bool> &visited, int i){
    percourse.push_back(i+1);
    visited[i] = true;
    for (int ind : tree[i]){
        if (not visited[ind]){
            visit(tree, percourse, visited, ind);
        }
    }
}


void TspSolver::solve(TspReader &tr,std::vector<int> &percourse) {
        int n = tr.getNumCities();
        std::vector<City> vc;
        tr.copyCitiesVector(vc);

        // creating the graph - adj graph
        std::vector<std::vector<int>> graph;
        graph.resize(n, std::vector<int>(n));
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                graph[i][j] = vc[i].disti(vc[j]);
            }
        }
        // creating the tree
        std::vector<std::vector<int>> tree;
        tree.resize(n);


        std::priority_queue<Vert, std::vector<Vert>, CompDist> heap;
        std::vector<bool> aux; // aux represents which vertices are in heap
        aux.resize(n, true);
        Vert top{};

        // Prim
        int curr = 0;
        for (int i = 0; i < n-1; i++) {
            aux[curr] = false;
            for (int j = 0; j < n; j++) {
                if (aux[j])
                    heap.push(Vert{j, curr,graph[curr][j]});
            }
            do {
                top = heap.top();
                heap.pop();
            } while (not aux[top.index]);

            // building tree with indexes
            tree[top.to].push_back(top.index);
            tree[top.index].push_back(top.to);
            curr = top.index;
        }

        // pre order tree transversal
        aux[curr] = false; //  aux now represents witch vertices have been visited in transversal - all vertices are false
        visit(tree, percourse, aux, 0);
}//solve

