import show_team_stats

teams = show_team_stats.team_list
while True:
  print("\nBASKETBALL TEAM STATS TOOL")
  for idx, team in enumerate(teams, 1):
    print(f"{idx}. {team}")

  user_input = input("\nEnter the number of the team you'd like to view (or type 'quit' to exit): ").strip()

  if user_input.lower() == 'quit':
    print("Exiting the program. Goodbye!")
    break

  if user_input.isdigit():
    index = int(user_input) - 1
    if 0 <= index < len(teams):
      selected_team = teams[index]
      show_team_stats.show_team_stats(selected_team)
    else:
      print("Invalid number. Please enter a number from the list.")
  else:
    print("Please enter a valid number or 'quit'.")