from calculator import add, subtract, multiply, divide
from calculator_class import Calculator


def testMyCalculaor():
    print('Lets text my calculator')
    myCalculator = Calculator()
    myCalculator.add(4,2, True)
    print('5 - 2 = {}'.format(myCalculator.subtract(5,2)))
    print('5 x 2 = {}'.format(myCalculator.multiply(5,2)))
    print('8 / 2 = {}'.format(myCalculator.divide(8,2)))
    return

def testCalculaorFx():
    print('Lets text calculator functions')
    myCalculator = Calculator()
    print('4 + 2 = {}'.format(add(4,2)))
    print('5 - 2 = {}'.format(subtract(5,2)))
    print('5 x 2 = {}'.format(myCalculator.multiply(5,2)))
    print('8 / 2 = {}'.format(myCalculator.divide(8,2)))
    return

def main(args):        
    testCalculaorFx()
    testMyCalculaor()
    return

# this condition is true when running the main comman 
# python app.py 
# it a safeguard from running when the file is being imported by another python file
if __name__ == "__main__":
    main('')