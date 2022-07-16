class Room:
    room_cost = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses = value
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            result += sum(x.get_monthly_expense() for x in items)
        self.expenses = result

    @staticmethod
    def __validate_expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$\n" \
               f"--- Appliances monthly cost: {self.expenses:.2f}$"
