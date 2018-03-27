from math import factorial, exp

def summation(m,u):
    '''Sum of u^k/k! for k = 0 to m
    '''
    x = 0
    for k in range(m):
        x += u**k / factorial(k)
    return x

def erlang(m,u):
    '''Output of this formula is used to get speed of answer
       and service level where m is number of agents and
       u is the traffic intensity
    '''
    a = u**m / factorial(m)
    b = 1 - (u/m)
    c = summation(m,u)
    return a/(a + b*c)

def speedofanswer(m,u,e,t):
    '''Average waiting time for a call where m is number of agents,
       u is the traffic intensity, e is the output from the erlang
       function and t is the average call duration
    '''
    return (e * t)/(m * (1 - (u/m)))

def servicelevel(m,u,e,t,tar):
    '''Probability that call will be answered in less than a target
       waiting time, where m is number of agents, u is traffic
       intensity, e is output from the erlang function, t is average
       call duration and tar is the target waiting time
    '''
    return 1 - e * exp(-(m-u) * (tar/t))

def estagents(u,t,tar,sl):
    '''Calculate the number of agents required to achieve a specified
       service level, where u is the traffic intensity, t is the 
       average call duration, tar is the target waiting time and sl
       is the specified service level
    '''
    m = 0
    slt = 0
    while slt < sl:
        m += 1
        e = erlang(m,u)
        try:
            slt = servicelevel(m,u,e,t,tar)
        except:
            slt = 1
    return m
