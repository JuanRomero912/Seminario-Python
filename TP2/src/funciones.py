rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]


def calculate_score(player_stats):
    """Calcula la puntuación del jugador en una ronda."""
    kills = player_stats['kills']
    assists = player_stats['assists']
    deaths = player_stats['deaths']

    return (kills * 3) + (assists * 1) - (1 if deaths else 0)


def calculate_mvp(team):
    """Calcula el MVP de la ronda."""
    player_scores = {}

    for player, stats in team.items():
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


total_team = {}

for round_num, round in enumerate(rounds):
    mvp_player = calculate_mvp(round)
    total_team = update_stats(total_team, round, mvp_player)
    show_round_stats(total_team, mvp_player, round_num + 1)
