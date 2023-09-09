import json

class DarkSoulsRoutes:
    """Main class with the operations between Dark Souls routes."""

    def __init__(self, routes):
        """Initialize the DarkSoulsRoutes with the provided routes.
        
        Parameters:
            ``routes`` (dict): A dictionary mapping locations to their neighbors and weights.
            
        Examples
        --------
        >>> routes = {
        ...     "Firelink Shrine": {"Undead Burg": 5},
        ...     "Undead Burg": {"Firelink Shrine": 5}
        ... }
        >>> ds = DarkSoulsRoutes(routes)
        """
        self.routes = routes

    def display_routes(self):
        """Display the routes for visualization in a nicer format.

        Examples
        --------
        >>> ds_routes = DarkSoulsRoutes(lordran_routes)
        >>> ds_routes.display_routes()
        Firelink Shrine connects to:
            - Undead Burg with weight 5
        Undead Burg connects to:
            - Firelink Shrine with weight 5
        """
        for location, connections in self.routes.items():
            print(location + " connects to:")
            for neighbor, weight in connections.items():
                print(f"  - {neighbor} with weight {weight}")
            print()

    def find_route(self, origin, destination):
        # TODO
        pass

# Load JSON file with Lordran routes defined (weights are incorrect)
lordran_routes_json = open('../data/lordran_routes.json')
lordran_routes = json.load(lordran_routes_json)
ds_routes = DarkSoulsRoutes(lordran_routes)
ds_routes.display_routes()