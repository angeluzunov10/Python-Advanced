def team_lineup(*players):
    players_lineup = {}
    text_to_print = ""
    for player in players:
        name, country = player
        if country not in players_lineup:
            players_lineup[country] = []
        players_lineup[country].append(name)

    for country, players in sorted(players_lineup.items(), key=lambda x: (-len(x[1]), x[0])):
        text_to_print += f"{country}:\n"
        for player in players:
            text_to_print += f"  -{player}\n"

    return text_to_print


print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))
