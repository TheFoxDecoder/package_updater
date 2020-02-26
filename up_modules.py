
import io
import pip
from subprocess import call
name = input("Enter name you ant update platform name: ")

def up_check():     
    if name == 'pip' or 'pip3' :
        call("pip freeze > requirements.txt",shell=True) # creating req file
        call('pip install -upgrade pip',shell=True)       
        if name == 'pip3':
            call('pip3 install -r requirements.txt', shell=True) #using requriments.txt
            #call("pip3 install -U $(pip freeze | awk '{split($0, a, \"==\"); print a[1]}')", shell=True)
            print("pip3 is  done")
        else:
            call("pip install -r requirements.txt", shell=True) #using requriments.txt
            #call("pip install -U $(pip freeze | awk '{split($0, a, \"==\"); print a[1]}')", shell=True)
            print('pip is done\n USE PIP3 its better')    
    elif name == 'conda' or 'anaconda':
        env = input("Enter Env Name: ")
        call('conda update -n {0} --all'.format(env),shell=True)
        print('conda is D O N E baby!!')
    else :
        print("IDK what the fuck you talking about \n Enter again!!")

try:
    while True:
        up_check()
except KeyboardInterrupt:
    print('Boy did you just Interrupt Keyboard\nNow you fucked up!')
    
