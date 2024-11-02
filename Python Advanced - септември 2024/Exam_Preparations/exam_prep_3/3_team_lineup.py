def team_lineup(*args):
    team_info = {}
    result = ""

    for player, country in args:
        if country not in team_info:
            team_info[country] = []
        team_info[country].append(player)

    sorted_team_info = dict(sorted(team_info.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for (country, players) in sorted_team_info.items():
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
print()
print(team_lineup(

    ("Lionel Messi", "Argentina"),

    ("Neymar", "Brazil"),

    ("Cristiano Ronaldo", "Portugal"),

    ("Harry Kane", "England"),

    ("Kylian Mbappe", "France"),

    ("Raheem Sterling", "England")))
print()
print(team_lineup(

    ("Harry Kane", "England"),

    ("Manuel Neuer", "Germany"),

    ("Raheem Sterling", "England"),

    ("Toni Kroos", "Germany"),

    ("Cristiano Ronaldo", "Portugal"),

    ("Thomas Muller", "Germany"),

    ("Bruno Fernandes", "Portugal"),

    ("Bernardo Silva", "Portugal"),

    ("Harry Maguire", "England")))
