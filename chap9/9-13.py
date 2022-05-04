from random import randint

class Die:

    def __init__(self,side=6):
        self.sides = side

    def roll_die(self):
        print(randint(1,self.sides))

if __name__ == '__main__':
    run = Die()
    i = 0
    while i < 10:
        i += 1
        run.roll_die()
    print('--------')
    i = 0
    run = Die(10)
    while i < 10:
        i += 1
        run.roll_die()
    print('--------')
    i = 0
    run = Die(20)
    while i < 10:
        i += 1
        run.roll_die()