alien_color = "red"
if alien_color == "green":
    x = 5
elif alien_color == "yellow":
    x = 10
else:
    x = 15
print("you got " + str(x) + " points")

fruit = ["apple", "bananas", "pears"]
if "apple" in fruit:
    print("you really like apple")


current_users = ["Yuri", "Sigma", "chen", "Li", "Chou"]
new_users = ["YURI", "Chen", "doom", "Tom", "John"]
new_current_users = []
for current_user in current_users:
    print(current_user.lower())
    new_current_users.append(current_user.lower())
print(new_current_users)

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print(new_user + " is used")
    else:
        print(new_user + " is not used")

        current_users.append(new_user.lower())
        print(current_users)
