p = float(input("Enter the principal "))
t = float(input("Enter time interval "))
r =float(input("Enter the interest rate "))


def take_value():
    return [p, t, r]


def cal_value():
    res = take_value()
    x = res[0]
    y = res[1]
    z = res[2]
    return x * y * z / 100


def dis_value():
    print(cal_value())

dis_value()
