# Simple interest formula is given by: Simple Interest = (P x T x R)/100
# Where, P is the principle amount T is the time and R is the rate
def simple_interest(p, t, r):
    print(f"Principal Amount: {p}")
    print(f"Time: {t}")
    print(f"Rate of Interest: {r}")
    s = (p * t * r) / 100
    print(f"Simple Interest: {s}")


p, t, r = map(float, input("Enter p t r values:").split(" "))
simple_interest(p, t, r)

