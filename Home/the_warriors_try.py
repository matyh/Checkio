#!/usr/bin/env checkio --domain=py run the-warriors


# END_DESC
# from __future__ import annotations
from typing import List, Union, Any, Type


class Warrior:
    def __init__(self):
        self.health: int = 50
        self.max_health = self.health
        self.attack: int = 5
        self.defense: int = 0

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    @property
    def is_alive(self):
        return self.health > 0

    def set_health(self, x: int):
        self.health = x

    def damage(self, damage: Union[int, float]):
        self.health -= damage

    def attack_enemy(self, enemy: 'Warrior'):
        enemy.damage(self.attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack: int = 7


class Defender(Warrior):
    def __init__(self):
        self.health = 60
        super().__init__()
        self.attack = 3
        self.defense = 2

    def damage(self, damage: Union[int, float]):
        if damage > self.defense:
            self.health -= (damage - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism: float = 0.50

    def attack_enemy(self, enemy: Warrior):
        enemy.damage(self.attack)
        # healing vampire for the 'vampirism' times damage done to the enemy
        self.health += self.vampirism * (self.attack - enemy.defense)


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        

class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 0
        self.healing = 2

    def heal(self, unit: Warrior):
        max_health = {Warrior: 50, Knight: 50, Defender: 60, Vampire: 40, Lancer: 50}
        if max_health[type(unit)] - unit.health > 2:
            unit.health += self.healing
        else:
            unit.health = max_health[type(unit)]


class Army:
    def __init__(self):
        self.units: List[Warrior] = []

    def add_units(self, unit_type, qty: int):
        self.units += [unit_type() for _ in range(qty)]

    def get_fighter(self):
        """
        Returns first unit from Army which is alive.
        """
        for unit in self.units:
            if unit.is_alive:
                return unit
            else:
                pass

    def get_units(self):
        return self.units


class Battle:
    @staticmethod
    def fight(army1: Army, army2: Army) -> bool:
        """
        Returns True if army1 wins, else returns False
        """
        fighter1 = army1.get_fighter()
        fighter2 = army2.get_fighter()
        while fighter1.is_alive and fighter2.is_alive:
            fighter1.attack_enemy(fighter2)
            if isinstance(fighter1, Lancer) and fighter2 is not army2.get_units()[-1]:
                army2.units[army2.get_units().index(fighter2) + 1].damage(fighter1.get_attack() * 0.5)
            if fighter1 is not army1.get_units()[-1]:
                second = army1.get_units()[army1.get_units().index(fighter1) + 1]
                if isinstance(second, Healer):
                    second.heal(fighter1)
            if not fighter2.is_alive:
                fighter2 = army2.get_fighter()
                if fighter2 is None:
                    return True
                continue
            fighter2.attack_enemy(fighter1)
            if isinstance(fighter2, Lancer) and fighter1 is not army1.get_units()[-1]:
                army1.units[army1.get_units().index(fighter1) + 1].damage(fighter2.get_attack() * 0.5)
            if fighter2 is not army2.get_units()[-1]:
                second = army2.get_units()[army2.get_units().index(fighter2) + 1]
                if isinstance(second, Healer):
                    second.heal(fighter2)
            if not fighter1.is_alive:
                fighter1 = army1.get_fighter()
                if fighter1 is None:
                    return False
                continue
        # attacker_army = army1
        # idle_army = army2
        # # zkouska jestli to pujde bez opakovani kodu pro attackera a idle
        # attacker = attacker_army.get_fighter()
        # idle = idle_army.get_fighter()
        # while attacker.is_alive and idle.is_alive:
        #     attacker.attack_enemy(idle)
        #     if isinstance(attacker, Lancer):
        #         idle_army.units[idle_army.get_units().index(idle) + 1].damage(attacker.get_attack() * 0.5)
        #     if not idle.is_alive:
        #         idle = idle_army.get_fighter()
        #         if idle is None and idle in army2.get_units():
        #             return True
        #     if not attacker.is_alive:
        #         attacker = attacker_army.get_fighter()
        #         if attacker is None and attacker in army1.get_units():
        #             return False
        #     attacker, idle = idle, attacker
        #     attacker_army, idle_army = idle_army, attacker_army


def fight(unit_1, unit_2):
    # TODO: prizpusobit vsem class - Lancer, Vampire..

    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attack_enemy(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.attack_enemy(unit_1)
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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert chuck.max_health == 50
    assert carl.max_health == 50
    assert bob.max_health == 60

    # assert fight(chuck, bruce) == True
    # assert fight(dave, carl) == False
    # assert chuck.is_alive == True
    # assert bruce.is_alive == False
    # assert carl.is_alive == True
    # assert dave.is_alive == False
    # assert fight(carl, mark) == False
    # assert carl.is_alive == False
    # assert fight(bob, mike) == False
    # assert fight(lancelot, rog) == True
    # assert fight(eric, richard) == False
    # assert fight(ogre, adam) == True
    # assert fight(freelancer, vampire) == True
    # assert freelancer.is_alive == True
    # assert freelancer.health == 14
    # priest.heal(freelancer)
    # assert freelancer.health == 16
    #
    # # battle tests
    # my_army = Army()
    # my_army.add_units(Defender, 2)
    # my_army.add_units(Healer, 1)
    # my_army.add_units(Vampire, 2)
    # my_army.add_units(Lancer, 2)
    # my_army.add_units(Healer, 1)
    # my_army.add_units(Warrior, 1)
    #
    # enemy_army = Army()
    # enemy_army.add_units(Warrior, 2)
    # enemy_army.add_units(Lancer, 4)
    # enemy_army.add_units(Healer, 1)
    # enemy_army.add_units(Defender, 2)
    # enemy_army.add_units(Vampire, 3)
    # enemy_army.add_units(Healer, 1)
    #
    # army_3 = Army()
    # army_3.add_units(Warrior, 1)
    # army_3.add_units(Lancer, 1)
    # army_3.add_units(Healer, 1)
    # army_3.add_units(Defender, 2)
    #
    # army_4 = Army()
    # army_4.add_units(Vampire, 3)
    # army_4.add_units(Warrior, 1)
    # army_4.add_units(Healer, 1)
    # army_4.add_units(Lancer, 2)
    #
    # battle = Battle()
    #
    # assert battle.fight(my_army, enemy_army) == False
    # assert battle.fight(army_3, army_4) == True
    # print("Coding complete? Let's try tests!")
