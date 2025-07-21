import math

class PickupRouteOptimizer:
    def __init__(self, locations):
        """
        locations: List of tuples (name, x, y)
        Example: [("Location A", 1, 2), ("Location B", 4, 6), ...]
        """
        self.locations = locations

    def distance(self, loc1, loc2):
        # Euclidean distance
        return math.sqrt((loc1[1] - loc2[1]) ** 2 + (loc1[2] - loc2[2]) ** 2)

    def optimize_route(self, start_index=0):
        if not self.locations:
            return []

        visited = [False] * len(self.locations)
        route = [start_index]
        visited[start_index] = True

        current = start_index
        for _ in range(len(self.locations) - 1):
            nearest = None
            min_dist = float('inf')
            for i, loc in enumerate(self.locations):
                if not visited[i]:
                    dist = self.distance(self.locations[current], loc)
                    if dist < min_dist:
                        min_dist = dist
                        nearest = i
            route.append(nearest)
            visited[nearest] = True
            current = nearest

        return [self.locations[i][0] for i in route]  # Return route by location names

# Example usage:
if __name__ == "__main__":
    locations = [
        ("Warehouse", 0, 0),
        ("A", 2, 3),
        ("B", 5, 4),
        ("C", 1, 7),
        ("D", 6, 1)
    ]
    optimizer = PickupRouteOptimizer(locations)
    route = optimizer.optimize_route()
    print("Optimized Pickup Route:", " -> ".join(route))