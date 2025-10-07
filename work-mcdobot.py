# mcdobot
# author: julian
#  6 october 2025

print("so a burger and drink")

mmaf = input("do you want to add fries with your meal broski")

if mmaf.lower().strip("!,.? ") == "yes":
    print("ok")
    print("your total is $67.41")
elif mmaf.lower().strip("!,.? ") == "no":
    print("cheap bastard")
    print("your total is $41.67")
else:
    print(f"speak english bro what is {mmaf}")
