import json

class DarkSoulsRoutes:
    def __init__(self, routes):
        self.routes = routes

    def display_routes(self):
        # Displaying the routes for visualization
        for location, connections in self.routes.items():
            print(location + " connects to:")
            for neighbor, weight in connections.items():
                print(f"  - {neighbor} with weight {weight}")
            print()

    def find_route(self, origin, destination):
        pass

# Load JSON file with Lordran routes defined
lordran_routes_json = open('./lordran_routes.json')
lordran_routes = json.load(lordran_routes_json)

ds_test = DarkSoulsRoutes(lordran_routes)
ds_test.display_routes()