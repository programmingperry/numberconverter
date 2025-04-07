# Abschlussprojekt Zahlenkonverter Programm Nele McCurrach
# ____________________________________________________________________________________________________________________
# Auswahl, zum Einloggen oder Registrieren
from authentifizierung import *
from beenden import *

def anmeldung():
    while True:
        try:
            anmeldewahl = input('Möchtest du dich\na) mit vorhandenem User Anmelden\nb) einen neuen User registrieren\n>>>>> ').lower()
            if anmeldewahl == 'a':
                # Ausführung der Funktionen aus Authentifizierung zum Einloggen
                db_connect()
                einloggen()
                break
            elif anmeldewahl == 'b':
                # Ausführung der Funktionen aus Authentifizierung zum Registrieren
                db_connect()
                registrieren()
                break
        except KeyboardInterrupt:
            sicherheitsabfrage()


# ____________________________________________________________________________________________________________________
# Verhindert Ausführung, wenn Name der Py-Datei nicht main ist
if __name__ == "__main__":
    anmeldung()