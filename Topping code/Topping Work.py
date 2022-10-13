#Ice cream menu

def sauce():
    sauces=["fudge", "strawberry", "mango"]
    s=input('What flavor of sauce do you want?')
    if s in sauces:
        print ("Okay, ice cream with "+s+" sauce . Anything else?")
    else:
        print ("Not a sauce option.")
    else:
        print ("We do not have "+s+" sauce. Please select something else.")

def IceCreamToppings():
    topcount=0
    topselect=[]
    toppings_options=["chocolate","sprinkles","whipped cream","cherry","strawberry"]
    while topcount<=2:
        x=input('What do you want on your ice cream? You can have up to two toppings.')

        if x =="sauce":
            sauce()
        elif x in toppings_options:
            print("Okay, ice cream with "+x+". Anything else?")
            topselect.append[x]
            topcount+=1
            y=input()
            if y =="sauce":
                sauce()
            elif y in toppings_options:
                print("Okay, here is your ice cream with "+x+"and "+y+".")
                topcount+=1
            else:
                print("Here is your ice cream with "+x+" because we do not have that.")
                topcount+=1

        else: 
            print ("Plain ice cream because we don't have that.")
            break

IceCreamToppings()


