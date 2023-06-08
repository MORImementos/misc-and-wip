############# ABILITIES #############
# todo should abilities just be dictionaries that are inputted into an ability effect class? same with tags, etc.
class Ability:
    _ability_types = ["activatable", "persistent", "context-triggered"]

    def __init__(self, description, cost, ability_type, ability_tags, duration=1, probability=None, tiers=1,
                 signature=False):
        self.signature = signature
        self.tiers = tiers
        self.probability = probability
        self.duration = duration
        self.tags = ability_tags
        self.type = ability_type
        self.cost = cost
        self.description = description
