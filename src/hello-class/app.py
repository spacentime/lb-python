from hello import Hello
from greet import Greet

def greetMe(name):
    print ('Hello {}'.format(name))
    return

def main(args):    
    #instantiate a class
    hello = Hello()    
    hello.sayHello()
    g1 = Greet();    
    g1.greetMe()
    g1.greetMe('Liran')


# this condition is true when running the main comman 
# python app.py 
# it a safeguard from running when the file is being imported by another python file
if __name__ == "__main__":
    main('')