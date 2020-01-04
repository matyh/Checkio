from Home.the_war import *


class TestUnits:
    def test_Warrior(self):
        war = Warrior()
        assert war.get_health() == 50
        assert war.get_attack() == 5
        assert war.defense == 0
        war.damage(10)
        assert war.get_health() == 40
        assert war.is_alive is True

    def test_Knight(self):
        knight = Knight()
        assert knight.get_health() == 50
        assert knight.get_attack() == 7
        assert knight.is_alive is True
        knight.damage(15)
        assert knight.get_health() == 35

    def test_Defender(self):
        defender = Defender()
        assert defender.get_health() == 60
        assert defender.get_attack() == 3
        assert defender.is_alive is True
        defender.damage(10)
        assert defender.get_health() == 52
        defender.damage(54)
        assert defender.get_health() == 0
        assert defender.is_alive is False


class TestInteractions:
    def test_fight(self):
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

        assert fight(chuck, bruce) is True
        assert chuck.is_alive is True
        assert bruce.is_alive is False


class TestBattle:
    def test_straight_fight(self):
