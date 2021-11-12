import qrandom
import numpy as np

randomMethod = int(input("What random sort do you want? Enter the corresponding number.\n 1) Flip a coin\n 2) Select individuals from a group\n "))

if randomMethod == 1:
    no_flips = int(input("Flip how many times?: "))
    for i in range(no_flips):
        coin = qrandom.randint(0, 1)
        if coin == 0:
            print("tails")
        if coin == 1:
            print("heads")

if randomMethod == 2:
    list_chance = []
    nameChance_dict = {}
    no_individuals = int(input("How many individuals?: "))

    for j in range(no_individuals):
        name = str(input("Name: "))
        chance = qrandom.random()
        while chance == any in list_chance:
            chance = qrandom.random()
        nameChance_dict[chance] = name
        list_chance.append(chance)
        new = np.asarray(list_chance)
    choose_how_many = int(input("How many individuals must be selected?: "))
    # print(new, type(new))
    sorted_list = np.argsort(new)
    # print(sorted_list)

    for k in range(choose_how_many):
        print(nameChance_dict[new[sorted_list[len(sorted_list) - 1 - k]]])