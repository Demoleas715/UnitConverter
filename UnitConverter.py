""" Unit Converter """

def pound_kilo(pounds):
	convertion_rate = 0.453592
	kilo = pounds * convertion_rate
	return kilo

pounds = int(input("Enter Pounds: "))
print (pound_kilo(pounds))