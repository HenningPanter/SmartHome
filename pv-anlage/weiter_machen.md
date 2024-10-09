website aufbauen
in main: wenn glob_var.connected_clients > 0:
    die richtigen Register zyklisch abrufen und in ein Mutex geschütztes dict schreiben

bestehende Websocketverbindung prüfen und schließen, wenn der Klient nicht mehr da ist

in website.py: daten zyklisch verschicken