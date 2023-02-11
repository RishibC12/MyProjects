print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? Answer 'yes' or 'no' \n")
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ", name_player)

score = 0

answer = input(' What is CPU stands for? \n ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' Which one is the first fully supported 64-ibt operating system: Windows, Mac, Linux? \n ')
if answer.lower() == 'Linux':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Computer Hard Disk was first introduced in 1956 by: dell, apple, ibm, microsoft? \n ')
if answer.lower() == 'ibm':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is ROM stands for? \n ')
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Mouse is an input device or output device? \n ')
if answer.lower() == 'input device':
    print("Correct")
    score += 1
else:
    print('Wrong')
print('your result is', score)
print(end='score')
