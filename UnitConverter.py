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
    answer = input("\nWould you like to convert pounds to kilos or kilos to pounds? ")
    if answer == 'pounds to kilos':
        pounds = int(input("\nEnter Pounds: "))
        print (pound_kilo(pounds))
    elif answer == 'kilos to pounds':
        kilos = int(input("\nEnter Kilos: "))
        print (kilo_pound(kilos))
    else:
        print ("\nError! Option not available.")
        