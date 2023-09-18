import pywhatkit

phone_number = input("Enter phone number: ")
#pywhatkit.sendwhatmsg(phone_number, "ceci est un msg écrit par un bot", 22, 5, 10, True, 2)

pywhatkit.sendwhatmsg_instantly(phone_number, "ceci est un msg écrit par un bot", 8, True, 3)
