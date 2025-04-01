# test_insulin_pen.py
import unittest
from insulin_pen_dashboard import InsulinPenDashboard

class TestInsulinPenDashboard(unittest.TestCase):
    def setUp(self):
        self.dashboard = InsulinPenDashboard()

    def test_initial_battery_level(self):
        self.assertEqual(self.dashboard.battery, 80)

    def test_use_battery(self):
        self.dashboard.use_battery()
        self.assertEqual(self.dashboard.battery, 70)

    def test_dosage_history_length(self):
        self.assertEqual(len(self.dashboard.history), 3)

if __name__ == "__main__":
    unittest.main()