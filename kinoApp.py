import random

results=[]
while len(results)<12:
    n = random.randrange(1, 80)
    if n not in results:
        results.append(n)
while True:
    try:
        gn=input('How many numbers will you guess? ')
        gn=int(gn)
        if not 13>gn>0:
            print('It\'s in between 1 and 12!')
        else:
            break
    except ValueError:
        print('Enter an integer')
        continue

    
my_guess=[]
while len(my_guess)<gn:
    try:
        g = input('Guess:')
        g = int(g)
        if not 81 > g > 0:
            print('It\'s in between 0 and 80!')
        if g not in my_guess:
            my_guess.append(g)
    except ValueError:
        print('Enter an integer')
        continue
while True:
    try:
        money=input('How much money do you want to pay for this? ')
        money=float(money)
        break
    except ValueError:
        print('Enter a float')
        continue
c=0
for f in my_guess:
    if f in results:
        c+=1
if c>0:
    print('Congratulations!')
    print('You win %1.2f euros' %(c*money))

    
else:
    print('You are a looser!')
    

print('Results: ', results)
