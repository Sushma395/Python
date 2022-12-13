# The formula to calculate compound interest annually is given by: A = P(1 + R/100) t; Compound Interest = A – P
# Where, P is the principal amount T is the time and R is the rate
def compound_interest(p, t, r):
    print(f"Principal Amount: {p}")
    print(f"Time: {t}")
    print(f"Rate of Interest: {r}")
    a = p*(1 + (r/100))**t
    c = a - p
    print(f"Compound Interest: {c}")


compound_interest(1000, 1, 2)

