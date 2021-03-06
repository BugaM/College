from grid import Node, NodeGrid
from math import inf
import heapq


class PathPlanner(object):
    """
    Represents a path planner, which may use Dijkstra, Greedy Search or A* to plan a path.
    """

    def __init__(self, cost_map):
        """
        Creates a new path planner for a given cost map.

        :param cost_map: cost used in this path planner.
        :type cost_map: CostMap.
        """
        self.cost_map = cost_map
        self.node_grid = NodeGrid(cost_map)

    @staticmethod
    def construct_path(goal_node):
        """
        Extracts the path after a planning was executed.

        :param goal_node: node of the grid where the goal was found.
        :type goal_node: Node.
        :return: the path as a sequence of (x, y) positions: [(x1,y1),(x2,y2),(x3,y3),...,(xn,yn)].
        :rtype: list of tuples.
        """
        node = goal_node
        # Since we are going from the goal node to the start node following the parents, we
        # are transversing the path in reverse
        reversed_path = []
        while node is not None:
            reversed_path.append(node.get_position())
            node = node.parent
        return reversed_path[::-1]  # This syntax creates the reverse list

    def dijkstra(self, start_position, goal_position):
        """
        Plans a path using the Dijkstra algorithm.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
        # The first return is the path as sequence of tuples (as returned by the method construct_path())
        # The second return is the cost of the path
        self.node_grid.reset()
        pq = []
        node = self.node_grid.get_node(start_position[0], start_position[1])
        node.f = 0
        heapq.heappush(pq, (node.f, node))
        while pq:
            f, node = heapq.heappop(pq)
            if node.closed is True:
                continue
            i, j = node.get_position()
            if i is goal_position[0] and j is goal_position[1]:
                return self.construct_path(node), node.f
            node.closed = True
            position = node.get_position()
            for successor_position in self.node_grid.get_successors(position[0], position[1]):
                successor = self.node_grid.get_node(successor_position[0], successor_position[1])
                if not successor.closed and successor.f > node.f + self.cost_map.get_edge_cost(position, successor_position):
                    successor.f = node.f + self.cost_map.get_edge_cost(position, successor_position)
                    successor.parent = node
                    heapq.heappush(pq, (successor.f, successor))
        return [], inf

    def greedy(self, start_position, goal_position):
        """
        Plans a path using greedy search.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
        self.node_grid.reset()
        pq = []
        node = self.node_grid.get_node(start_position[0], start_position[1])
        # utilizing node.f to storage the heuristic function
        node.f = node.distance_to(goal_position[0], goal_position[1])
        node.g = 0
        heapq.heappush(pq, (node.f, node))
        node.closed = True
        while pq:
            f, node = heapq.heappop(pq)
            # node.closed = True
            position = node.get_position()
            for successor_position in self.node_grid.get_successors(position[0], position[1]):
                successor = self.node_grid.get_node(successor_position[0], successor_position[1])
                if successor.closed is False:
                    successor.parent = node
                    i, j = successor.get_position()
                    # node.closed = True
                    successor.g = node.g + self.cost_map.get_edge_cost(position, successor_position)
                    if i is goal_position[0] and j is goal_position[1]:
                        return self.construct_path(node), successor.g
                    successor.f = successor.distance_to(goal_position[0], goal_position[1])
                    heapq.heappush(pq, (successor.f, successor))
                    successor.closed = True
        # The first return is the path as sequence of tuples (as returned by the method construct_path())
        # The second return is the cost of the path
        return [], inf

    def a_star(self, start_position, goal_position):
        """
        Plans a path using A*.

        :param start_position: position where the planning stars as a tuple (x, y).
        :type start_position: tuple.
        :param goal_position: goal position of the planning as a tuple (x, y).
        :type goal_position: tuple.
        :return: the path as a sequence of positions and the path cost.
        :rtype: list of tuples and float.
        """
        # The first return is the path as sequence of tuples (as returned by the method construct_path())
        # The second return is the cost of the path
        self.node_grid.reset()
        pq = []
        node = self.node_grid.get_node(start_position[0], start_position[1])
        node.g = 0
        node.f = node.distance_to(goal_position[0], goal_position[1])
        heapq.heappush(pq, (node.f, node))
        while pq:
            f, node = heapq.heappop(pq)
            i, j = node.get_position()
            if node.closed is True:
                continue
            if i is goal_position[0] and j is goal_position[1]:
                return self.construct_path(node), node.f
            node.closed = True
            position = node.get_position()
            for successor_position in self.node_grid.get_successors(position[0], position[1]):
                successor = self.node_grid.get_node(successor_position[0], successor_position[1])
                if not successor.closed and successor.f > node.g + \
                        self.cost_map.get_edge_cost(position, successor.get_position()) + \
                        successor.distance_to(goal_position[0], goal_position[1]):
                    successor.g = node.g + self.cost_map.get_edge_cost(position, successor.get_position())
                    successor.f = successor.g + successor.distance_to(goal_position[0], goal_position[1])
                    successor.parent = node
                    heapq.heappush(pq, (successor.f, successor))
        return [], inf
