# Aufgabe 3: Passwort-Validator
#
# Schreibe eine Funktion namens 'is_valid_password', die:
# - Einen Parameter 'password' (string) entgegennimmt
# - Einen optionalen Parameter 'min_length' mit Standardwert 8 hat
# - True zurückgibt, wenn das Passwort ALLE Bedingungen erfüllt:
#   1. Mindestens 'min_length' Zeichen lang
#   2. Mindestens eine Zahl enthält
#   3. Mindestens einen Großbuchstaben enthält
#   4. Mindestens einen Kleinbuchstaben enthält
# - Sonst False zurückgibt

def is_valid_password(password,min_length=8): 
    if len(password)>=min_length: 
        if any(char.isdigit() for char in password) == True: 
            if any(char.isupper() for char in password) == True: 
                if any(char.islower() for char in password) == True: 
                    return 'Passwort Korregt'
                else: 
                    return 'kein Kleinbuchstabe'
            else: 
                return 'kein Großbuchstabe'
        else: 
            return 'keine Zahl '   
    else: 
        return 'zu kurz'
# Teste mit diesen Passwörtern:
test_passwords = [
     "Hello123",      # Valid
     "hello123",      # Invalid (kein Großbuchstabe)
     "HELLO123",      # Invalid (kein Kleinbuchstabe)
     "HelloWorld",    # Invalid (keine Zahl)
     "Hi1",           # Invalid (zu kurz)
     "SecurePass99"   # Valid
 ]
#
# Beispiel-Aufruf:
for pwd in test_passwords:
     result = is_valid_password(pwd)
     print(f"{pwd}: {result}")
#
# Tipps:
# - Nutze die String-Methoden: .isdigit(), .isupper(), .islower()
# - Du kannst durch jeden Buchstaben im String iterieren
# - Denke an die len()-Funktion für die Länge
