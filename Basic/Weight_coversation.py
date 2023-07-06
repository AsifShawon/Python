weight = float(input("Weight: "))
unit = input("(K)gs or (L)bs: ")

if unit == 'K' or unit == 'k':
    print("Weight in lbs: ", (weight * 2.205))
elif unit == 'L' or unit == 'l':
    print("Weight in kg: ", (weight / 2.205))
