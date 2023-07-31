import csv
import time
import os


def menu():

    print("|!| Pixelmon Helper |!|")
    print("\n[1] Pokemon's EVs")
    print("\n[2] Pokemon's Info")
    print("\n[9] Quit")
    
    answer = input("\n>> ")
    if answer == "1":
        os.system("cls")
        evs()
    if answer == "2":
        os.system("cls")
        pokedex()
    if answer == "9":
        os.system("cls")
        print("Made By Robert Mapes")
        time.sleep(3)
        quit()
    else:
        os.system("cls")
        menu()

def evs():

    print("|!| Pixelmon Helper |!|")
    user_pokemon = input("\nPokemon's Name >> ")
    file = csv.reader(open("./data/evs_data.csv"))

    for row in file:
        if row[0].lower() == user_pokemon.lower():
            print("\n" + row[0])
            print("HP : " + row[1] , "\nAttack : " + row[2] , "\nDefense : " + row[3] , "\nSpecial Attack : " + row[4] , "\nSpecial Defense : " + row[5] , "\nSpeed : " + row[6])
            input()
            break


    os.system("cls")
    menu()

def pokedex():

    print("|!| Pixelmon Helper |!|")
    user_pokemon = input("\nPokemon's Name >> ")
    file = csv.reader(open("./data/pokemon_data.csv"))

    for row in file:
        if row[1].lower() == user_pokemon.lower():
            print("\n" + row[0] + ". " + row[1] + "\nType : " + row[9] + "/" + row[10])
            print("\nHP : " + row[2] , "\nAttack : " + row[3] , "\nDefense : " + row[4] , "\nSpecial Attack : " + row[5] , "\nSpecial Defense : " + row[6] , "\nSpeed : " + row[7] , "\nTotal : " + row[8])
            print("\nAbilities : " + row[11] + "/" +  row[12] + "\nHidden Ability : " + row[13])
            print("\nSteps Taken to Hatch : " + row[16])
            input()
            break


    os.system("cls")
    menu()



menu()

















