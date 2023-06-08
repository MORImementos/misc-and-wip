class Player:
    def __init__(self, roster:list, gold:int, income:dict, inventory:list, research:dict):
        self.research = research # values being list where [progress, interval]
        self.inventory = inventory
        self.income = income
        self.gold = gold
        self.roster = roster

    def add_income(self, exclude=None):
        """calculate and add income to player gold"""
        for source, amount in self.income.items():
            if source not in exclude:
                self.gold += amount

    def advance_research(self, exclude=None):
        """calculate and advance research"""
        for source, research in self.research.items():
            if source not in exclude:
                research[0] += research[1]