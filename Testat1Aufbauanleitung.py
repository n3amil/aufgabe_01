# Aufbauanleitung
import time                                             # Importiere das Modul "Time" um zeitliche Abstände bei der
                                                        # Ausgabe des Codes zu ermöglichen

#Eingabe
user_input = input ( " Wollen Sie mit dem Aufbau der Lampe beginnen? yes/no : " )

if user_input.lower() == "yes":
    print(" ...Starte den Aufbau der Lampe... ")
    time.sleep(1)
    print( "Schraube Mittelstange (1) auf den Sockel")
    time.sleep(1)
    print( "Schraube Mittelstange (2) auf Mittelstange (1)")
    time.sleep(1)
    print( "Befestige das hängende Kabel an der Mittelstange (1) mit der Kabelklemme")
    time.sleep(1)
    print( "Schraube die Gabelung auf Mittelstange (2)")
    time.sleep(1)
    print( "Schraube die Glühbirne in die Birnenhalterung")
    time.sleep(1)
    print( "Schraube Mittelstange (3) auf die Gabelung")
    time.sleep(1)
    print( "Drehe den Schraubendeckel von Mittelstange (3)")
    time.sleep(1)
    print( "Stülpe den Lampenschirm auf die Mittelstange und lege eine Unterlegscheibe auf das obere Gewinde der Mittelstange(3)")
    time.sleep(1)
    print( "Drehe den “Schraubendeckel” wieder auf Mittelstange (3)")
    time.sleep(1)
    print("Befestige den Lampenschirm an den vorgesehenen Haltern")
    print("Fertig ist Ihre neue Lampe!")



elif user_input.lower() == "no":                            # der elif Befehl funktioniert gleich wie der if Befehl,
    print("Schade :(")                                      # jedoch nur, wenn der if Befehl nicht true war.

else:                                                       # Der else Befehl wird ausgeführt, wenn keines von beidem
    print("Wählen Sie aus Yes oder No")                     # erfüllt wurde.





