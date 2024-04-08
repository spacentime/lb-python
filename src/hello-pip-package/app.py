import os

# using os package to check if file exists 

def checkFileSuffix(fileName):
    fileExt = "py"
    actualExt = fileName.split('.')[-1].lower()
    if actualExt != fileExt:
        print('Expected of type "{}".\nBut "{}" was given.'.format(fileExt, actualExt))
        return False
    else:
        return True    

def checkFile(path = None):    
    if not checkFileSuffix(path):
        return
    
    if not os.path.isfile(path):
        print("{} is not a valid file path!".format(path))    
    else: 
        print('File named "{}" was found'.format(path))
    return

def main(args):    
    checkFile('app.py')
    checkFile('none.py')
    checkFile('app.py1')

# this condition is true when running the main comman 
# python app.py 
# it a safeguard from running when the file is being imported by another python file
if __name__ == "__main__":
    main('')