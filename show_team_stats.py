import balance_team
import clean_data

from constants import TEAMS
from constants import PLAYERS

clean_players = clean_data.clean_data(PLAYERS)
balanced_teams = balance_team.balance_teams(clean_players, TEAMS)
team_list = list(balanced_teams.keys())

def show_team_stats(team_name):
  players = balanced_teams[team_name]
  total_players = len(players)
  experienced = sum(1 for p in players if p['experience'])
  inexperienced = total_players - experienced
  average_height = sum(p['height'] for p in players) / total_players
  guardians = [guardian for p in players for guardian in p['guardians']]

  print(f"\nTeam {team_name} Stats")
  print("-" * 20)
  print(f"Total players: {total_players}")
  print(f"Total experienced: {experienced}")
  print(f"Total inexperienced: {inexperienced}")
  print(f"Average height: {average_height:.1f} inches")
  print("\nPlayers on Team:")
  for p in players:
    print(f"  - {p['name']}")
  print("Guardians:")
  print(", ".join(guardians))
