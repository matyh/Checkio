#!/usr/bin/env checkio --domain=py run the-warriors


# END_DESC
from typing import List, Union, Any


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    @property
    def is_alive(self):
        return self.health > 0

    def set_health(self, x):
        self.health = x

    def damage(self, damage: int):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage_done = (self.attack - enemy.defense) if isinstance(enemy, Defender) else self.attack
        enemy.health -= damage_done
        if isinstance(self, Vampire):
            self.health += self.vampirism * damage_done


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def damage(self, damage: int):
        if damage > self.defense:
            self.health -= (damage - self.defense)
        else:
            pass


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.50


class Army:
    def __init__(self):
        self.units: List[Union[Warrior, Knight]] = []

    def add_units(self, unit_type, qty: int):
        self.units += [unit_type() for _ in range(qty)]

    def get_fighter(self):
        return self.units.pop(0)

    def get_units(self):
        return self.units


class Battle:
    def fight(self, army1, army2):
        """
        :param Army army1:
        :param Army army2:
        :return: boolean
        """
        fighter1 = army1.get_fighter()
        fighter2 = army2.get_fighter()
        while fighter1.is_alive and fighter2.is_alive:
            fighter1.attack_enemy(fighter2)
            if not fighter2.is_alive:
                if army2.get_units():
                    fighter2 = army2.get_fighter()
                    continue
                else:
                    return True
            fighter2.attack_enemy(fighter1)
            if not fighter1.is_alive:
                if army1.get_units():
                    fighter1 = army1.get_fighter()
                    continue
                else:
                    return False


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.damage(unit_1.get_attack())
        if not unit_2.is_alive:
            return True
        unit_1.damage(unit_2.get_attack())
        if not unit_1.is_alive:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 11)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 13)
    battle = Battle()

    assert battle.fight(army_1, army_2) == True

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")