menu={"sandwich":60,"coffee":10,"burger":60}
print(menu)
a=int(input("how much sandwich did you eat?"))
b=int(input("how much sandwich did you eat?"))
c=int(input("how much sandwich did you eat?"))
bill=(a*menu["sandwich"]+b*menu["coffee"]+c*menu["burger"])
print(bill)