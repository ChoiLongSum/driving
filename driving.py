country = input('which country are you from?')
age = input('what is your age?')
age = int(age) # remember to change string to interger!
if country == 'taiwan':
	if age >= 18: 
		print('you can have a driving license')
	else:
		print('you cannot have a driving license yet.')
elif country == 'america':
	if age >= 16:
		print('you can have a driving license')
	else:
		print('you cannot have a driving license yet.')
