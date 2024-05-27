#Programming_Assignment_1
import random
import csv

# Load data from CSV files
with open("Pokemon.csv", newline=" ") as f:    
    pokemon_reader = csv.DictReader(f)  
    pokemons = [row for row in pokemon_reader]
with open('PokemonLearnableMoves.csv', newline='') as f:
    moves_reader = csv.DictReader(f)
    moves = [row for row in moves_reader]

with open('TypeChart.csv', newline='') as f:
    type_chart_reader = csv.DictReader(f)
    type_chart = {row['Type']: {t: float(row[t]) for t in type_chart_reader.fieldnames[1:]} for row in type_chart_reader}

with open('AttackTypeMultipliers.csv', newline='') as f:
    attack_type_reader = csv.DictReader(f)
    attack_type_multipliers = {row['DefendingType']: {t: float(row[t]) for t in attack_type_reader.fieldnames[1:]} for row in attack_type_reader}

# Select 2 random pokemons
p1, p2 = random.sample(pokemons, 2)
print(f'{p1["Name"]} vs {p2["Name"]}')

# Select 4 random moves for each pokemon
p1_moves = random.sample([m for m in moves if m['PokemonName'] == p1['Name']], 4)
p2_moves = random.sample([m for m in moves if m['PokemonName'] == p2['Name']], 4)
print(f'{p1["Name"]} moves: {[m["MoveName"] for m in p1_moves]}')
print(f'{p2["Name"]} moves: {[m["MoveName"] for m in p2_moves]}')

# Set up initial battle state
p1_hp = int(p1['HP'])
p2_hp = int(p2['HP'])
p1_status = None
p2_status = None
p1_pp = {m['MoveName']: int(m['PP']) for m in p1_moves}
p2_pp = {m['MoveName']: int(m['PP']) for m in p2_moves}

# Main battle loop
turn = 1
while p1_hp > 0 and p2_hp > 0:
    print(f'Turn {turn}:')
    if int(p1['Spe']) > int(p2['Spe']):
        attacker = p1
        defender = p2
        moveset = p1_moves
        pp = p1_pp
    else:
        attacker = p2
        defender = p1
        moveset = p2_moves
        pp = p2_pp

    # Select move and calculate damage
    move = random.choice(moveset)
    if pp[move['MoveName']] == 0:
        print(f'{attacker["Name"]}: {move["MoveName"]} has no PP left!')
        continue
    pp[move['MoveName']] -= 1
    print(f'{attacker["Name"]} uses {move["MoveName"]}')
    if move['Type'] == 'Status':
        print(f'{move["MoveName"]} has no effect')
        continue
    if random.random() > float(move['Accuracy']) / 100:
        print(f'{move["MoveName"]} missed!')
        continue
    atk_stat = int(attacker['Atk']) if move['Category'] == 'Physical' else int(attacker['SpA'])
    def_stat = int(defender['Def']) if move['Category'] == 'Physical' else int(defender['SpD'])
    base_power = int(move['BasePower'])
    def attack_type():
        type_multiplier = attack_type      
        
        #to create a list of Pokemon with their stats, moves, and types
         #  pokemon_list = [    {"name": "Pikachu", "type": "Electric", "hp": 35, "atk": 55, "def": 30, "moves": ["Thunder Shock", "Quick Attack"]},
    #{"name": "Charizard", "type": "Fire/Flying", "hp": 78, "atk": 84, "def": 78, "moves": ["Flamethrower", "Fly"]}
#]

# Sample code to create a list of trainers with their Pokemon teams
#trainer_list = [    {"name": "Ash Ketchum", "team": [pokemon_list[0], pokemon_list[1]]},
#{"name": "Gary Oak", "team": [pokemon_list[1]]}]
# code to calculate damage based on the attacking and defending Pokemon's stats and moves
#def calculate_damage(attacker, defender, move):
   # effectiveness = 1
#if move.type in defender.type:
      #  effectiveness *= 2 
#if move.type in [t[0] for t in defender.type2]:
    #    effectiveness *= 2
#if move.type in [t[0] for t in defender.type]:
    #    effectiveness *= 0.5
#if move.type in [t[0] for t in defender.type2]:
        #effectiveness *= 0.5
#damage = (2 * attacker.level / 5 + 2) * (attacker.atk) * (move.power / defender.type) / (50 + 2) * effectiveness
#return damage

# code to simulate a battle between two Pokemon
#import random
#def battle(pokemon1, pokemon2):
   # while pokemon1.hp > 0 and pokemon2.hp > 0:
       # move1 = random.choice(pokemon1.moves)
      #  move2 = random.choice(pokemon2.moves)
     #   damage1 = calculate_damage(pokemon1, pokemon2, move1)
       # damage2 = calculate_damage(pokemon2, pokemon1, move2)
      #  pokemon2.hp -= damage1
       # pokemon1.hp -= damage2
    #if pokemon1.hp > 0:
       # return pokemon1
    #else:
       # return pokemon2
# code to simulate a battle between two trainers
#def trainer_battle(trainer1, trainer2):
    #pokemon1 = random.choice(trainer1["team"])
    #pokemon2 = random.choice(trainer2["team"])
   # winner = battle(pokemon1, pokemon2)
   # if winner == pokemon1:
      #  return trainer1
    #else:
     #   return
