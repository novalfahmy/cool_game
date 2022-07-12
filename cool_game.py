import random
import time
import pandas as pd


def motion(x,y):
    print(x*15)
    time.sleep(y)

while True:
    no_players = input('Input number of player: ')
    try:
        no_players = int(no_players)
        break 
    except ValueError:
        print('Input the right answer')
motion('',0)

player_name = []
for players in range(1, no_players+1):
    all_player = input(f'Player Name {players}: ')
    player_name.append(all_player)
motion('',0)

while True:
    no_round = input('Input number of round: ')
    try:
        no_round = int(no_round)
        break 
    except ValueError:
        print('Input the right answer')
motion('',0)

while True:
    game_type = input('Input game type (Largest or Lowest): ')
    if game_type == 'Largest':
        break 
    elif game_type == 'Lowest':
        break 
    else:
        print('Input the right answer')

player_score = []
def game_round(x):
    motion('',0)
    print(f'Round {x}, Fight!')
    motion('',2)
    for name in player_name:
        rand = random.randint(0,100)
        print(f'Player {name} got {rand}')
        player_score.append({"Name":name, "Score":rand})
        time.sleep(0.5)
    motion('-',0)
    
    
for round in range(1, no_round+1):
    motion('',0)
    readiness = input(f'Are you ready for the round {round} (Yay or Nay)? ')
    if readiness == 'Yay':
        game_round(round)
    else: 
        motion('',1)
        print('Ok good byee ^^')
        break

motion('',1.5)
print('And here is the result...')
motion('',1.5)

df = pd.DataFrame(player_score)
grouped_player = df.groupby(['Name']).sum()

if game_type == 'Largest':
    grouped_player = grouped_player.reset_index().sort_values(by='Score', ascending=False)
else: 
    grouped_player = grouped_player.reset_index().sort_values(by='Score', ascending=True)
summary_dict = grouped_player.to_dict(orient='records')

for summary in summary_dict:
    print(f'{summary["Name"]} got {summary["Score"]} points!')

motion('',1.5)
print(f'Congrats!, {summary_dict[0]["Name"]} is the winner! ^^')