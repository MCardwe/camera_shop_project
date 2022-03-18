import unittest
from models.camera import Camera
from models.make import Make

class TestCamera(unittest.TestCase):
    
    def setUp(self):
        self.canon = Make("Canon")
        self.camera = Camera("250d", "Canon", "Compact DSLR", "Lightweight APS-C mid-range camera", 5, 250, 500)

    def test_camera_has_name(self):
        self.assertEqual("250d", self.camera.name)

    def test_camera_has_make(self):
        self.assertEqual("Canon", self.camera.make)

    def test_camera_has_type(self):
        self.assertEqual("Compact DSLR", self.camera.type)

    def test_camera_has_description(self):
        self.assertEqual("Lightweight APS-C mid-range camera", self.camera.description)

    def test_camera_has_stock_count(self):
        self.assertEqual(5, self.camera.stock)

    def test_camera_has_buy_price(self):
        self.assertEqual(250, self.camera.buy_price)

    def test_camera_has_sell_price(self):
        self.assertEqual(500, self.camera.sell_price)

    def test_camera_id_is_none(self):
        self.assertEqual(None, self.camera.id)