""" Unit Converter """

def pound_kilo(pounds):
    convertion_rate = 0.453592
    kilos = pounds * convertion_rate
    return kilos

def kilo_pound(kilos):
    convertion_rate = 2.20462
    pounds = kilos * convertion_rate
    return pounds

if __name__ == '__main__':
    print ("\n")
    pounds = int(input("Enter Pounds: "))
    print ("\n")
    print (pound_kilo(pounds))
    print ("\n\n")
    kilos = int(input("Enter Kilos: "))
    print ("\n")
    print (kilo_pound(kilos))
