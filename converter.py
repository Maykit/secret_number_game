# This is a mile/kilometer converter

print "Hello user. I am here to help you convert kilometers to miles."



while True:

    km = float(raw_input("Enter distance in km: "))
    m = km * 0.62137119
    print "Equals distance in m: " + str(m)

    cont = str.lower(raw_input("Want to enter another distance? Yes / No?"))

    if cont == "no":
        print "Thanx for using the converter"
        break
    elif cont == "yes":
        print "Good. Do it again."
    else:
        cont = str.lower(raw_input("Want to enter another distance? Yes / No?"))
