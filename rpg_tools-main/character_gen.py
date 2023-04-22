# make a class that accepts input for allowable abilities


class Character:
    _hp_tiers = {'very low': 0.6, 'low': 0.8, 'small': 1.0, 'medium': 1.2, 'large': 1.4, 'titanic': 2.0}
    # attack, defense, speed, skill, move
    _damage_types = ['sword', 'shield', 'axe', 'marksman', 'fire']
    _skill_levels = {'1': 5, '2': 10, '3': 15, '4': 20, '5': 25}
    _character_types = ['stealth', 'beast']
    _move_types = ['flying', 'walking']

    def __init__(self, name, damage_types="", resist_weakness="", tags="", move_type="",
                 stat_caps=None, level=1, hp_class=1.0, hp=0):
        self.name = name
        self.damage_types = damage_types

        self.resist_weakness = resist_weakness
        self.tags = tags
        self.move_types = move_type
        self.stat_caps = stat_caps
        self.level = level
        self.hp_class = hp_class
        self.stats = []
        self.hp = hp
        self.type = "character"

    def get_current_stats(self):
        """multiply current level by stat caps to get current stats for a given level"""
        _default_stat_caps = [100, 100, 125, 125, 5]

        if self.stat_caps is None:
            self.stat_caps = _default_stat_caps

        if self.level <= 50:

            for stat in self.stat_caps:
                if stat != self.stat_caps[-1]:
                    self.stats.append(int(stat * (self.level / 50)))

            self.stats.append(self.stat_caps[-1])

        if self.level >= 50:
            self.stats[4] += 1

    def assign_skill_levels(self):
        pass

    def display_stats(self):
        """display summary of character stats on screen"""
        print(self.name)
        print(f"HP: {self.hp:,}")
        print(f"Attack: {self.stats[0]:,}")
        print(f"Defense: {self.stats[1]:,}")
        print(f"Speed: {self.stats[2]:,}")
        print(f"Skill: {self.stats[3]:,}")
        print(f"Move: {self.stats[4]}")


    def get_current_hp(self):
        """make current hp value out of thresholds, hp class, etc."""

        self.hp = 0

        # 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100
        hp_thresholds = [450, 900, 1_800, 3_000, 5_100, 9_000, 15_000, 27_000, 40_500, 54_000, 84_000, 120_000, 180_000, 255_000,
                         390_000, 540_000, 840_000, 1_200_000, 1_950_000, 3_000_000]

        # since each tier of 10 is equally split within itself, subtract previous value to determine what amount to
        # add above previous threshold
        hp_to_allocate = [450, 450, 900, 1_200, 2_100, 3_900, 6_000, 12_000, 13_500, 13_500, 30_000, 36_000, 60_000, 75_000,
                          135_000, 150_000, 300_000, 360_000, 750_000, 1_050_000]

        # determine which multiple of 10 the level is in
        hp_index = int(self.level // 5)

        # add previous threshold value to calculated value level modulo 10 to determine remainder over multiple of 10
        # (if 18, I want to get the value of 8, so I can multiply the 20 threshold by 0.8, etc.)
        if hp_index != 0:
            # previous value
            self.hp += int(hp_thresholds[hp_index - 1])

            # value based on level between previous and next
            added_value = int((hp_to_allocate[hp_index]) * ((self.level % 5) * .2))
            self.hp += int(added_value)

        # else statement to avoid index error when level < 10
        elif hp_index == 0:
            self.hp = int(hp_to_allocate[hp_index + 1] * (self.level % 10) * .2)

        # multiply by hp class
        self.hp = round(self.hp * self.hp_class)


# class for character attributes, split attributes and stats and abilities and weapons? tags class


class Tag:
    """use to check attributes of things. stealth type characters, slaying abilities, etc."""
    def __init__(self, name, type_with_tag, context):
        self.name = name
        self.type_with_tag = type_with_tag
        self.context = context

    def check_context(self, target):
        """check the scope of a tag's use against a target to see if it applies"""
        if self.context[0] in target.type:
            if self.context[1] in target.tags:
                print("TRUE")
            else:
                print("FALSE")
        else:
            print("FALSE")


class Ability:
    pass

class CharacterType:
    pass

class Weapon:
    def __init__(self, name, damage_types, damage, tags):
        self.name = name
        self.damage_types = damage_types
        self.damage = damage
        self.tags = tags


test = Character('test', level=50, hp_class=2, tags='demon')
test.get_current_stats()
test.get_current_hp()
test.display_stats()
slaying = Tag('slaying', ['ability', 'weapon', 'item'], ['character', 'demon'])

dragonslayer = Weapon('Dragonslayer', ['blade', 'bludgeon'], [800, 1600, 2400], ['slaying', 'slaying_demon', 'legendary'])
print(dragonslayer.name + ": ", *dragonslayer.damage_types, *dragonslayer.damage, *dragonslayer.tags)

slaying.check_context(test)