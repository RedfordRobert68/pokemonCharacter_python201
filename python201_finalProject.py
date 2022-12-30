# Ask for user input
# Create a dynamic URL based on Step 1
# Fetch the data from the URL in Step 2
# Convert JSON to a dictionary
# Print out Pokemon data

# import json
import requests


# ************************************
# Functions
# ***********************************
def get_character():
    print(f"\nName:\t\t{pokemon['name'].capitalize()}")
    print(f"ID:\t\t{pokemon['id']}")
    print(f"Weight\t\t{pokemon['weight']}")
    print(f"Base Experience:{pokemon['base_experience']}")
    print("\nAbilities:")
    for ability in pokemon['abilities']:
        print(ability['ability']['name'])


    print("\nStrengths:")
    for stat in pokemon['stats']:
        print(stat['stat']['name'])

    print("\n")
    
while True:

    character_choice = input("What character would you like to see? ")
    character_choice = character_choice.lower()

    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{character_choice}")

    if req.status_code == 200:
        pokemon = req.json()
        get_character()

        find_another = input("Would you like to view another character? Yes? No? ")
        if find_another.lower() == "no":
            exit()
        elif find_another.lower() == "yes":
            continue
        else:
            while True:
                find_another = input("Would you like to view another character? Yes? No? ")
                if find_another.lower() == "no":
                    exit()
                elif find_another.lower() == "yes":
                    break
 
    else:
        print("The requested character does not exist in the database.")

        retry = input("Would you like to try again? Yes or No? ")
        if retry.lower() == "no":
            exit()
        elif retry.lower() == "yes":
            continue
        else:
            while True:
                retry = input("Would you like to try again? Yes or No? ")
                if retry.lower() == "no":
                    exit()
                elif retry.lower() == "yes":
                    break


# print(type(pokemon))

 