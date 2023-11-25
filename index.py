#this is my python code for a bot and the bot uses the number of words a user input for response
print('/** Welcome to Bukunmi Bot **/')
user_input = input("Please tell me your name? ")
name = len(user_input)
if name <= 5:
    user_resp = input("what a lovely name can you tell me how i may be of help to you today: ")
    if len(user_resp) >= 9:
        print('okay thanks for contacting me i will get back to you as soon as possible')
    else:
        print('okay, be wait operation in progress')
elif name >= 6:
    print("Welcome to BUKUNMI's bot how may i help you ")
    user_input2= input('Please tell me how to help you (A) i need the location of place (B) i need to order a ')
    if user_input2 == "A":
        print(' okay all you need to do now is to go to your google map '
              'and search for the place you want locate thanks ')
    elif user_input2 == "B":
        print('please, hold on, i will be back in a moment')
    else:
        print('404, page error please restart')
else:
    print('404 error')