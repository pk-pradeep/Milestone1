l=[0,1,2]
def show(l):
    print('this is the list : [__,__,__]')

def loc():
    position='non'
    while position not in ['0','1','2']:
        position=input("Enter your pick for location: ")
        if position not in ['0','1','2']:
            print("Sorry! try again [0,1,2]")
    return int(position)

def user_value(l,position):
    value=input("Enter your new value: ")
    l[poision]=value
    return l

def gameon():
    choice='non'
    while choice not in ['Y','N']:
        choice=input("Wanna play more ('Y','N'): ")
        if choice not in ['Y','N']:
            print("Sorry! you've entered wrong option.")
            print("Please enter valid option ('Y','N')")
    if choice.lower()=='y':
        return True
    else:
        print(f'Your final list: {l}')
        return False

game=True
while game:
    show(l)
    poision=loc()
    l=user_value(l,poision)
    print(f'You list: {l}')
    game=gameon()
