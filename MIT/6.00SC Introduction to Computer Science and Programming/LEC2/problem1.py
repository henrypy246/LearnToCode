from datetime import date
from datetime import datetime
def hello():
	name = input('Enter your name: ')
	birth_day = datetime.strptime(input('Enter your birthday: '),'%m/%d/%Y')
	print('hello ',name, 'you was born on ',birth_day)
hello()