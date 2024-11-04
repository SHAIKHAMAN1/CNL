class Router:
    def __init__(self, num_nodes):
        # Initialize the number of routers and the distance matrix
        self.num_nodes = num_nodes
        self.distance_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]  # Distance matrix initialized with infinity
        self.next_hop = [[-1] * num_nodes for _ in range(num_nodes)]  # Next hop matrix initialized with -1
        self.initialize_router()

    def initialize_router(self):
        # Initialize the distance matrix and next hop matrix (for direct links)
        for i in range(self.num_nodes):
            self.distance_matrix[i][i] = 0  # Distance to self is always 0
            self.next_hop[i][i] = i  # Next hop to self is self

    def set_edge(self, src, dest, cost):
        # Set the distance and next hop for direct links
        self.distance_matrix[src][dest] = cost
        self.distance_matrix[dest][src] = cost  # For an undirected graph, both directions have the same cost
        self.next_hop[src][dest] = dest
        self.next_hop[dest][src] = src

    def update_routing_table(self):
        # Update the routing table using the Distance Vector Routing Algorithm
        for k in range(self.num_nodes):  # Intermediate node
            for i in range(self.num_nodes):  # Source node
                for j in range(self.num_nodes):  # Destination node
                    # If a shorter path is found through an intermediate node, update the distance and next hop
                    if self.distance_matrix[i][k] + self.distance_matrix[k][j] < self.distance_matrix[i][j]:
                        self.distance_matrix[i][j] = self.distance_matrix[i][k] + self.distance_matrix[k][j]
                        self.next_hop[i][j] = self.next_hop[i][k]

    def print_routing_table(self):
        # Print the final routing table (distance and next hop for each router)
        print("\nDistance Vector Routing Table:")
        for i in range(self.num_nodes):
            print(f"Router {i + 1}:")
            for j in range(self.num_nodes):
                print(f"  To {j + 1}: Cost = {self.distance_matrix[i][j]}, Next hop = {self.next_hop[i][j] + 1}")
            print()

# Function to get user input
def get_user_input():
    num_nodes = int(input("Enter the number of routers: "))  # Number of routers
    router = Router(num_nodes)

    print("\nEnter the cost of the links (enter -1 if no direct link exists):")
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            cost = int(input(f"Cost between Router {i + 1} and Router {j + 1}: "))  # Input the cost between routers
            if cost != -1:
                router.set_edge(i, j, cost)

    return router

# Main program
if __name__ == "__main__":
    # Get user input and initialize the routers
    router = get_user_input()
    
    print("\nUpdating routing tables using Distance Vector Routing Protocol...")
    router.update_routing_table()  # Update the routing table based on the distance vector algorithm
    router.print_routing_table()  # Print the final routing table
