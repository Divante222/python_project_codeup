import os
import subprocess

# with open([filename]), w) as f
with open('new_file.txt', 'w') as f:
    f.write('hello pagel')



#mulitple lines use a variable with \n
with open('new_file.txt', 'w') as f:
    f.write('hello pagel\n'
            'my name is divante')
    


#can do it in a list too
the_list = ['hello\n', 'pagle\n','divante\n']

with open('new_file.txt', 'w') as f:
    f.writelines(the_list)

with open('new_file.txt', 'r') as f:
    data = f.readlines() ##returns a list line by line
    

    print(data)
    
    
print(os.path.exists('new_file.txt')) ## does this filepath exist is whats its checking

# can use this in an f statement to see if the file exists if it doesn't you can create it

# subprocess.run('code', 'new_file.txt')opens the code in vs code


os.remove('new_file.txt') ### deletes files
