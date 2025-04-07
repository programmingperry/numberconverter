# Abschlussprojekt Zahlenkonverter Programm Nele McCurrach
# ____________________________________________________________________________________________________________________
# Programm-Hauptteil zur Konvertierungs-Auswahl, Zahleneingabe und Umrechnung
from main import sicherheitsabfrage

# ____________________________________________________________________________________________________________________
# Auswahl-Konvertierungsart
def konvert_wahl():
    # Dictionary zu den Konvertierungs-Auswahlmöglichkeiten
    optionen = {
        'a': ('Dezimal in Hexadezimal', 'dez_hex'),
        'b': ('Dezimal in Binär', 'dez_bin'),
        'c': ('Hexadezimal in Dezimal', 'hex_dez'),
        'd': ('Hexadezimal in Binär', 'hex_bin'),
        'e': ('Binär in Dezimal', 'bin_dez'),
        'f': ('Binär in Hexadezimal', 'bin_hex'),
    }
    # Anzeige der Konvertierungsmöglichkeiten
    print('____________________________________________________________________________________\n\n'
            'Welche Konvertierung willst du vornehmen?\n'
            'a) Dezimal in Hexadezimal\nb) Dezimal in Binär\n'
            'c) Hexadezimal in Dezimal\nd) Hexadezimal in Binär\n'
            'e) Binär in Dezimal\nf) Binär in Hexadezimal\n')
    # Eingabe der Konvertierungsauswahl und Überprüfung, ob Auswahl in optionen Dictionary vorhanden
    while True:
        konvertauswahl = input('>>>>> ').lower()

        if konvertauswahl in optionen: # prüfen, ob Auswahl in dict. "optionen" vorhanden ist
            print(f'Umwandlung von {optionen[konvertauswahl][0]}.') # Ausgabe gewählter Konvertierungsart - Zufriff dict. "optionen", erstes Element
            return optionen[konvertauswahl][1] # Weiterreichen gewählter Konvertierungsart - Zufriff dict. "optionen", zweites Element
        else:
            print('Keine gültige Eingabe, bitte gebe einen Buchstaben zwischen a und f ein.')
            continue # Eingabe startet erneut

# ____________________________________________________________________________________________________________________
# Zahlen Eingabe und Fehlerhandling
def zahlen_eingabe(umwandlung):
    while True:  # Abbruch bei beenden_programm
        zahl_eingabe = input('\nGib eine Zahl ein:\n>>>>> ')

        # Prüfung Dezimal in Hexa / Bin
        if umwandlung == 'dez_hex' or umwandlung == 'dez_bin':
            if zahl_eingabe.isdigit() and int(zahl_eingabe) >= 0:
                print(f'Umwandlung der Zahl {zahl_eingabe}')
                return int(zahl_eingabe)
            else:
                print('Gib eine ganze, positive Zahl ein.')

        # Prüfung Hexa in Dez / Bin
        elif umwandlung == 'hex_dez' or umwandlung == 'hex_bin':
            try:
                int(zahl_eingabe, 16) # prüft ob Eingabe als Hexadez. umwandelbar ist, bei true erfolgt Umwandlung
                print(f'Umwandlung der Zahl {zahl_eingabe}\n')
                return zahl_eingabe.upper()
            except ValueError:
                print('Gib eine Hexadezimalzahl im Bereich 0 bis 9 und A bis F ein.')

        # Prüfung Binär in Dez / Hexa
        elif umwandlung == 'bin_dez' or umwandlung == 'bin_hex':
            if all(c in "01" for c in zahl_eingabe):  # Überprüft, ob alle Zeichen (c) 0 oder 1 sind
                print(f'Umwandlung der Zahl {zahl_eingabe}')
                return zahl_eingabe
            else:
                print("Gib eine gültige Binärzahl (bestehend aus 0 und 1) ein.")


# ____________________________________________________________________________________________________________________
# Zahlen-Umwandlung / Konvertierer

# Funktionen zur Umwandlung der Zahlen
def dez_zu_hex(zahl_eingabe):
    # Konvertierung zu hexa durch hex(), [2:] entfernt Präfix 0x in Ausgabe (gegeben durch Funktionen)
    return hex(zahl_eingabe)[2:]

def dez_zu_bin(zahl_eingabe):
    # Konvertierung zu binär durch bin()
    return bin(zahl_eingabe)[2:]

def hex_zu_dez(zahl_eingabe):
    #  Wandelt String in Dezimalzahl um, 16 gibt an, dass Eingabe Hexadez ist
    return int(zahl_eingabe, 16)

def hex_zu_bin(zahl_eingabe):
    # Konvertiert Hexa zuerst in Dezimal, konvertiert dann Dezimalzahl in Binär
    return bin(int(zahl_eingabe, 16))[2:]

def bin_zu_dez(zahl_eingabe):
    # Konvertiert Binär-String in Dezimal, 2 gibt an, dass Eingabe Binär ist
    return int(zahl_eingabe, 2)

def bin_zu_hex(zahl_eingabe):
    # Konvertiert Binärzahl in Dezimal, wandelt Dezimal in Hexa um
    return hex(int(zahl_eingabe, 2))[2:]

# Dictionary für die Umwandlungs-Funktionen
umwandlungs_funktionen = {
    'dez_hex': dez_zu_hex,
    'dez_bin': dez_zu_bin,
    'hex_dez': hex_zu_dez,
    'hex_bin': hex_zu_bin,
    'bin_dez': bin_zu_dez,
    'bin_hex': bin_zu_hex,
}

def konvertierung(umwandlung, zahl):
    while True:
        # Aufruf der richtigen Umwandlungsfunktion basierend auf Auswahl
        if umwandlung in umwandlungs_funktionen:
            ergebnis = umwandlungs_funktionen[umwandlung](zahl)  # passende Funktion wird hier aufgerufen
            print(f"\nDas Ergebnis der Umwandlung ist:\n>>>>> {ergebnis}\n")
            print('____________________________________________________________________________________\n')
            break
        else:
            print("Error. Dumm gelaufen.\nBitte wenden Sie sich an unser Support-Team highly trained monkeys")

# ____________________________________________________________________________________________________________________
# Verhindert Ausführung, wenn Name der Py-Datei nicht main ist
if __name__ == "__main__":
    konvert_wahl()
    zahlen_eingabe()
    konvertierung()