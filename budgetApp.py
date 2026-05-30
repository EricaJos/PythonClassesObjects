#You should have a Category class that accepts a name as the argument.
class Category:
    pass
    def __init__(self, name):
        self.name = name
        #The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.
        self.ledger = []

    #The Category class should have the following methods:

    # - A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
    def deposit(self, amount, description = ''):
        specific_obj = {'amount': amount, 'description': description}
        self.ledger.append(specific_obj)
        

    # - A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            specific_obj = {'amount': -amount, 'description': description}
            self.ledger.append(specific_obj)
            return True
        else:
            return False

    # - A get_balance method that returns the current category balance based on ledger.
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    # - A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
    def transfer(self,amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    # - A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.
    def check_funds(self, amount):
        return amount <= self.get_balance()



    # When a Category object is printed, it should:
    def __str__(self):
        # - Display a title line of 30 characters with the category name centered between * characters.
        title = f"{self.name:*^30}\n"
        items = ''
        # - List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        # - Show a final line Total: [balance], where [balance] should be replaced by the category total.
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# You should have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string. To build the chart:

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        withdrawals = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_amounts.append(withdrawals)
    total_spent = sum(spent_amounts)
    percentages = []
    if total_spent > 0:
        for spent in spent_amounts:
            percent = int((spent / total_spent) * 100)
            percentages.append(percent - (percent % 10))
    else:
        percentages = [0] * len(categories)

    chart = 'Percentage spent by category\n'
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + '| '
        for percent in percentages:
            chart += 'o  ' if percent >= level else '   '
        chart += '\n'

    chart += '    ' + '-' + '---' * len(categories) + '\n'
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += '     '
        for category in categories:
            chart += (category.name[i] + '  ') if i < len(category.name) else '   '
        chart += '\n'

    if chart.endswith('\n'):
        chart = chart[:-1]

    return chart


#food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')