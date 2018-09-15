import random
from tkinter import*

#yields
y1={0 : 0, 1 : 2.5}
y2={0 : 0, 1 : 1, 2 : 5}
y3={0 : 0, 1 : 0, 2: 2.5, 3 : 25}
y4={0 : 0, 1 : 0, 2: 1, 3 : 4, 4 : 100}
y5={0 : 0, 1 : 0, 2: 0, 3 : 2, 4 : 20, 5 : 450}
y6={0 : 0, 1 : 0, 2: 0, 3 : 1, 4 : 7, 5 : 50, 6 : 1600}
y7={0 : 0, 1 : 0, 2: 0, 3 : 1, 4 : 3, 5 : 20, 6 : 100, 7 : 5000}
y8={0 : 0, 1 : 0, 2: 0, 3 : 0, 4 : 2, 5 : 10, 6 : 50, 7 : 1000, 8 : 15000}
y9={0 : 0, 1 : 0, 2: 0, 3 : 0, 4 : 1, 5 : 5, 6 : 25, 7 : 200, 8 : 4000, 9 : 40000}
y10={0 : 2, 1 : 0, 2: 0, 3 : 0, 4 : 0, 5 : 2, 6 : 20, 7 : 80, 8 : 500, 9 : 10000, 10 : 100000}
y11={0 : 2, 1 : 0, 2: 0, 3 : 0, 4 : 0, 5 : 1, 6 : 10, 7 : 50, 8 : 250, 9 : 1500, 10 : 15000, 11 : 500000}
y12={0 : 4, 1 : 0, 2: 0, 3 : 0, 4 : 0, 5 : 0, 6 : 5, 7 : 25, 8 : 150, 9 : 1000, 10 : 2500, 11 : 25000, 12 : 1000000}
y1
results=[]
while len(results)<12:
    n = random.randrange(1, 80)
    if n not in results:
        results.append(n)
res=Tk()
res.geometry("600x460")
res.title("Results")
resLabel0=Label(res, text="Results \n", font=("Comic Sans", 30,'bold'))
resLabel=Label(res, text=" ".join(str(e) for e in results), font=("Comic Sans", 18,'bold'))
resLabel0.pack(side=TOP)
resLabel.pack(side=TOP)
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

current_yield=eval('y'+str(gn))
for k, v in current_yield.items():
    print(k,v)
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
win_money=current_yield.get(c)*money
if win_money>0:
    print('Congratulations!')
    print('You win %1.2f euros' %win_money)

    
else:
    print('You are a looser!')
    
print('Results: ', results)

                   
                   
