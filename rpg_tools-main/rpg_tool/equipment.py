############# EQUIPMENT #############
class Weapon:
    def __init__(self, name, damage_types, base_damage, weapon_tags, description=None, other_effects=None):
        self.other_effects = other_effects
        self.description = description
        self.name = name
        self.damage_types = damage_types
        self.base = base_damage
        self.tags = weapon_tags

    def weapon_might(self, char_stats):
        self.current_damage = self.base + char_stats["Attack"]
        for skill in self.damage_types:
            if skill in char_stats.skill.values():
                self.current_damage += skill

    def item_boosts(self, character):
        # for damage_type in self.damage_types:
        #     if damage_type in character.item.tags:
        #         self.current_damage *= character.item.multiplier
        pass

class Armor:
    def __init__(self, defense, armor_tags=None, effects=None, description=None):
        self.description = description
        self.effects = effects
        self.armor_tags = armor_tags
        self.defense = defense



# class berserker_armor(armor):
#     while True:
#         if Ability.cooldown == True:
#             if anger in Ability.tags:
#                 Ability.cooldown == False