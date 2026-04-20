# ============================================
# Aufgabe 1: Notenbewertung
# ============================================
# Schreibe ein Programm, das:
# 1. Eine Punktzahl von 0 bis 100 vom Benutzer einliest.
# 2. Je nach Punktzahl eine Note ausgibt:
#    90–100: "Note 1"
#    80–89:  "Note 2"
#    70–79:  "Note 3"
#    60–69:  "Note 4"
#    50–59:  "Note 5"
#    < 50:   "Nicht bestanden"
#
# Hinweise:
# - Verwende if / elif / else.
# - Achte auf die richtigen Bereiche (>= und <=).
# - Beispielausgabe: "Du hast Note 2."

"""
eingabe = input("Punktzahl: ")

try:
    punktzahl = int(eingabe)
except ValueError:
    print("Fehler - bitte eine ganze Zahl eingeben.")
else:
    if punktzahl > 100 or punktzahl < 0:
        print("Fehler - ungültige Eingabe (Punktzahl muss zwischen 0 und 100 liegen).")
    elif punktzahl >= 90:
        print("Note 1")
    elif punktzahl >= 80:
        print("Note 2")
    elif punktzahl >= 70:
        print("Note 3")
    elif punktzahl >= 60:
        print("Note 4")
    elif punktzahl >= 50:
        print("Note 5")
    else:
        print("Nicht bestanden")
"""

# ============================================
# Aufgabe 2: Zahlen von 1 bis N
# ============================================
# Schreibe ein Programm, das:
# 1. Eine ganze Zahl N einliest.
# 2. Alle Zahlen von 1 bis N (inklusive) untereinander ausgibt.
#
# Hinweise:
# - Verwende eine for-Schleife mit range().
# - Beispiel: Bei N = 5 werden 1, 2, 3, 4, 5 ausgegeben.

"""
n = input("Zahl eingeben: ")

try:   
    zahl = int(n)
except ValueError:
    print("Fehler - bitte eine ganze Zahl eingeben.")
else: 
    for i in range(zahl): 
        print(f"Zahl: {i}")
        i=i+1
"""

# ============================================
# Aufgabe 3: Summe von 1 bis N
# ============================================
# Schreibe ein Programm, das:
# 1. Eine ganze Zahl N einliest.
# 2. Die Summe aller Zahlen von 1 bis N berechnet.
# 3. Die Summe ausgibt, z.B.:
#    "Die Summe von 1 bis 5 ist 15."
#
# Hinweise:
# - Verwende eine Schleife und eine Variable summe, die bei 0 startet.
# - Addiere in der Schleife jede Zahl zu summe.
# - Gib das Ergebnis am Ende aus.

"""
n = input("Zahl eingeben: ")

try:   
    zahl = int(n)
except ValueError:
    print("Fehler - bitte eine ganze Zahl eingeben.")
else: 
    summe=0
    for i in range(zahl+1): 
        summe=summe+i
    
    print(f"Summe von 1 bis {zahl} ist {summe}")
"""

# ============================================
# Aufgabe 4: Einfacher Passwortcheck
# ============================================
# Schreibe ein Programm, das:
# 1. Ein geheimes Passwort im Code speichert, z.B. geheim_pw = "python123".
# 2. Den Benutzer nach einem Passwort fragt.
# 3. Solange nachfragt, bis das richtige Passwort eingegeben wurde.
# 4. Bei richtigem Passwort "Zugang erlaubt." ausgibt.
#
# Hinweise:
# - Verwende eine while-Schleife.
# - Vergleiche die Eingabe mit der geheimen Variable.
# - Gib bei falschem Passwort eine Fehlermeldung aus und frage erneut.

password = input("Passwort festlegen: ")
print("\n\n\n")

while True:
    eingabe = input("Passwort eingeben: ")
    if eingabe == password: 
        print("Sie sind eingeloggt!")
        break
    else: 
        print("Falsches Passwort")


