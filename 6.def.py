def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# sandwich_orders = ['alice', 'pastrami', 'brian', 'pastrami', 'candace', 'pastrami']
# finished_orders = []
# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print("I made your " + current_order.title() + " sandwich")
#     finished_orders.append(current_order)
# print("\nThe following sandwich have been made: ")
# for finished_order in finished_orders:
#     print(finished_order.title())


def print_orders(sandwich, finished):
    while sandwich:
        current_order = sandwich.pop()
        print("I made your " + current_order.title() + " sandwich")
        finished.append(current_order)


def show(finished):
    print("\nThe following sandwich have been made: ")
    for finish in finished:
        print(finish)


# sandwich_orders = ['alice', 'pastrami', 'brian', 'pastrami', 'candace', 'pastrami']
# finished_orders = []
# print_orders(sandwich_orders, finished_orders)
# show(finished_orders)


def show_magicians(names):
    for name in names:
        print(name)


# old = ['mu', 'ke', 'sad', 'pk']
# new = []
# show_magicians(old)


def make_great(old, new):
    while old:
        current_name = 'the Great ' + old.pop()
        new.append(current_name)


# make_great(old[:], new)
# show_magicians(new)
# show_magicians(old)
# print(new)
# print(old)


def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


# user_profile = build_profile('a', 'b', fk='c', upi='d', asd=True)
# print(user_profile)
