class Expense:
    # Constructor to initialize an Expense object with name, category, and amount
    def __init__(self, name, category, amount) -> None:
        self.name = name  # The name of the expense
        self.category = category  # The category to which the expense belongs
        self.amount = amount  # The amount of the expense

    # Representation method to define how an Expense object is printed
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
        # Provides a string representation of the object, showing the name, category, and amount
