rules = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

key_word = input('Ingrese una palabra clave: ').lower().strip()

# Dividir las reglas en líneas
rules_list = rules.split("\n")

for rule in rules_list:
    # Comprobar si la palabra clave está en la regla
    if key_word in rule.lower():
        print(rule)
