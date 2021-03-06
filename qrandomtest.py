import random as rand
from typing import Dict, List, Union
import numpy as np
import requests

_ANU_PARAMS: Dict[str, Union[int, str]] = {
    "length": 1,
    "type": "hex16",
    "size": 8,
}
_ANU_URL: str = "https://qrng.anu.edu.au/API/jsonI.php"

def get_qrand_int64() -> List[int]:
    """Get quantum random int64s from the ANU API."""
    response = requests.get(_ANU_URL, _ANU_PARAMS)
    response.raise_for_status()
    r_json = response.json()

    if r_json["success"]:
        return [int(number, 16) for number in r_json["data"]]
    else:
        raise RuntimeError(
            "The 'success' field in the ANU response was False."
        )
#print(len(get_qrand_int64()))

while(True):
    try:
        randomMethod = int(input("What random sort do you want? Enter the corresponding number.\n 1) Flip a coin\n 2) Select individuals from a group\n "))

        if randomMethod == 1:
            no_flips = int(input("Flip how many times?: "))
            for i in range(no_flips):
                rand.seed(get_qrand_int64()[0])
                coin = rand.randint(0, 1)
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
                rand.seed(get_qrand_int64()[0])
                chance = rand.random()
                while chance == any in list_chance:
                    rand.seed(get_qrand_int64()[0])
                    chance = rand.random()
                nameChance_dict[chance] = name
                list_chance.append(chance)
                new = np.asarray(list_chance)
            choose_how_many = int(input("How many individuals must be selected?: "))
            # print(new, type(new))
            sorted_list = np.argsort(new)
            # print(sorted_list)

            for k in range(choose_how_many):
                print(nameChance_dict[new[sorted_list[len(sorted_list) - 1 - k]]])
    except:
        continue
