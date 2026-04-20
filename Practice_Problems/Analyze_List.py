# Aufgabe 2: Liste analysieren mit Standardwerten
#
# Schreibe eine Funktion namens 'analyze_numbers', die:
# - Einen Parameter 'numbers' (Liste von Zahlen) entgegennimmt
# - Einen optionalen Parameter 'operation' mit Standardwert "sum" hat
# - Je nach 'operation' unterschiedliche Ergebnisse zurückgibt:
#   * "sum" → Summe aller Zahlen
#   * "avg" → Durchschnitt aller Zahlen
#   * "max" → Größte Zahl
#   * "min" → Kleinste Zahl
# - Bei ungültiger Operation: return None
def analyze_numbers(numbers,operation='sum'): 
    if operation == 'sum': 
        return sum(numbers)
    elif operation == 'avg': 
        return sum(numbers)/len(numbers)
    elif operation == 'max':
        return max(numbers)
    else: 
        return 'error'

# Teste mit dieser Liste:
data = [12, 45, 7, 23, 56, 89, 34]
#
# Beispiel-Aufrufe:
print(analyze_numbers(data))              # Sollte Summe ausgeben
print(analyze_numbers(data, "avg"))       # Sollte Durchschnitt ausgeben
print(analyze_numbers(data, "max"))       # Sollte 89 ausgeben
print(analyze_numbers(data,'test_falsche_eingabe'))     
#
# Bonus: Füge einen Docstring hinzu, der erklärt, was die Funktion macht
