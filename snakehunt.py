import random
import string
import faker

class Snake:
    amount = 0
    victims = 0

    def __init__(self, name="Nobody"):
        self.name = name
        self.victims = 0
        Snake.amount += 1
        print(f"{self.name} is born")

    def hunt(self, victims=1):
        self.victims += victims
        Snake.victims += victims
        print(f"{self.name} ate {self.victims}")

    def hiss(self):
        return f"{self.name} says: sssss..."

# snake1 = Snake("Alice")
# snake1.hunt(2)
# snake2 = Snake("Bob")
# snake2.hunt(2)
# snake2.hunt(4)

# print(snake1.name, snake1.victims, Snake.victims)
# print(snake2.name, snake2.victims, Snake.victims)

# let's create many snakes

n = 10  # how many snakes we want

# create list od snakes with random names
# snakes = [Snake("".join(random.choices(string.ascii_uppercase, k=4))) for i in range(n)]
snakes = [Snake(faker.Faker().first_name()) for i in range(n)]
print(snakes)

# let's hunt!
for snake in snakes:
    prey = random.randint(0, 10)
    snake.hunt(prey)

