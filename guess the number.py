#guess_the_number
import random as r

name = input("kaun khel rha re baba: ")
print(f'''aajao mere bhai {name} aaj ham ek bawaal cheej khelenge pura system hil jaaega to kare shuru?''')
ls=[]
for i in range(0,101):
    ls.append(i)
number=r.randint(0,100)
level=int(input("kitni baar kheloge be :"))
user_input=0
count=1
print("number")
while number!=user_input:
     user_input=int(input("enter a number:"))
     if count<(level+1):
        if user_input<number:
           print("thoda bada socho be")
        count+=1
     elif user_input>number:
        print("thoda aasmaan se neeche aao be")
        count+=1
     else:
        print("zindagi mai jab bada socho tab aana , nikalo ab")
        break
    if count<(level+1):
       print("bhadaai ho kya baat hai bawaal macha diye")
