import random

def stein_papier_schere():
    optionen = ["Stein", "Papier", "Schere"]
    
    print("Willkommen zu Stein, Papier, Schere!")
    print("Gib deine Wahl ein: 'Stein', 'Papier' oder 'Schere'.")

    # Der Spieler macht seinen Zug
    spieler_wahl = input("Deine Wahl: ").capitalize()

    # Der Computer macht eine zufällige Wahl
    computer_wahl = random.choice(optionen)
    
    print(f"Der Computer wählt: {computer_wahl}")

    # Überprüfen, ob der Spieler gewonnen, verloren oder unentschieden gespielt hat
    if spieler_wahl == computer_wahl:
        print("Unentschieden!")
    elif (spieler_wahl == "Stein" and computer_wahl == "Schere") or \
         (spieler_wahl == "Papier" and computer_wahl == "Stein") or \
         (spieler_wahl == "Schere" and computer_wahl == "Papier"):
        print("Du gewinnst!")
    else:
        print("Der Computer gewinnt!")

# Starte das Spiel
stein_papier_schere()
