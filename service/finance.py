class CampusCard:
    def __init__(self):
        self.balance = 100.0

    def balance_inquiry(self):
        # query account balance
        return self.balance

    def recharge(self, amount: float) -> bool:
        # account recharge
        self.balance += amount
        return True

    def deduction(self, amount: float) -> bool:
        # account deduction
        if self.balance < amount:
            return False

        self.balance -= amount
        return True
