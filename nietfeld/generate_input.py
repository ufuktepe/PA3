import random

def generate_nums ():
    random.seed()
    file = open("input.txt", "w")
    #file.write("10\n8\n7\n6\n5")
    for i in range(100):
        file.write(str(random.randint(1, 10 ** 12)) + "\n")