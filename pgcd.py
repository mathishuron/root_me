#!/usr/bin/env python3

def pgcd(a,b):
    u_n_moins_1 = 0
    v_n_moins_1 = 1
    u_n = 1
    v_n = - 1 * (a // b)
    while (a % b != 0):
        r = a % b
        a = b
        b = r
        (u_n, u_n_moins_1) = (u_n_moins_1 - (a // b) * u_n, u_n)
        (v_n, v_n_moins_1) = (v_n_moins_1 - (a // b) * v_n, v_n)
    return (b, u_n_moins_1, v_n_moins_1)

g = 209
p = 991
(buf, u, v) = pgcd(209,991)
print(u + p)

