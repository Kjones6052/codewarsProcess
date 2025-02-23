# This is where I will write the code to solve the problem

def chocolate_split(people, bars):
    # 16 pieces of chocolate per bar
    # A = 20% of people => do not want chocolate
    # B = 10% of people => want chocolate after everyone else had some who wants it
    # C = 5% of people => will take 1 piece always, up to 20 piece if any left
    # D = 65% of people => will have 1 piece of chocolate only
    result = []
    
    return result # helpful tip 1
    # Return array = [0, 1, 2, 3]
    # 0 = number of people who had 1 piece
    # 1 = number of piece left after every has had all they want
    # 2.a = if not enough chocolate add to array "You should buy more chocolate next time"
    # 3.a = suggested number of bars to satisfy number of people in group
    # 2.b = if more than 16 pieces left add to array "That was too much chocolate!"
    # 3.b = suggested number of bars to satisfy groups B, C, and D.
    # if people OR bars are not numbers return "Error. We need numbers."
    # if people = None => return "Nobody here. Skedaddle."


# helpful tip 2
people = 100
bars = 10
print("test 1:", chocolate_split(people, bars)) # Output: [80, 0]
people = 0
bars = 10
print("test 2:", chocolate_split(people, bars)) # Output: "Nobody here. Skedaddle."
people = "blue"
bars = 10
print("test 3:", chocolate_split(people, bars)) # Output: "Error. We need numbers."