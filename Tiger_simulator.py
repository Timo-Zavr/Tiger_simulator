import random
import time
import os
clear = lambda: os.system('cls')
clear()

# print("🐯🌿🌿🐰🌿")
# print("🌿🌿🌿🌿🌿")
# print("🌿🌿🌿🌿🌿")
# print("🌿🌿🐰🌿🌿")
# print("🌿🌿🌿🌿🌿")

class Rabbit:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    

class Tiger:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.emout = "Выслеживает добычу"
    def wolk(self):
        kd = random.choice(["-x", "x", "-y", "y"])
        if kd == "x" and self.x < 4:
            self.x += 1
        if kd == "-x" and self.x > 0:
            self.x -= 1
        if kd == "y" and self.y < 4:
            self.y += 1
        if kd == "-y" and self.y > 0:
            self.y -= 1
    def is_raddit(self):
        if self.y == R1.y and self.x+1 == R1.x:
            self.emout = "Тигр атакует!"
        elif self.x == R1.x and self.y+1 == R1.y:
            self.emout = "Тигр атакует!"
        elif self.y == R1.y and self.x-1 == R1.x:
            self.emout = "Тигр атакует!"
        elif self.x == R1.x and self.y-1 == R1.y:
            self.emout = "Тигр атакует!"
        else:
            self.emout = "Выслеживает добычу"
    def atack(self):
        kd = random.choice(["yes","no"])
        self.y = R1.y
        self.x = R1.x
        reset_doard()
        if kd == "yes":
            self.emout = "Сытый тигр идёт домой"
            return True
        elif kd == "no":
            self.emout = "Тигр не поймал зайца"
            return False

            # R1.y = random.randint(0,4)
            # R1.x = random.randint(0,4)
            # R1.x = random.randint(0,4)

T = Tiger()
R1 = Rabbit(random.randint(0,4), random.randint(0,4))
# if R1.y == 0 and R1.x == 0:
#     R1 = Rabbit(random.randint(0,4), random.randint(0,4))
area = [["🌿","🌿","🌿","🌿","🌿"],
        ["🌿","🌿","🌿","🌿","🌿"],
        ["🌿","🌿","🌿","🌿","🌿"],
        ["🌿","🌿","🌿","🌿","🌿"],
        ["🌿","🌿","🌿","🌿","🌿"]]

def reset_doard():
    time.sleep(0.25)
    clear()
    for y in range(5):
        area[y] = ["🌿","🌿","🌿","🌿","🌿"]
    area[R1.y][R1.x] = "🐰"
    area[T.y][T.x] = "🐯"
    for y in range(5):
        line = ""
        for i in area[y]:
            line += i
        print(line)

while True:
    if T.emout == "Выслеживает добычу":
        T.wolk()
        reset_doard()
        T.is_raddit()
        print(T.emout)
    elif T.emout == "Тигр атакует!":
        reset_doard()
        print(T.emout)
        if not T.atack():
            reset_doard()
            print(T.emout)
            time.sleep(0.5)
            R1.y = random.randint(0,4)
            R1.x = random.randint(0,4)
            T.emout = "Выслеживает добычу"
    elif T.emout == "Сытый тигр идёт домой":
        T.x = 0
        T.y = 0
        R1.y = 0
        R1.x = 0
        reset_doard()
        print(T.emout)
        break
    else:
        reset_doard()
        print(T.emout)
        break