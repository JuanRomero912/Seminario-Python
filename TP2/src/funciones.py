
def calculate_score(player_stats):
    """Calcula la puntuación del jugador en una ronda."""
    kills = player_stats['kills']
    assists = player_stats['assists']
    deaths = player_stats['deaths']

    return (kills * 3) + (assists * 1) - (1 if deaths else 0)


def calculate_mvp(round):
    """Calcula el MVP de la ronda."""
    player_scores = {}

    for player, stats in round.items():
        player_scores[player] = calculate_score(stats)

    mvp = max(player_scores, key=player_scores.get)

    return mvp


def update_stats(team, round, mvp):
    """Actualiza las estadísticas tras cada ronda, la primer ronda inicializa todas las estadísticas."""
    
    # Iterar sobre los jugadores y sus estadísticas en la ronda
    for player, stats in round.items():
        
        # Si el jugador ya existe en el equipo, actualizamos sus estadísticas
        if player in team:
            team[player]['kills'] += stats['kills']
            team[player]['assists'] += stats['assists']
            team[player]['deaths'] += 1 if stats['deaths'] else 0
            team[player]['score'] += calculate_score(stats)
        else:
            # Si el jugador no existe en el equipo, lo inicializamos con sus estadísticas
            team[player] = {
                'kills': stats['kills'],
                'assists': stats['assists'],
                'deaths': 1 if stats['deaths'] else 0,
                'score': calculate_score(stats),
                'mvps': 0
            }

    team[mvp]["mvps"] += 1

    return team


def show_round_stats(team, mvp, round):
    """Muestra las estadísticas de la ronda ordenadas por puntuación."""
    print("Ronda ", round, ":")
    print("Jugador  Kills  Asistencias  Muertes  MVPs  Puntos")
    print("--------------------------------------------------------")

    # Ordenar al equipo por puntos
    sorted_team = sorted(team.items(), key=lambda x: x[1]['score'], reverse=True)

    for player, stats in sorted_team:
        print(f"{player:<10} {stats['kills']:<6} {stats['assists']:<12} {stats['deaths']:<8} {stats['mvps']:<5} {stats['score']}")

    print("MVP de la ronda: ", mvp)
    print("--------------------------------------------------------")

