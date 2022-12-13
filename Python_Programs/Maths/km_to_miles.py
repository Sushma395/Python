def kilometre(km):
    cr = 0.62137 #conversion_ratio
    m = km * cr
    print(f"{km} kilometres = {m} miles")


km = float(input("Enter kms: "))
kilometre(km)
