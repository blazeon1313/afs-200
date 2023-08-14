import random

# Create a class for a die(single dice)
class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        self.currentFaceValue = None

    def roll(self):
        self.currentFaceValue = random.randint(1, self.sides)

    def getCurrentFaceValue(self):
        if self.currentFaceValue == None:
            self.roll()
        return self.currentFaceValue

    def showDieFace(self):
        match self.currentFaceValue:
            case 1:
                return f"⚀ (1)"
            case 2:
                return f"⚁ (2)"
            case 3:
                return f"⚂ (3)"
            case 4:
                return f"⚃ (4)"
            case 5:
                return f"⚄ (5)"
            case 6:
                return f"⚅ (6)"
            
def checkForYahtzee(array):
    if(array[0].getCurrentFaceValue() == array[1].getCurrentFaceValue() ==
    array[2].getCurrentFaceValue() == array[3].getCurrentFaceValue() == array[4].getCurrentFaceValue()):
        return True


def roll_five():
    joined_die = []
    listOfDice = [Die(), Die(), Die(), Die(), Die()]
    
    for die in listOfDice:
        die.roll()
        joined_die.append(die.showDieFace())
    print(" ".join(joined_die))

    if(checkForYahtzee(listOfDice)):
        print("YAHTZEE")
    

roll_five()