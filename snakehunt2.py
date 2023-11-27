import faker
import random

class Snake:
    total_snakes = 0
    total_victims = 0
    def __init__(self, name="Snaky"):
        self.name = name
        self.victims = 0
        Snake.total_snakes += 1

    def hunt(self, mice=1):
        self.victims += mice
        Snake.total_victims += mice

    def __str__(self):
        return f"I am {self.name}, I have {self.victims} mice in my belly"

# snakes_list = []
# for i in range(100):
#     snakes_list.append(Snake())
myfaker = faker.Faker()
snakes_list = [Snake(myfaker.first_name()) for i in range(10)]


for snake in snakes_list:
    print(snake)

print("Total victims:", Snake.total_victims)

for snake in snakes_list:
    snake.hunt(random.randint(0,10))
print("The hunt is over")
for snake in snakes_list:
    print(snake)

print("Total victims:", Snake.total_victims)