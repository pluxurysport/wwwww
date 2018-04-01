def perevod(result):
	eur = 70
	dol = 60
	uah = 2
	currency = int(input('dollar - 400, euro - 401, uah - 402, \n'))
	if currency == 400:
		cash = round (result/dol,2)
		print ('Доллар:' , cash )
	elif currency == 401:
		cash = round (result/eur,2)
		print ('Евро: ',cash)
	elif currency == 402:
		cash = round(result*uah, 2)
		print('Гривна: ',cash)
	else:
		cash = 0
		print ('Error')
		return 0
	return cash
