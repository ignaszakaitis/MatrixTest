# insulin_pen_dashboard.py

class InsulinPenDashboard:
    def __init__(self):
        self.battery = 80
        self.history = [
            {"id": 1, "time": "08:00 AM", "dose": "10 units"},
            {"id": 2, "time": "12:00 PM", "dose": "8 units"},
            {"id": 3, "time": "06:00 PM", "dose": "12 units"},
        ]
    
    def use_battery(self):
        if self.battery > 0:
            self.battery -= 10
    
    def display_dashboard(self):
        print("Insulin Pen Dashboard")
        print(f"Battery Level: {self.battery}%")
        print("Dosage History:")
        for entry in self.history:
            print(f"{entry['time']} - {entry['dose']}")

if __name__ == "__main__":
    dashboard = InsulinPenDashboard()
    dashboard.display_dashboard()