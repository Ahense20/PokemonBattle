class Move:
    # Constructor to initialize the Move object with its attributes
    def __init__(self, name, mType, category, contest, pp, power, accuracy):
        self.name = name  # Name of the move
        self.mType = mType  # Type of the move (e.g., Fire, Water)
        self.category = category  # Category of the move (e.g., Physical, Special)
        self.contest = contest  # Contest category for the move
        self.pp = pp  # Power Points (PP) of the move
        self.power = power  # Power of the move
        self.accuracy = accuracy  # Accuracy of the move

    # Method to get the power of the move
    def get_power(self):
        return self.power

    # Method to get the type of the move
    def get_m_type(self):
        return self.mType

    # Method to get the name of the move
    def get_name(self):
        return self.name

    # Method to get the accuracy of the move
    def get_accuracy(self):
        return self.accuracy

    # Method to print the details of the move
    def print_moves(self):
        print(f"Move: {self.name}, Type: {self.mType}, Category: {self.category}, Contest: {self.contest}, PP: {self.pp}, Power: {self.power}, Accuracy: {self.accuracy}")