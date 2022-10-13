#Ice cream menu

def sauce():
    sauces=["fudge, strawberry, mango"]
    s=input('What flavor of sauce do you want?')
    if s in sauces:
        print ("Okay, ice cream with "+s+" sauce . Anything else?")
        topcount+=1
    else:
        print ("We do not have "+s+" sauce. Please select something else.")

def IceCreamToppings():
    topcount=0
    while topcount<=2:
        x=input('What do you want on your ice cream? You can have up to two toppings.')
        if x =="sauce":
            sauce()
        elif x in toppings:
            print("Okay, ice cream with "+x+". Anything else?")
            topcount+=1
            y=input()
            if y =="sauce":
                sauce()
            elif y in toppings:
                print("Okay, here is your ice cream with "+x+"and "+y+".")
                topcount+=1
            else: print("Here is your ice cream with x because we do not have that.")
        else: 
            print ("Plain ice cream because we don't have that.")
            break

IceCreamToppings()

