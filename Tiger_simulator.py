import random
import time
import os
clear = lambda: os.system('cls')
clear()

class Tiger:
    def __init__(self):
        self.state = "Выследить добычу"
        self.successful_attack_prob = 0.5
        self.x, self.y = 0, 0

    def update_state(self, rabbits):
        if self.state == "Выследить добычу":
            print("Тигр выслеживает добычу!")
            self.move_randomly()
            if any(self.is_near_rabbit(rabbit) for rabbit in rabbits):
                self.state = "Атаковать добычу"
        elif self.state == "Атаковать добычу":
            if random.random() < self.successful_attack_prob:
                print("Тигр успешно атаковал зайца!")
                for rabbit in rabbits:
                    if self.is_near_rabbit(rabbit):
                        rabbit.to_capture()
                time.sleep(0.333)
                self.state = "Бежать домой"
            else:
                print("Тигр промахнулся!")
                time.sleep(0.333)
        elif self.state == "Бежать домой":
            self.x, self.y = 0, 0

    def move_randomly(self):
        kd = random.choice(["-x", "x", "-y", "y"])
        if kd == "x":
            self.x += 1
        if kd == "-x":
            self.x -= 1
        if kd == "y":
            self.y += 1
        if kd == "-y":
            self.y -= 1
        self.x = max(0, min(self.x, 4))
        self.y = max(0, min(self.y, 4))

    def is_near_rabbit(self, rabbit):
        if self.y == rabbit.y and self.x+1 == rabbit.x:
            return True
        elif self.x == rabbit.x and self.y+1 == rabbit.y:
            return True
        elif self.y == rabbit.y and self.x-1 == rabbit.x:
            return True
        elif self.x == rabbit.x and self.y-1 == rabbit.y:
            return True
        else:
            return False

    def __str__(self):
        return f"T (тигр): ({self.x}, {self.y})"

class Rabbit:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.captured = False  # схвачен или нет

    def to_capture(self):
        self.captured = True

    def __str__(self):
        return f"З (заяц): ({self.x}, {self.y})"

def print_field(tiger, rabbits):
    field = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append("🌿")
        field.append(row)

    field[tiger.x][tiger.y] = "🐯"
    for rabbit in rabbits:
        if not rabbit.captured:
            field[rabbit.x][rabbit.y] = "🐰"
    for row in field:
        print("".join(row))

def main():
    tiger = Tiger()
    rabbit1 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbit2 = Rabbit(random.randint(1, 4), random.randint(1, 4))
    rabbits = [rabbit1, rabbit2]

    while tiger.state != "Бежать домой":
        print_field(tiger, rabbits)
        tiger.update_state(rabbits)
        time.sleep(0.333)
        clear()

    tiger.update_state(rabbits)
    print_field(tiger, rabbits)
    if tiger.state == "Бежать домой":
        print("Тигр вернулся домой.")

if __name__ == "__main__":
    main()

# # print("🐯🌿🌿🐰🌿")
# # print("🌿🌿🌿🌿🌿")
# # print("🌿🌿🌿🌿🌿")
# # print("🌿🌿🐰🌿🌿")
# # print("🌿🌿🌿🌿🌿")

# class Rabbit:
#     def __init__(self, y, x):
#         self.y = y
#         self.x = x
        
    

# class Tiger:
#     def __init__(self):
#         self.y = 0
#         self.x = 0
#         self.emout = "Выслеживает добычу"
#     def wolk(self):
#         kd = random.choice(["-x", "x", "-y", "y"])
#         if kd == "x" and self.x < 4:
#             self.x += 1
#         if kd == "-x" and self.x > 0:
#             self.x -= 1
#         if kd == "y" and self.y < 4:
#             self.y += 1
#         if kd == "-y" and self.y > 0:
#             self.y -= 1
#     def is_raddit(self):
#         if self.y == R1.y and self.x+1 == R1.x:
#             self.emout = "Тигр атакует!"
#         elif self.x == R1.x and self.y+1 == R1.y:
#             self.emout = "Тигр атакует!"
#         elif self.y == R1.y and self.x-1 == R1.x:
#             self.emout = "Тигр атакует!"
#         elif self.x == R1.x and self.y-1 == R1.y:
#             self.emout = "Тигр атакует!"
#         else:
#             self.emout = "Выслеживает добычу"
#     def atack(self):
#         kd = random.choice(["yes","no"])
#         self.y = R1.y
#         self.x = R1.x
#         reset_doard()
#         if kd == "yes":
#             self.emout = "Сытый тигр идёт домой"
#             return True
#         elif kd == "no":
#             self.emout = "Тигр не поймал зайца"
#             return False

#             # R1.y = random.randint(0,4)
#             # R1.x = random.randint(0,4)
#             # R1.x = random.randint(0,4)

# T = Tiger()
# R1 = Rabbit(random.randint(0,4), random.randint(0,4))
# # if R1.y == 0 and R1.x == 0:
# #     R1 = Rabbit(random.randint(0,4), random.randint(0,4))
# area = [["🌿","🌿","🌿","🌿","🌿"],
#         ["🌿","🌿","🌿","🌿","🌿"],
#         ["🌿","🌿","🌿","🌿","🌿"],
#         ["🌿","🌿","🌿","🌿","🌿"],
#         ["🌿","🌿","🌿","🌿","🌿"]]

# def reset_doard():
#     time.sleep(0.25)
#     clear()
#     for y in range(5):
#         area[y] = ["🌿","🌿","🌿","🌿","🌿"]
#     area[R1.y][R1.x] = "🐰"
#     area[T.y][T.x] = "🐯"
#     for y in range(5):
#         line = ""
#         for i in area[y]:
#             line += i
#         print(line)

# while True:
#     if T.emout == "Выслеживает добычу":
#         T.wolk()
#         reset_doard()
#         T.is_raddit()
#         print(T.emout)
#     elif T.emout == "Тигр атакует!":
#         reset_doard()
#         print(T.emout)
#         if not T.atack():
#             reset_doard()
#             print(T.emout)
#             time.sleep(0.5)
#             R1.y = random.randint(0,4)
#             R1.x = random.randint(0,4)
#             T.emout = "Выслеживает добычу"
#     elif T.emout == "Сытый тигр идёт домой":
#         T.x = 0
#         T.y = 0
#         R1.y = 0
#         R1.x = 0
#         reset_doard()
#         print(T.emout)
#         break
#     else:
#         reset_doard()
#         print(T.emout)
#         break