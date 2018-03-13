import pyodbc
from datetime import datetime, timedelta
from math import factorial, exp

def summation(m,u):
    x = 0
    for n in range(m):
        x += (u**n/factorial(n))
    return x

def erlang(m,u):
    a = (u**m/factorial(m))
    b = 1 - (u/m)
    c = summation(m,u)
    return a/(a+b*c)

def speed_of_answer(m,u,e,t):
    return (e*t)/(m*(1-(u/m)))

def service_level(m,u,e,t,tar):
    return 1 - e*exp(-(m-u)*(tar/t))

def est_agents(u,t,tar):
    m = 0
    sl = 0
    while sl < 0.85:
        m += 1
        e = erlang(m,u)
        try:
            sl = service_level(m,u,e,t,tar)
        except:
            sl = 1
    return m

if __name__=="__main__":
    ''' An example usage of the summation function '''
    print(summation(10,2))
