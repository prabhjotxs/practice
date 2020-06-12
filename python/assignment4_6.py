def computepay(h, r):
    if (h > 40):
        fix_rate = h * r;
        ovt_rate = (h - 40) * (r * 0.5)
    return fix_rate + ovt_rate

s_hrs = input("Enter Hours:")
s_rate = input("Enter rate per hour:")

hrs = float(s_hrs)
rate = float(s_rate)

p = computepay(hrs, rate)
print("Pay",p)