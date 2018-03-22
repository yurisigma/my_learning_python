# prompt = "Tell me something, and I will repeat it back to you; "
# prompt += "\n Enter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#
# height = input("How tall are you, in inches? \n Your Height: ")
# height = int(height)
# if height >= 36:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little taller")


# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
#
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even")
# else:
#     print("\nThe number " + str(number) + " is odd")


# sandwich_orders = ['alice', 'pastrami', 'brian', 'pastrami', 'candace', 'pastrami']
# finished_orders = []
#
# print("The Pastrami is sold out")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
#
# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print("I made your " + current_order.title() + " sandwich")
#     finished_orders.append(current_order)
# print("\nThe following sandwich have been made: ")
# for finished_order in finished_orders:
#     print(finished_order.title())

visits = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    place = input("\nIf you could visit one place in the world, where would you go? ")
    visits[name] = place

    choose_active = True
    while choose_active:
        repeat = input("Would you like to let another person respond? (yes/no) ")
        if repeat == 'yes':
            break
        elif repeat == 'no':
            choose_active = False
            polling_active = False
        else:
            print("You have to answer me, 'yes' or 'no'")

print("\n Polling Results")
for name, place in visits.items():
    print(name + " would like to visit " + place + ".")
