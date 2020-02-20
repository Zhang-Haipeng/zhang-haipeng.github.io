# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import numpy as np

path = '/Users/roc/Documents/02_personal-blog/Zhang-Haipeng.github.io/assets/img/gallery/origin'

# Function to rename multiple files 
def main(): 

    for filename in os.listdir(path):
        if filename[-4:] == '.jpg': # pass other files
            numb = str(np.random.randint(1,100000000000))
            os.rename(path+'/'+filename, path+'/'+numb+'.jpg')
            print(filename,'to',numb+'.jpg')
    
# Driver Code 
if __name__ == '__main__': 
    main() 
