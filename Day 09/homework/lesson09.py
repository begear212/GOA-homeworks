age = int(input("12"))
if age >= 18:
    print("მანქანის ტარება შეგიძლია")
else :
    print("მანქანის ტარება არ შეგიძლია")

temperature = float(input("41.5"))

if temperature >= 28:
    print("თბილა")
else:
    print("ცივა")

bread_count = int(input("24"))

if bread_count >= 1:
    print("ცოტა პური დაგვრჩა")
else:
    print("პურის ყიდვა გვჭირდება")

price = float(input("100"))
discount = float(input("(20%)"))
balance = float(input("80"))

final_price = price - (price * discount / 100)

if balance >= final_price:
    print("თქვენ გაქვთ საკმარისი ფული")
else:
    print("თქვენ საკმარისი ფული არ გაქვთ")

number = int(input("73173217"))

if number %2 !=0:
    print("კენტია")
else:
    print("ლუწია")





