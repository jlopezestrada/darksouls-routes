import unittest
import json
from darksouls_routes import DarkSoulsRoutes

class TestDarkSoulsRoutes(unittest.TestCase):
    def setUp(self):
        lordran_routes_json = open('../data/lordran_routes.json')
        lordran_routes = json.load(lordran_routes_json)
        self.ds_routes = DarkSoulsRoutes(lordran_routes)

    def test_direct_connection(self):
        route = self.ds_routes.find_route("Firelink Shrine", "Undead Burg")
        self.assertEqual(route, ["Firelink Shrine", "Undead Burg"])

    def test_multi_node_route(self):
        route = self.ds_routes.find_route("Firelink Shrine", "The Depths")
        self.assertEqual(route, ["Firelink Shrine", "Undead Burg", "Lower Undead Burg", "The Depths"])
    
    def test_invalid_origin(self):
        with self.assertRaises(ValueError):
            self.ds_routes.find_route("Belfry Sol", "Undead Burg")
    
    def test_same_origin_destination(self):
        route = self.ds_routes.find_route("Firelink Shrine", "Firelink Shrine")
        self.assertEqual(route, ["Firelink Shrine"])