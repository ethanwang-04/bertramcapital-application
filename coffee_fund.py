import json, random
from datetime import datetime

class CoffeeFund:
    def __init__(self, filename='coffee_fund_state.json'):
        self.filename = filename
        # Format: {'Name': 'Coffee Type'}
        self.coworkers = {}
        # Format: {'Coffee Type': Price}
        self.prices = {}
        # Format: {'Name': {'Total Paid': Amount, 'Times Paid': Count}}
        self.payments = {}
        # Format: {'YYYY-MM-DD': ['Name1', 'Name2']}
        self.absence_log = {}

        self.load_state()

    def save_state(self):
        state = {
            'coworkers': self.coworkers,
            'prices': self.prices,
            'payments': self.payments,
            'absence_log': self.absence_log
        }
        with open(self.filename, 'w') as f:
            json.dump(state, f)

    def load_state(self):
        try:
            with open(self.filename, 'r') as f:
                state = json.load(f)
                self.coworkers = state.get('coworkers', {})
                self.prices = state.get('prices', {})
                self.payments = state.get('payments', {})
                self.absence_log = state.get('absence_log', {})
        except FileNotFoundError:
            print("No existing state found. Starting fresh.")

    def add_coworker(self, name, coffee_type):
        self.coworkers[name] = coffee_type
        if name not in self.payments:
            self.payments[name] = {'Total Paid': 0, 'Times Paid': 0}

    def remove_coworker(self, name):
        if name in self.coworkers:
            del self.coworkers[name]
            del self.payments[name]

    def set_coffee_price(self, coffee_type, price):
        self.prices[coffee_type] = price

    def calculate_payment(self):
        # Randomly choose 0 to 2 coworkers to be 'absent'
        num_absent = random.randint(0, 2)
        absent_coworkers = random.sample(list(self.coworkers.keys()), num_absent)

        today = datetime.now().strftime('%Y-%m-%d')
        self.absence_log[today] = absent_coworkers

        # Calculate the total only for 'present' coworkers
        daily_total = sum(self.prices[self.coworkers[name]] for name in self.coworkers if name not in absent_coworkers)

        least_paid = min(self.payments, key=lambda x: (self.payments[x]['Total Paid'], self.payments[x]['Times Paid']))
        self.payments[least_paid]['Total Paid'] += daily_total
        self.payments[least_paid]['Times Paid'] += 1

        return least_paid, daily_total, absent_coworkers

    def report(self):
        for name, info in self.payments.items():
            print(f"{name} has paid a total of ${info['Total Paid']:.2f} over {info['Times Paid']} times.")


fund = CoffeeFund()
fund.add_coworker('Bob', 'Cappuccino')
fund.add_coworker('Jeremy', 'Black Coffee')
# Adding the other coworkers similarly
fund.add_coworker('Sam', 'Latte')
fund.add_coworker('Jessica', 'Caramel Macchiato')
fund.add_coworker('Amy', 'Flat White')
fund.add_coworker('Olivia', 'Dark Chocolate Mocha')
fund.add_coworker('Evan', 'Cold Brew')

fund.set_coffee_price('Cappuccino', 5.50)
fund.set_coffee_price('Black Coffee', 2.00)
# Set prices for other coffee types
fund.set_coffee_price('Latte', 4.50)
fund.set_coffee_price('Caramel Macchiato', 6.00)
fund.set_coffee_price('Flat White', 5.00)
fund.set_coffee_price('Dark Chocolate Mocha', 5.75)
fund.set_coffee_price('Cold Brew', 3.45)

payer, amount, absentees = fund.calculate_payment()
print(f"Today, {payer} should pay for the coffee, totaling ${amount:.2f}. Absent: {', '.join(absentees)}")
fund.save_state()

fund.report()