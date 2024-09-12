import random
import requests

class Controller:
    def __init__(self):
        self.daily_demand = 0
        self.total_produced = 0

    def run_day(self):
        self.daily_demand = random.randint(230, 270)  # Random demand between 230 and 270
        print(f"Market demand for the day: {self.daily_demand} products")

        # Send demand to Factory 1
        factory1_url = "http://factory1:5001/produce"
        response1 = requests.post(factory1_url, json={"demand": self.daily_demand})
        produced1 = response1.json().get('produced', 0)
        print(f"Factory 1 produced: {produced1} products")

        self.total_produced = produced1

        if self.total_produced < self.daily_demand:
            remaining_demand = self.daily_demand - self.total_produced
            # Send remaining demand to Factory 2
            factory2_url = "http://factory2:5002/produce"
            response2 = requests.post(factory2_url, json={"demand": remaining_demand})
            produced2 = response2.json().get('produced', 0)
            print(f"Factory 2 produced: {produced2} products")

            self.total_produced += produced2

        print(f"Total products produced: {self.total_produced}")


