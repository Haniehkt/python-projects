size=input("Add the size of pizza S, M or L?")
pepperoni=input("do you want to add pepperoni for small pizza?Y or N?")
pepperoni_larg=("do you want to add pepperoni for medium or large piza?Y or N")
cheese=input("do you want to add cheese for any size ?y or n?")
if size=="s":
    bill=15
    print(f"your pizza is small so you have to pay{bill}")
elif size=="m":
    bill=20
    print(f"your pizza is medium so you have to pay{bill}")
elif size=="l":
    bill=25
    print(f"your pizza is medium so you have to pay{bill}")
if pepperoni=="y":
    bill+=2
elif pepperoni_larg=="y":
    bill+=3
if cheese=="y":
    bill+=1
print(f"your final bill s {bill}")
    
 