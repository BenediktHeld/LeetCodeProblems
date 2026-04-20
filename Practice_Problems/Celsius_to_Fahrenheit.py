# Aufgabe 1: Temperatur-Konverter
#
# Schreibe eine Funktion namens 'celsius_to_fahrenheit', die:
# - Einen Parameter 'celsius' (float oder int) entgegennimmt
# - Die Temperatur in Fahrenheit umrechnet (Formel: F = C * 9/5 + 32)
# - Das Ergebnis zurückgibt (return)
def celsius_to_fahrenheit(celsius): 
    fahrenheit = celsius*9/5+32
    return fahrenheit
#
# Teste deine Funktion mit folgenden Werten:
# - 0°C sollte 32°F ergeben
# - 100°C sollte 212°F ergeben
# - 37°C sollte 98.6°F ergeben
print(celsius_to_fahrenheit(25))

# Beispiel-Aufruf:
# result = celsius_to_fahrenheit(25)
# print(f"25°C = {result}°F")
#
# Erwartete Ausgabe:
# 25°C = 77.0°F
