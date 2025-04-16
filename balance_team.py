import random

def balance_teams(players, team_names):
  num_teams = len(team_names)

  experienced = [p for p in players if p['experience']]
  inexperienced = [p for p in players if not p['experience']]

  random.shuffle(experienced)
  random.shuffle(inexperienced)

  teams = {name: [] for name in team_names}

  def distribute(players_list):
    for idx, player in enumerate(players_list):
      team_name = team_names[idx % num_teams]
      teams[team_name].append(player)
  
  distribute(experienced)
  distribute(inexperienced)

  return teams
