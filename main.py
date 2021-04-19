# asking user name

print("welcome to our super market")

import sys
while True :
 name = input("Enter your name (without initial): ")
 user_name = name.isalpha()
 length = len(name)

 if user_name:
    break
 else:
    print("Name cannot contain numbers enter again.(without initial)")
    continue
if length >= 3:
    pass
else:
    print("your name is lesser than three letters re run and try again.QUITTING..... ")
    sys.exit()



# asking user age

while True:
 age = input("enter your age: ")
 user_age = age.isdigit()
 if user_age:
    break
 else:
    print("Age cannot contain alphabets enter again")
    continue

if user_age<=18:
    pass
else:
    print("You are lesser than 18 so you cant use this application.QUITTTING......")
    sys.exit()

# asking user address
address = input("enter your address: ")
# asking user whether you are a prime member
prime = input("are you a prime member: ")

if prime == "yes":
    pass
elif prime == "no":
    print("you are not a prime member so you will not eligible free delivery")

    # shopping list

print('''### shopping list

apple
orange
table
Meat & Fish
Dairy
Vegetables and fruit
Freezer
Bread & bread spreads
Snacks
Care Products
Greek yogurt
Pasta
cans of chopped tomatoes
can of coconut milk
carton fo almond milk
box of tea
pack of coffee
toys
shampoo
soap
ipad
laptop
tablets
android tab
banana
rice
snacks
keyboard
painting essentials
chocolates
dustbin
bucket
dustbin cover
fruits
tv
monitor
computer



''')
ordered_things = input("select from above items")


# delivery info

print(ordered_things)
print("order details")
print("name: " + name)
print("deliver to: " + address)
print("free delivery: " + prime)
print("your order will be deliverd soon thanks for being with us")




