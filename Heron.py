from fractions import Fraction


def heron(a, init=1, p=10 ** -20, afficher=False):

    x = init
    f = lambda u: (u + a / u) / 2
    y = f(x)

    while abs(x - y) > p:
        if afficher:
            print(y)
        x, y = y, f(y)

    return y


a = Fraction(54732, 100)
u0 = Fraction(30)
p = Fraction(1, 10 ** 10)


sqrt_a = heron(a, init=u0, p=p, afficher=True)
print(float(sqrt_a))
