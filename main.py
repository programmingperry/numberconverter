# Abschlussprojekt Zahlenkonverter Programm Nele McCurrach
# ____________________________________________________________________________________________________________________
# Zusammenführung aller Funktionen und deren Ausführung
from login import *
from zahlenkonverter import *
from beenden import *
from authentifizierung import *

# Hauptfunktion die alle Funktionen in richtiger Reihenfolge aufruft
def main():
    print('\n********* SUPER DUPER ZAHLENKONVERTER *********\n')
    anmeldung()
    while True:
        try:
            arg1 = konvert_wahl()
            arg2 = zahlen_eingabe(arg1)
            konvertierung(arg1,arg2)
            if not weitermachen():
                break
        except KeyboardInterrupt:
            sicherheitsabfrage()


# ____________________________________________________________________________________________________________________
# Verhindert direkte Ausführung der Funktionen beim Import
if __name__ == "__main__":
    main()

