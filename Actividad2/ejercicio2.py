titles = [
    "Speedrun de Super Mario en tiempo récord",
    "Charla sobre desarrollo de videojuegos",
    "Jugando al nuevo FPS del momento con amigos",
    "Música en vivo: improvisaciones al piano"
]

max_word_count = 0
longest_title = ''

for title in titles:
    words = title.split()
    if len(words) > max_word_count:
        max_word_count = len(words)
        longest_title = title

print('El título con más palabras es:', longest_title)

# otra forma de hacerlo
# 
longest_title = max(titles, key=lambda title: len(title.split()))
print('El título con más palabras es:', longest_title)