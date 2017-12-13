

#My Python Story


def greeting():
    print("Hello.....")
    response=input('Do you want to play?   (yes/no)')
    return response

def second_choice():
    print("Great......")
    response=input('Do you open it?....')
    return response

def haters():
    print("Lame, bye then!")


def opened():
    print('Great')
    print('LIMP NOODLE')
def not_opened():
    print('Your trash')
    print('That is not nice')

x = greeting()
if x=="yes":
    y = second_choice()
    if y=="yes":
        opened()
        
        

else:
    haters()





