class Greet:    
    defaultText = ""

    def __init__(self):
      self.defaultText = "Bob"      
    
    def greetMe(self, name = None):
      text = ''
      if not name:
         text = self.defaultText
      else:
         text = name

      print ('Hello {}'.format(text))
      return

