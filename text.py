### 一
# 变量
# message = "hello world!"
# print(message)
# message = "hello world haha"
# print(message)

# 修改字符串大小写
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())

# 合并拼接字符串
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + "" + last_name
# print(full_name)

# 制表符和换行符
# print("Languages:\n\tPython\n\tC\n\tJavascript")

# 删除空白
# lan = " python "
# lan = lan.rstrip().lstrip()
# print(lan)

# 使用str()函数避免类型错误
# age = 23
# message = "Happy " + str(age) + "rd Birthday"
#print(message)

### 二
# 列表
# bicycles = ['trek','cannondcle','redline','specialized']
# print(bicycles[0].title())
# print(bicycles[3].title())
# print(bicycles[-2].title())
# message = "My first bicycle was a " + bicycles[0].title() + "."
# print(message)

# 修改列表元素
# moto = ['honda','yamaha','suzuki']
# print(moto)
# moto[0] = "ducati"
# print(moto)
# moto[1] = "zzt"
# print(moto)

# 列表中添加元素
# moto = ['honda','yamaha','suzuki']
# print(moto)
# moto.append('ducati')
# print(moto)
# mo = []
# mo.append('honda')
# mo.append('yamaha')
# mo.append('suzuki')
# print(mo)

# 列表中插入元素
# moto = ['honda','yamaha','suzuki']
# moto.insert(1,'docati')
# print(moto)

# 列表中删除元素del  pop
# moto = ['honda','yamaha','suzuki']
# print(moto)
# del moto[0]
# print(moto)
# del moto[0]
# print(moto)
# mo = ['honda','yamaha','suzuki']
# print(mo)
# poped_moto = mo.pop(-1)
# print(mo)
# print(poped_moto)

# 根据值删除元素
# moto = ['honda','yamada','suzuki','ducati']
# print(moto)
# moto.remove('ducati')
# print(moto)

# 使用sort()对列表进行永久性排序
# cars = ['bwm','audi','toyota','subaru']
# cars.sort(reverse=True)
# print(cars)

# 使用函数sorted()对列表进行临时排序
# cars = ['bwm','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# 倒着打印列表
# cars = ['bwm','audi','toyota','subaru']
# print(cars)
# cars.reverse()
# print(cars)

# 确定列表长度
# cars = ['bwm','audi','toyota','subaru']
# print(len(cars))

### 三
# 遍历列表
# magicians = ['alice','david','caro']
# for magician in magicians:
# 	print(magician.title() + ", that was a great trick!")

# 使用函数range()
# for value in range(1,5):
# 	print(value)

# 使用range()创建数字列表
# numbers = list(range(1,6))
# print(numbers)
# even_num = list(range(2,11,2))
# print(even_num)
# squares = []
# for value in range(1,11):
# 	squares.append(value**2)
# print(squares)
# squares = [value**2 for value in range(1,11)]
# print(squares)
# 对数字列表进行统计计算
# nums = [1,2,3,4,5,6,7,8,9,0]
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# practice
# for value in range(1,21):
#	print(value)
# num = list(range(1,1000001))
# for value in num:
#	print(value)
# print(min(num))
# print(max(num))
# print(sum(num))
# num = list(range(1,20,2))
# for value in num:
# 	print(value)
# num = list(range(3,31,3))
# print(num)
# nums = []
# for value in range(1,11):
#	num = value**3
#	nums.append(num)
# print(nums)
# nums = [value**3 for value in range(1,11)]
# print(nums)

# 使用函数的一部分
# players = ['A','B','C','D']
# print(players[2:3])
# for player in players[:3]:
# 	print(player.title())
# my_foods = ['A','B','C']
# friend_foods = my_foods[:]
# for my_food in my_foods:
#	print(my_food)
# for friend_food in friend_foods:
#	print(friend_food)

# 元组
# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])
# for dimension in dimensions:
#	print(dimension)
# dimensions = (400,100)
# print(dimensions[0])

# foods = ('A','B','C','D','E')
# foods[0] = 'B'
# print(foods)
# for food in foods:
#	print(food)
# foods = ('A','F','H','D','E')
# for food in foods:
# print(food)


# if语句
# cars = ['audi','bwm','subaru','toyota']
# for car in cars:
#	if car == 'bwm':
#		print(car.upper())
#	else:
#		print(car.title())

# vegetables = ['mushroom','onions','pineapple']
# print('mushroo' not in vegetables)

# age =  18
# if age >= 18:
#	print("your are old enough to vote!")
# print("Have you registered to vote yet?")

# age = 12
# if age < 4:
#	price = 0
# elif age < 18:
#	price = 5
# else:
#	price = 10
# print("your admission cost is $"+ str(price) + "!")

# alien_color = 'gr'
# if alien_color == 'green':
#	print("you get 5 point")
# elif alien_color == 'yellow':
#	print("you get 10 point")
# elif alien_color == 'red':
#	print("you get 15 point")

# shop_vegetables = ['mushroom','green peppers','extra cheese']
# user_vegetables = ['mushroom','pineapple','extra cheese']
# for user_vegetable in user_vegetables:
#	if user_vegetable in shop_vegetables:
#		print("Adding " + user_vegetable + "!")
#	else:
#		print("Sorry, we don't have " + user_vegetable + "!")
# print("\nFinish making your pizza!")
 
### 字典
# alien_o = {'color':'green','points':5}
# print("The alien color is " + alien_o['color'])
# alien_o['color'] = 'yellow'
# del alien_o['points']
# print(alien_o)

# favorite_languages = {
#	'jen':'python',
#	'sarah':'c',
#	'edward':'ruby',
#	'phil':'phton',
#	'zzt':'python',
#	}
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#	print(name.title())
#	if name in friends:
#		print('Hi' + name.title() +
#			',I see your favorite language is ' + 
#			favorite_languages[name].title() + '!')

#for name in sorted(set(favorite_languages.values())):
#	print(name)

#嵌套
# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'green','points':10}
# alien_2 = {'color':'green','points':15}
# aliens = [alien_0,alien_1,alien_2]
#for alien in aliens:
#	print(alien['color'])

# aliens = []
# for alien_number in range(30):
#	new_alien = {'color':'green','points':5,'speed':'slow'}
#	aliens.append(new_alien)
# for alien in aliens[0:3]:
#	if alien['color'] == 'green':
#		alien['color'] = 'yellow'
#		alien['speed'] = 'medium'
#		alien['points'] = 10
		
# for alien in aliens[0:5]:
#	print(alien)
# print(str(len(aliens)))

# pizza = {
#	'crust':'thick',
#	'toppings':['mushrooms','extra cheese']
#	}
# for topping in pizza['toppings']:
#	print('\n'+topping)


### 用户输入和ehile循环
# message = input()
# print(message)

# current_number = 1
# while current_number <= 5:
#	print(current_number)
#	current_number += 1


# while True:
#	message = input()
#	if message == 'quit':
#		break
#	else:
#		print(message)

# responses = {}
# keys = True
# while keys:
#	name = input("\nWhat's your name? ")
#	response = input("who's your love? ")
#	responses[name] = response
#	repeat = input("again?(yes/no)")
#	if repeat == 'no':
#		keys = False
# print("\n-----------")
# for name,response in responses.items():
#	print(name,response)


## 函数
# def describe_pet(animal_type,animal_name):
#	print("I have a " + animal_type + "," + "name is " + animal_name)
# describe_pet('cat','tom')
# describe_pet(animal_type='dog',animal_name='lengwa')

def make_pizza(size,*toppings):
	print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)

# def build_profile(first,last,**user_info):
#	profile = {}
#	profile['first_name'] = first
#	profile['last_name'] = last
#	for key,value in user_info.items():
#		profile[key] = value
#	return profile
# user_profile = build_profile("ali","baba",location="princeton",field="physics")
# print(user_profile)

### 类  self 与 js 中的 this 类似 

#class Dog():
#	def __init__(self,name,age):
#			self.name = name
#		self.age = age
#	
#	def sit(self):
#		print(self.name.title() + " is now sitting")
#		
#	def roll_over(self):
#		print(self.name.title() + " rolled over")
# my_dog = Dog('willie',6)
# your_dog = Dog("willie",3)
# print("my dog name is " + my_dog.name.title())
# print("my dog is " + str(my_dog.age) + "years old")
# my_dog.sit()
# my_dog.roll_over()
# your_dog.sit()

#class Car():
#	def __init__(self,make,model,year):
#		self.make = make
#		self.model = model
#		self.year = year
#		self.odometer_reading = 0
#	def get_descriptive_name(self):
#		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#		return long_name.title()
#	def read_odometer(self):
#		print("This car has " + str(self.odometer_reading) + " miles on it")
#	def update_odometer(self,mileage):
#		if mileage >= self.odometer_reading:
#			self.odometer_reading = mileage
#		else:
#			print("you can't roll back an odometer")
#	def increment_odometer(self,miles):
#		self.odometer_reading += miles
# my_new_car = Car('audi','a4',2018)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_used_car = Car('subaru','outback','2015')
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#class Battery():
#	def __init__(self,battery_size=70):
#		self.battery_size = battery_size
#	def describe_battery(self):
#		print("This car has a " + str(self.battery_size) + "-KWh battery")
#	def get_range(self):
#		if self.battery_size == 70:
#			range = 240
#		elif self.battery.size == 80:
#			range = 270
#		message = "This car can go approximately " + str(range)
#		message += " miles on a full charge"
#		print(message)
		
#class ElectricCar(Car):
#	def __init__(self,make,model,year):
#		super().__init__(make,model,year)
#		self.battery = Battery()
	
#my_tesla = ElectricCar('tesla','model s',2016)
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()

