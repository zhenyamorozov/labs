import random

class Snake:
    total = 0
    total_victims = 0
    def __init__(self, name="Python"):
        self.name = name
        self.victims = 0
        Snake.total += 1
    def hunt(self, food=1):
        self.victims += food
        Snake.total_victims += food
    def __str__(self):
        return f"Snake {self.name} ate {self.victims}"



# let's create many snakes!
n = 10
amount_food = 50
# snakes_list = []
# for i in range(n):
#     snakes_list.append(Snake())
snakes_list = [Snake(f"Python{i+1}") for i in range(n)]

for snake in snakes_list:
    print(snake)
print(f"Total snakes: {Snake.total}")
print(f"Total eaten: {Snake.total_victims}")

for snake in snakes_list:
    food = random.randint(0,10)
    food = food if food<=amount_food else amount_food
    snake.hunt(food)
    amount_food -= food


for snake in snakes_list:
    print(snake)
print(f"Total snakes: {Snake.total}")
print(f"Total eaten: {Snake.total_victims}")
pass