"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Procházka
email: michael.p@hotmail.com
"""

def print_intro():
    print("Welcome to Tic Tac Toe")
    print("=" * 40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 40)
    print("Let's start the game")
    print("-" * 40)

def vytiskni_mrizku(mrizka):
    """Vytiskne aktuální stav hrací mřížky."""
    print("+---+---+---+")
    for i in range(3):
        print("| {} | {} | {} |".format(*mrizka[i]))
        print("+---+---+---+")

def ziskej_souradnice(cislo_tahu):
    """Převede číslo tahu (1-9) na řádek a sloupec."""
    cislo_tahu -= 1
    radek = cislo_tahu // 3
    sloupec = cislo_tahu % 3
    return radek, sloupec

def je_vitez(mrizka, hrac):
    """Zkontroluje, zda je v aktuální mřížce vítěz."""
    for i in range(3):
        if all(mrizka[i][j] == hrac for j in range(3)):
            return True
        if all(mrizka[j][i] == hrac for j in range(3)):
            return True
    if all(mrizka[i][i] == hrac for i in range(3)):
        return True
    if all(mrizka[i][2 - i] == hrac for i in range(3)):
        return True
    return False

def hraj_piskvorky():
    mrizka = [[" " for _ in range(3)] for _ in range(3)]
    aktualni_hrac = "O"
    pocet_tahu = 0

    print_intro()

    while True:
        vytiskni_mrizku(mrizka)
        print("=" * 40)
        tah = input(f"Player {aktualni_hrac.lower()} | Please enter your move number: ")

        if not tah.isdigit() or int(tah) < 1 or int(tah) > 9:
            print("Invalid move. Please enter a number from 1 to 9.")
            continue

        radek, sloupec = ziskej_souradnice(int(tah))
        if mrizka[radek][sloupec] != " ":
            print("This cell is already taken. Try another move.")
            continue

        mrizka[radek][sloupec] = aktualni_hrac
        pocet_tahu += 1

        if je_vitez(mrizka, aktualni_hrac):
            vytiskni_mrizku(mrizka)
            print(f"Congratulations, the player {aktualni_hrac.lower()} WON!")
            break

        if pocet_tahu == 9:
            vytiskni_mrizku(mrizka)
            print("It's a draw!")
            break

        aktualni_hrac = "O" if aktualni_hrac == "X" else "X"

if __name__ == "__main__":
    hraj_piskvorky()