# Import necessary libraries
import csv  # To read and write CSV files
import ast  # To parse strings of lists into Python lists
from Pokemon import Pokemon  # Importing the Pokemon class
from Move import Move  # Importing the Move class
import random  # For generating random numbers
import time  # For adding delays to enhance user experience

# Dictionary that defines type effectiveness in battle
type_effectiveness = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Others": 1},
    "Fire": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1, "Grass": 2, "Others": 1},
    "Water": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 1, "Grass": 0.5, "Others": 1},
    "Electric": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0.5, "Grass": 0.5, "Others": 1},
    "Grass": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Others": 1},
    "Others": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Others": 1},
}

# Function that calculates damage during a battle
def damage_calculations(pokemon_a, pokemon_b, chosen_move):
    # Checks for same-type attack bonus (STAB)
    if chosen_move.get_m_type() == pokemon_a.get_p_type():
        stab = 1.5
    else:
        stab = 1
    # Determines type matchup multiplier
    tm = type_matchup(chosen_move.get_m_type(), pokemon_b.get_p_type())
    # Extracts attack and defense stats of the involved Pokemon
    attack = pokemon_a.get_attack()
    defense = pokemon_b.get_defense()
    # Generates a random damage multiplier for variability
    random_number = random.uniform(0.5, 1)
    # Calculates final damage
    damage = chosen_move.get_power() * (attack / defense) * stab * tm * random_number
    return damage

# Helper function to get type effectiveness multiplier
def type_matchup(move_type, defender_type):
    # Retrieves the effectiveness of a move type against a defender's type
    return type_effectiveness.get(move_type, {}).get(defender_type, 1)

# Main function to run the Pokemon battle
def main():
    # File paths for Pokemon and move data
    pokemon_filename = 'pokemon-data.csv'
    moves_filename = 'moves-data.csv'
    pokemons = []  # List to store all Pokemon objects
    moves = []  # List to store all Move objects
    team_rocket = []  # List to store Team Rocket's Pokemon
    team_player = []  # List to store Player's Pokemon
    counter1 = 0  # Counter for Team Rocket's Pokemon fainted
    counter2 = 0  # Counter for Player's Pokemon fainted
    rhp = 0  # Placeholder for Team Rocket's Pokemon HP
    php = 0  # Placeholder for Player's Pokemon HP

    print("Welcome to Pokemon Colosseum!\n")
    pName = input("Enter Player Name: ")
    time.sleep(0.5)  # Delays for smoother gameplay

    # Reads in move data from the CSV file
    with open(moves_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Skips the header row
        for row in reader:
            move = Move(
                name=row[0], mType=row[1], category=row[2], contest=row[3],
                pp=int(row[4]), power=int(row[5]), accuracy=row[6]
            )
            moves.append(move)  # Appends the Move object to the list

    # Reads in Pokemon data from the CSV file
    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)  # Skip the header row
        for row in reader:
            # Parses and validates moves for each Pokemon
            parsed_moves = [
                next((move for move in moves if move.get_name() == move_name), None)
                for move_name in ast.literal_eval(row[7])
            ]
            parsed_moves = [move for move in parsed_moves if move is not None]
            # Creates and appends a Pokemon object to the list
            pokemon = Pokemon(
                name=row[0], pType=row[1], hp=int(row[2]), attack=int(row[3]), defense=int(row[4]),
                height=int(row[5]), weight=int(row[6]), moves=parsed_moves
            )
            pokemons.append(pokemon)

    # Assigns both teams 3 random Pokemon
    team_rocket, team_player = Pokemon.assign_pokemon_teams(pokemons)
    # Display initial teams
    print("Team Rocket enters with", ", ".join([p.print_pokemon_teams() for p in team_rocket]))
    print(f"Team {pName} enters with", ", ".join([p.print_pokemon_teams() for p in team_player]))
    time.sleep(1.5)

    # Random coin toss to decide the starting team
    coin_toss = random.choice(["Team Rocket", "Team Player"])
    if coin_toss == "Team Rocket":
        print("\nCoin toss goes to ----- Team Rocket to start the attack!")
        current = "Team Rocket"
    else:
        print(f"\nCoin toss goes to ----- Team {pName} to start the attack!\n")
        current = "Team Player"
    time.sleep(2.5)

    # Main battle loop
    while team_rocket and team_player:
        if current == "Team Rocket":
            # Logic for Team Rocket's turn
            r_pokemon = team_rocket.pop(0)
            p_pokemon = team_player.pop(0)
            random_attack = r_pokemon.random_pokemon_moves()  # Selects a random move
            print(f"Team Rocket's {r_pokemon.print_pokemon_teams()} cast '{random_attack.get_name()}' to {p_pokemon.print_pokemon_teams()}")
            time.sleep(1.0)
            damage_taken = int(damage_calculations(p_pokemon, r_pokemon, random_attack))
            print(f"Damage to {p_pokemon.print_pokemon_teams()} is {damage_taken} points.")
            time.sleep(1.0)
            p_pokemon.hp -= damage_taken  # Update player's Pokemon HP
            if p_pokemon.hp <= 0:
                print(f"Now {r_pokemon.print_pokemon_teams()} has {r_pokemon.hp} HP, and {p_pokemon.print_pokemon_teams()} faints back to the poke ball.\n")
                time.sleep(1.0)
                team_player.append(p_pokemon)  # Adds Pokemon back to player's list
                counter2 += 1  # Increments fainted Pokemon counter
                if counter2 == 3:
                    print(f"All of Team {pName}'s Pokemon fainted, and Team Rocket prevails!")
                    time.sleep(1.0)
                    break
                team_rocket.insert(0, r_pokemon)  # Reinserts Pokemon into Team Rocket
                current = "Team Player"  # Switch turn to player
            else:
                # Displays HP status after attack
                print(f"Now {p_pokemon.print_pokemon_teams()} has {p_pokemon.hp} HP, and {r_pokemon.print_pokemon_teams()} has {r_pokemon.hp} HP.\n")
                time.sleep(1.0)
                r_pokemon.used_move(random_attack)  # Marks the move as used
                team_rocket.insert(0, r_pokemon)
                team_player.insert(0, p_pokemon)
                current = "Team Player"

        elif current == "Team Player":
            # Logic for Player's turn
            r_pokemon = team_rocket.pop(0)
            p_pokemon = team_player.pop(0)
            print(f"Choose the move for {p_pokemon.print_pokemon_teams()}:")
            Pokemon.print_moves(p_pokemon)  # Displays player's available moves
            print("\n")
            time.sleep(1.0)
            choice = input(f"Team {pName}'s choice: ")

            moveList = p_pokemon.moves  # Retrieves player's Pokemon moves
            # Checks if player made a valid selection
            if choice.isdigit() and 1 <= int(choice) <= len(moveList):
                selected_move = moveList[int(choice) - 1]

                if selected_move in p_pokemon.used_moves:
                    # Notifys if the move has already been used
                    print(f"{selected_move.get_name()} has already been used! Please choose an available move!")
                    time.sleep(1.0)
                    team_rocket.insert(0, r_pokemon)
                    team_player.insert(0, p_pokemon)
                else:
                    # Executes selected move
                    print(f"{p_pokemon.print_pokemon_teams()} used '{selected_move.get_name()}' on {r_pokemon.print_pokemon_teams()}")
                    time.sleep(1.0)
                    damage_taken = int(damage_calculations(p_pokemon, r_pokemon, selected_move))
                    print(f"Damage to {r_pokemon.print_pokemon_teams()} is {damage_taken} points.")
                    time.sleep(1.0)
                    r_pokemon.hp -= damage_taken  # Updates Team Rocket's Pokemon HP

                    if r_pokemon.hp <= 0:
                        # Handles Pokemon fainting
                        print(f"Now {r_pokemon.print_pokemon_teams()} faints back to the poke ball, and {p_pokemon.print_pokemon_teams()} has {p_pokemon.hp} HP\n")
                        time.sleep(1.0)
                        team_rocket.append(r_pokemon)  # Adds Pokemon back to Team Rocket's list
                        counter1 += 1   # Increments fainted Pokemon counter
                        p_pokemon.used_move(selected_move)  # Marks the move as used
                        team_player.insert(0, p_pokemon)
                        if counter1 == 3:
                            print(f"All of Team Rocket's Pokemon fainted, and Team {pName} prevails!")
                            break
                        current = "Team Rocket"  # Switch turn to Team Rocket
                    else:
                        # Displays HP status after attack
                        print(f"Now {p_pokemon.print_pokemon_teams()} has {p_pokemon.hp} HP, and {r_pokemon.print_pokemon_teams()} has {r_pokemon.hp} HP.\n")
                        time.sleep(1.0)
                        p_pokemon.used_move(selected_move)  # Marks the move as used
                        team_rocket.insert(0, r_pokemon)
                        team_player.insert(0, p_pokemon)
                        current = "Team Rocket"  # Switch turn to Team Rocket
            # Tells player they have made an invalid choice
            else:
                print("Invalid choice. Please try again.")
                team_rocket.insert(0, r_pokemon)
                team_player.insert(0, p_pokemon)

# Entry point for the program
if __name__ == "__main__":
    main()
