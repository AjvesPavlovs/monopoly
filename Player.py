class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.double_turns = 0
        self.rolled_dice = False
        self.next_turn = False
        self.alive = True
        self.debts = []

    def move(self, steps):
        if self.position + steps >= 40:
            self.money += 200  # Passed 'GO'
        self.position = (self.position + steps) % 40
        

    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def earn(self, amount):
        self.money += amount

    class debt:
        def __init__(self, recipient, amount):
            self.recipient = recipient
            self.amount = amount

    def add_debt(self, recipient, amount):
        new_debt = self.debt(recipient, amount)
        self.debts.append(new_debt)
