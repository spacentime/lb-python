class Hello:
    "This is a Hello class"
    defaultText = ""

    def __init__(self):
      self.defaultText = "Hello, World!"
    
    def sayHello(self):        
        print(self.defaultText)
        return        

def doIt():  
    p1 = Hello()  
    p1.sayHello()    
    return
