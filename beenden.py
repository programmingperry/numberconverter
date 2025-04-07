# Abschlussprojekt Zahlenkonverter Programm Nele McCurrach
# ____________________________________________________________________________________________________________________
# Mechanismen zum Fortführen oder Beenden des Programms
import sys

# ____________________________________________________________________________________________________________________
# Funktion um die Zahleneingabe fortlaufend weiterzuführen
def weitermachen():
    while True:
        weitere_zahl = input('Möchtest du eine weitere Zahl eingeben? (j/n):\n>>>>> ').lower()
        if weitere_zahl == 'n':
            sicherheitsabfrage()
            return False
        elif weitere_zahl == 'j':
            print('Weiter geht die wilde Sause!\n')
            return True
        else:
            print("Ungültige Eingabe! Das Programm wird beendet.")
            sys.exit(0)



# ____________________________________________________________________________________________________________________
# Sicherheitsabfrage bei Auswahl Programm Beenden
def sicherheitsabfrage():
    while True:
        sicherheitsfrage = input('Willst du das Programm wirklich beenden? (j / n)\n>>>>> ').lower()
        if sicherheitsfrage == 'j':
            print('Das Programm wird beendet. Tschüss!')
            sys.exit(0)
        elif sicherheitsfrage == 'n':
            print('Toll, einfach toll, dass du dich für den super duper Zahlenkonverter entscheidest!')
            break
        elif sicherheitsfrage != 'j' and sicherheitsfrage != 'n':
            print('Keine gültige Eingabe.')


# ____________________________________________________________________________________________________________________
# Verhindert Ausführung, wenn Name der Py-Datei nicht main ist
if __name__ == "__main__":
    weitermachen()
    sicherheitsabfrage()

