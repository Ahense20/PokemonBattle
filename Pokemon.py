from Move import Move  # Importing the Move class
import random  # For generating random numbers

class Pokemon:
    # Constructor to initialize the Pokemon object with its attributes
    def __init__(self, name, pType, hp, attack, defense, height, weight, moves):
        self.name = name  # Name of the Pokemon
        self.pType = pType  # Type of the Pokemon (e.g., Fire, Water)
        self.hp = hp  # Hit Points (HP) of the Pokemon
        self.attack = attack  # Attack stat of the Pokemon
        self.defense = defense  # Defense stat of the Pokemon
        self.height = height  # Height of the Pokemon
        self.weight = weight  # Weight of the Pokemon
        self.moves = moves  # List of moves the Pokemon can use
        self.used_moves = []  # List of moves that have already been used

    # Method to return the name of the Pokemon (used for team printing)
    def print_pokemon_teams(self):
        return self.name

    # Method to get the attack stat of the Pokemon
    def get_attack(self):
        return self.attack

    # Method to get the defense stat of the Pokemon
    def get_defense(self):
        return self.defense

    # Method to get the type of the Pokemon
    def get_p_type(self):
        return self.pType

    # Method to get the current HP of the Pokemon
    def get_hp(self):
        return self.hp

    # Method to print detailed information about the Pokemon
    def print_pokemon_info(self):
        move_info = "\n".join(self.moves)  # Formatting moves for display
        print(f"{self.name} ({self.pType} type)\nHP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}\nMoves:\n{move_info}")

    # Method to print the moves available to the Pokemon and marking used ones
    def print_moves(self):
        for i, move in enumerate(self.moves, start=1):
            use = "(N/A)" if move in self.used_moves else ""  # Mark used moves as unavailable
            print(f"{i}. {move.get_name()} {use}")

    # Method to select a random move from Team Rocket's Pokemon's available moves
    def random_pokemon_moves(self):
        attack = random.choice([move for move in self.moves if move not in self.used_moves])  # Exclude used moves
        return attack

    # Method to mark a move as used, and reset the list if all moves have been used
    def used_move(self, move):
        if move not in self.used_moves:
            self.used_moves.append(move)
        # Reset used moves if all have been utilized
        if len(self.used_moves) == len(self.moves):
            self.used_moves = []
            print(f"All moves for {self.name} can be used again!")

    # Static method to assign Pokemon to two teams randomly
    @staticmethod
    def assign_pokemon_teams(pokemons):
        team_rocket = random.sample(pokemons, 3)  # Randomly select 3 Pokemon for Team Rocket
        team_player = random.sample([p for p in pokemons if p not in team_rocket], 3)  # Select 3 Pokemon for Team Player
        return team_rocket, team_player