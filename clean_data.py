import copy

def clean_data(players_list):
  players = copy.deepcopy(players_list)
  cleaned_players = []
  for player in players:
    cleaned_player = {
      'name': player['name'],
      'guardians': [g.strip() for g in player['guardians'].split(' and ')],
      'experience': player['experience'].strip().upper() =='YES',
      'height': int(player['height'].split()[0])
    }
    cleaned_players.append(cleaned_player)
  
  return cleaned_players
