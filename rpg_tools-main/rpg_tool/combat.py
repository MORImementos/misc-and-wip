import random

class Combat:
    def __init__(self, attacker, attack_type, defenders, status=False):
        self.status = status
        self.defenders = defenders
        self.attack_type = attack_type
        self.attacker = attacker

    def attack(self):
        pass

    def counter_attack(self):
        # if self.status == True:
        #     if ViciousFighter in defenders.Ability or ViciousSilverPin in defenders.Item:
        #         return True
        #
        #     else:
        #         return False
        pass

def rng_gen(target, check_higher_value=False):
    """rng roller for accuracy, percent activation, etc"""
    randnum = random.randint(1, 100)
    if not check_higher_value:
        if randnum <= target:
            return True
        else:
            return False

    elif check_higher_value:
        if randnum >= target:
            return True
        else:
            return False

def accuracy_check(attacker_hit, defender_avoid):
    """calculate accuracy of an attack"""
    probability = attacker_hit - defender_avoid
    if probability >= 0:
        return True
    elif probability <= 0:
        probability = 100 + probability
        accuracy_test = rng_gen(probability)
        return accuracy_test

def turn_counter():
    """count the turns of a battle"""
    player_turn = False
    npc_turn = False

    if player_turn == True and npc_turn == True:
        return True


def active_speed():
    pass

def active_skill():
    pass

def active_move():
    pass

def active_avoid():
    pass