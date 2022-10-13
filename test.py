#testing
print ('What do you want on your ice cream? You can have up to two.')
toppings=["whipped cream", "cherry", "sprinkles", "chocolate chips", "sauce"]
x=input()
if x in toppings:
    print("Okay, ice cream with "+x+". Anything else?")
    y=input()
    if y in toppings:
        print("Okay, ice cream with "+x+"and "+y+".")
else: print ("Okay, plain ice cream because we don't have that.")

