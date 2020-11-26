from nba_api.stats.endpoints import CommonTeamYears

# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamyears.md
response = CommonTeamYears(league_id="09")

print(response.get_json())