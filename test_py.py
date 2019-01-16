# -*- codJng: UTF-8 -*-
while True:
    J = input("pls input the lirun:")
    J = int(J)
    if J <= 10:
        a = J * 0.01
        print(a)
    elif J <= 20 and J > 10:
        b = 0.25 + J * 0.075
        print(b)
    elif J <= 40 and J > 20:
        c = 0.75 + J * 0.05
        print(c)
    elif J <= 60 and J > 40:
        d = 0.95 + J * 0.03
        print(d)
    elif J <= 60 and J > 100:
        e = 2 + J * 0.015
        print(e)
    else:
        f = 2.95 + J * 0.01
        print(f)
    print("OK")
