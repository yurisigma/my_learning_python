class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def read_number_served(self):
        print("有" + str(self.number_served) + "人在这里就餐过")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " 正在营业.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['banana', 'chocolate', 'lemon']


# IceCream01 = IceCreamStand('DQ', 'ICEBERGS')
# IceCream01.describe_restaurant()
# print(IceCream01.flavors)


# restaurant01 = Restaurant('kfc', '快餐')
# restaurant01.number_served = 10
# restaurant01.read_number_served()
# restaurant01.set_number_served(80)
# restaurant01.read_number_served()
# restaurant01.increment_number_served(1000)
# restaurant01.read_number_served()

# restaurant02 = Restaurant('上海汤包', '中餐')
# restaurant01.describe_restaurant()
# restaurant01.open_restaurant()

class Car:
    def __init__(self, make, model, year):
        self.gas_tank = 50
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        print(long_name.title())

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def reset_odometer(self):
        self.odometer_reading = 0

    def fill_gas_tank(self):
        print("This car's tank is " + str(self.gas_tank))


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        range01 = 0
        if self.battery_size == 70:
            range01 = 240
        elif self.battery_size == 85:
            range01 = 270
        message = "This car can go approximately " + str(range01)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# my_tesla = ElectricCar('tesla', ' model s', '2016')
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
# my_new_car = Car('Audi', 'a4', '2016')
# my_tesla.get_descriptive_name()
# my_new_car.get_descriptive_name()
#
# my_tesla.fill_gas_tank()
# my_new_car.fill_gas_tank()
#
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
# my_new_car.reset_odometer()
# my_new_car.read_odometer()
#
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


class User:

    def __init__(self, first_name, last_name, gender, birthday_year=1990, birthday_month=1, birthday_day=1):
        self.visits = {}
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday_year = birthday_year
        self.birthday_month = birthday_month
        self.birthday_day = birthday_day
        self.user_name = self.first_name + " " + self.last_name
        self.user_birthday = str(self.birthday_year) + "年" \
                             + str(self.birthday_month) + "月" \
                             + str(self.birthday_day) + "日"
        self.visits[self.user_name] = self.user_birthday
        self.login_attempts = 0

    def describe_user(self):
        print("姓名：" + self.user_name
              + "\n性别：" + self.gender
              + "\n生日：" + self.user_birthday)

    def greet_user(self):
        print("尊敬的" + self.user_name + "你好!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, gender, birthday_year=1990, birthday_month=1, birthday_day=1):
        super().__init__(first_name, last_name, gender, birthday_year, birthday_month, birthday_day)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

# user02 = Admin("Tom", "Strong", "male", 1991, 9, 9)
# user02.show_privileges()
# user01 = User("yuri", "sigma", "male", 1992, 6, 9)
# user01.describe_user()
# user01.increment_login_attempts()
# print(user01.login_attempts)
# user01.reset_login_attempts()
# print(user01.login_attempts)

# users = {}
# polling_active = True
# while polling_active:
#     first_name = input("\nWhat's your first name? ")
#     last_name = input("\nWhat's your last name? ")
#     gender = input("\nWhat's your gender")
#     birthday_year = input("\n Birthday Year?")
#     birthday_month = input("\n Birthday Month?")
#     birthday_day = input("\n Birthday Day?")
#     user = User(first_name, last_name, gender, int(birthday_year), int(birthday_month), int(birthday_day))
#     users[user.user_name] = user.user_birthday
#     user.describe_user()
#     user.greet_user()
#
#     choose_active = True
#     while choose_active:
#         repeat = input("Would you like to let another person respond? (yes/no) ")
#         if repeat == 'yes':
#             break
#         elif repeat == 'no':
#             choose_active = False
#             polling_active = False
#         else:
#             print("You have to answer me, 'yes' or 'no'")
#
# print("\n --Polling Results--")
# print(users)
