# Abschlussprojekt Zahlenkonverter Programm Nele McCurrach
# ____________________________________________________________________________________________________________________
# Funktionen zum Einlog- und Registrierungsvorgang
import mysql.connector # Bibliothek um mit mySQl zu arbeiten
import string

# ____________________________________________________________________________________________________________________
# Connection zur Datenbank
def db_connect():
    return mysql.connector.connect(
        host="localhost", # IP Adresse (vorerst) der lokalen Datenbank 
        user="root", # Angelegter Username
        password="", # Passwort für Username
        database="zahlenkonverter" # Datenbankname 
    )

#print(db_connect())

# ____________________________________________________________________________________________________________________
# Funktion zum Einloggen bei vorhandenem Nutzer
def einloggen():
    conn = db_connect()
    cursor = conn.cursor()
    while True:
        username = input('Username: ')
        passwort = input('Passwort: ')

        # Passwort direkt abfragen
        cursor.execute("SELECT password FROM usersneu WHERE username = %s", (username,))
        result = cursor.fetchone()

        # Überprüfen, ob Benutzername und Passwort übereinstimmen
        if result and result[0] == passwort:
            print('\nEinloggen erfolgreich.\nDu besitzt nun das unglaubliche Previleg, Zahlen umzurechnen.\n')
            break
        else:
            print('Benutzername oder Passwort falsch.')
    cursor.close()
    conn.close()

# ____________________________________________________________________________________________________________________
# Funktion zum Anlegen eines neuen Nutzers
def registrieren():
    conn = db_connect()
    cursor = conn.cursor()
    # Benutzername erstellen und direkt prüfen
    while True:
        while True:
            username = input('Usernamen erstellen: ')

            # Prüfen, ob der Benutzername bereits existiert
            cursor.execute("SELECT username FROM usersneu WHERE username = %s", (username,))
            if cursor.fetchone():
                print("Dieser Username ist bereits vergeben. Bitte wähle einen anderen.")
            else:
                break  # Benutzername ist verfügbar

        while True:
            passwort = input('Passwort erstellen: ')
            # Passwort-Kriterien prüfen
            if len(passwort) >= 8 and any(char.isdigit() for char in passwort) and any(
                    char in string.punctuation for char in passwort):
                while True:
                    passwort2 = input('Passwort bestätigen: ')  # Zweite Eingabe für Bestätigung

                    if passwort == passwort2:
                        break  # Passwörter stimmen überein, Schleife verlassen
                    else:
                        print("Passwörter stimmen nicht überein.")
                        repeat_choice = input("Möchtest du das erste Passwort erneut eingeben? (j/n): ").lower()
                        if repeat_choice == 'j':
                            break  # Zurück zur ersten Passwort Eingabe
                        elif repeat_choice == 'n':
                            continue  # Nur zweite Eingabe wiederholen
                        else:
                            print("Ungültige Eingabe. Bitte erneut versuchen.")
                if passwort == passwort2:
                    break  # Hauptschleife verlassen
            else:
                print(
                    'Kein gültiges Passwort. Passwort muss mind. 8 Zeichen lang sein, eine Zahl und ein Sonderzeichen enthalten.')

        try:
            # Benutzername und Passwort direkt speichern
            cursor.execute("INSERT INTO usersneu (username, password) VALUES (%s, %s)", (username, passwort))
            conn.commit()
            print("Registrierung erfolgreich.\n")
            break
        except mysql.connector.IntegrityError:
            print("Dieser Username ist bereits vergeben.")
    cursor.close()
    conn.close()

# ____________________________________________________________________________________________________________________
# Verhindert Ausführung, wenn Name der Py-Datei nicht main ist
if __name__ == "__main__":
    db_connect()
    einloggen()
    registrieren()
