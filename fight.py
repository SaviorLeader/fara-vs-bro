class Character:
    def __init__(self,name, * ,level,health,damage):
        self.name = name
        self.level = level
        self.health = health * level
        self.damage = damage * level
    def attack(self,enemy):
        enemy.health -= self.damage
        return f"{self.name} deals {self.damage} damage to {enemy.name}"
    def is_alive(self):
        return self.health >= 0

class Fara(Character):
   def __str__(self):
        return f"Warrior - {self.name}"

class Bro(Character):
   def __str__(self):
        return f"Mage - {self.name}"

f = Fara("fara",level = 2,health = 100,damage = 50)
b = Bro("bro",level = 2,health = 80,damage = 40)
print(f)
print(b)

round = 1
print(f"{f.name} and {b.name} starts round {round}")

while f.is_alive() and b.is_alive():
    print(f"Round - {round}")       

    print(f.attack(b))
    if not b.is_alive():
        print(f"{b.name} death")
        break
    print(b.attack(f))
    if not f.is_alive():
        print(f"{f.name} death")
        break
  
    round += 1



