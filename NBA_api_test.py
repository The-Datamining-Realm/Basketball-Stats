from nba_api.stats.static import teams

response = teams.get_teams()

print(response)