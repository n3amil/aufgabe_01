print('Aufgabe 3 - Kinobesucht \n')
# -------------------------
# Aufgabe 3 - Kinobesucht
# Hier wird der User aufgefordert, als Eingabeparameter sein Alter anzugeben.
alter = input("Bitte geben Sie ihr Alter an: ")

# Ist das Alter größer gleich 12, darf der User den Film anschauen.
# Hierbei wird die Variable "alter" in einen Integer umgewandelt, da der Eingabeparameter als String abgespeichert wurde
if int(alter) >= 12:
    print("Ihr alter ist " + alter + ". " + "Sie dürfen das Kino betreten und eine 2:22 Stunden an dauernde Romanze "
                                            "betrachten. Herzlichen Glückwunsch.")

# Ist der User andernfalls 11 Jahre oder jünger, darf der User den Film nicht anschauen.
else:
    print("Ihr alter ist " + alter + ". " + "Au, wie schade. Ihnen bleibt leider der Zutritt verwehrt.")

print('Aufgabe 4 - Spaß mit Zahlen \n')
# -------------------------
# Aufgabe 4 - Spaß mit Zahlen
# Eingabe
eingabe1 = input(" Bitte geben Sie eine Zahl ein : ")
# Umwandlung in Integer
eingabe_zahl = int(eingabe1)
# Prüfung für korrekt Eingabe
if eingabe_zahl < 0:
    exit("keine gültige Eingabe")
for i in range(0, eingabe_zahl + 1, 1):
    # prüfe gerade Zahl
    if i % 2 == 0:
        # Ausgabe i
        print(i)
# Variable i zurück auf 0 setzen
i = 0
while i <= eingabe_zahl:
    # prüfe gerade Zahl
    if i % 2 == 0:
        # Ausgabe i
        print(i)
    # Variable i hochzählen
    i = i + 1


print('Aufgabe 5 - Aufbauanleitung - Lösung 1 \n')
# -------------------------
# Aufgabe 5 - Aufbauanleitung - Lösung 1
# Aufbauanleitung
# Importiere das Modul "Time" um zeitliche Abstände bei der Ausgabe des Codes zu ermöglichen
import time

# Eingabe
user_input = input(" Wollen Sie mit dem Aufbau der Lampe beginnen? yes/no : ")

if user_input.lower() == "yes":
    print(" ...Starte den Aufbau der Lampe... ")
    time.sleep(1)
    print("Schraube Mittelstange (1) auf den Sockel")
    time.sleep(1)
    print("Schraube Mittelstange (2) auf Mittelstange (1)")
    time.sleep(1)
    print("Befestige das hängende Kabel an der Mittelstange (1) mit der Kabelklemme")
    time.sleep(1)
    print("Schraube die Gabelung auf Mittelstange (2)")
    time.sleep(1)
    print("Schraube die Glühbirne in die Birnenhalterung")
    time.sleep(1)
    print("Schraube Mittelstange (3) auf die Gabelung")
    time.sleep(1)
    print("Drehe den Schraubendeckel von Mittelstange (3)")
    time.sleep(1)
    print(
        "Stülpe den Lampenschirm auf die Mittelstange und lege eine Unterlegscheibe auf das obere Gewinde der Mittelstange(3)")
    time.sleep(1)
    print("Drehe den “Schraubendeckel” wieder auf Mittelstange (3)")
    time.sleep(1)
    print("Befestige den Lampenschirm an den vorgesehenen Haltern")
    print("Fertig ist Ihre neue Lampe!")


# der elif Befehl funktioniert gleich wie der if Befehl jedoch nur, wenn der if Befehl nicht true war.
elif user_input.lower() == "no":
    print("Schade :(")
# Der else Befehl wird ausgeführt, wenn keines von beidem erfüllt wurde.
else:
    print("Wählen Sie aus Yes oder No")

print('Aufgabe 5 - Aufbauanleitung - Lösung 2 \n')
# -------------------------
# Aufgabe 5 - Aufbauanleitung - Lösung 2
def ikea():
    print('Bitte Mittelstange (1) auf Sockel schrauben und Mittelstangen (1) mit Mittelstange (2) verschrauben')
    user_input_1 = input('Mittelstange (1) und (2) verschraubt? (ja/nein) ')
    if user_input_1 == "ja":
        print('Bitte Kabelklemme anbringen und Gabelung auf Fassung von Mittelstange (2) schrauben')
        user_input_2 = input('Kabelklemme und Gabelung verschraubt? (ja/nein) ')
        if user_input_2 == "ja":
            print('Bitte Mittelstange(3) mit Gabelung verschrauben und Schraubendeckel abschrauben')
            user_input_3 = input('Mittelstange(3) verschraubt und Schraubendeckel abgeschraubt? (ja/nein) ')
            if user_input_3 == "ja":
                print('Bitte Lampenschirm auf Mittelstange(3) aufstecken, mit Schraubendeckel fixieren und nach unten '
                      'spannen')
                user_input_4 = input('Lampenschirm auf Mittelstange (3) angebracht, fixiert mit Schraubendeckel und '
                                     'gespannt? (ja/nein) ')
                if user_input_4 == "ja":
                    print(
                        'Sie haben die Lampe korrekt aufgebaut!')
                else:
                    ikea()
            else:
                ikea()
        else:
            ikea()
    else:
        ikea()


ikea()
