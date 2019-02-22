#!/usr/bin/env checkio --domain=py run the-defenders

# https://py.checkio.org/mission/the-defenders/

# 
# END_DESC

# Taken from mission Army Battles








# Taken from mission The Warriors


class Army(list):
    def add_units(self, Solider, count):
        for i in range(count):
            solider = Solider()
            self.append(solider)


class Battle:
    def _get_first_solider(self, army):
        return army.pop(0)

    def fight(self, army1, army2):
        if len(army1) == 0:
            return False
        if len(army2) == 0:
            return True

        s1 = self._get_first_solider(army1)
        s2 = self._get_first_solider(army2)

        while True:
            if fight(s1, s2):
                try:
                    s2 = self._get_first_solider(army2)
                except IndexError:
                    return True
            else:
                try:
                    s1 = self._get_first_solider(army1)
                except IndexError:
                    return False


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive is False:
            return True

        unit_1.health -= unit_2.attack
        if unit_1.is_alive is False:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")