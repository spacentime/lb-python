# define function say hellp that return nothing
def sayHello():
    print('Hello, World!')
    return

def greetMe(name):
    print ('Hello {}'.format(name))
    return

def main(args):    
    sayHello()
    greetMe('Liran')

# this condition is true when running the main comman 
# python app.py 
# it a safeguard from running when the file is being imported by another python file
if __name__ == "__main__":
    main('')