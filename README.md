# Project 1 - Pokemon Colosseum

This is the first project in COP 430 - Intro to Artificial Intelligence. It is a text based Pokemon battle simulator that's between the player and Team Rocket. Teams are generated with three random Pokemon where the player chooses their moves to win the battle. 



## Features

- Turn-based Battles: This has turn based comabt features where the player and Team Rocket have alternating attacks.

- Dynamic Damage Calculation: Includes mechanics such as STAB (Same Type Attack Bonus) and type effectiveness.

- Team Assignment: Teams are randomly assigned 3 Pokémon each from the dataset.

- Move Reusability: Pokémon moves can be used once per cycle before resetting for reuse.

- Interactive Gameplay: Player has the ability to select moves for their Pokemon and can strategize based on type advantage.


## File Structure

- Pokemon.Colosseum.py: Main gameplay script.

- Move.py: Defines the Move class for Pokémon moves.

- Pokemon.py: Defines the Pokemon class for Pokémon attributes and behavior.


## Data Files

- pokemon-data.csv: Contains Pokémon details, such as stats and available moves.
- moves-data.csv: Contains move details, including type, power, and accuracy.
  
## Setup Instructions 
    1) Download the files
    Ensure you have the following files saved locally in the same directory:
    -PokemonColosseum.py (the main script provided above)
    -Move.py (contains the Move class definition
    -Pokemon.py (contains the Pokemon class definition
    -pokemon-data.csv (contains Pokémon data)
    -moves-data.csv (contains move data)

    2) Ensure You Have Python Installed
    Check if Python is installed on your system by running the command:
            python --version
    If you do not have Python installed, you can download the latest version off of https://www.python.org/.
    
    3) Run the Script in Command Prompt
    Navigate to the directory where your files are located:
    cd /path/to/your/files
    Execute the game:
            python PokemonColosseum.python

    4) Enter Team Name
    After running the command you will enter your team name, then the battle will start!

## Gameplay Mechanics
Damage Formula: 

damage = chosen_move.get_power() * (attack / defense) * stab * tm * random_number

- STAB: 1.5 if move type matches Pokémon type, otherwise 1.
- Type Matchup (tm): Multiplier based on type matchups (e.g., Fire is strong against Grass).
- Random Modifier: Random value between 0.5 and 1 for variability.

Type Matchups:
Effectiveness is determined using the type_effectiveness dictionary. Example:

type_effectiveness = {
    "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Others": 1},
...
}
