#function is block of statement that perform a specific task
def add_numbers(a, b):
    c = a + b
    return c

c = add_numbers(5, 6)
#print(c)

#function definiton with default argument
def add_numbers(a, b=5):
    c = a + b
    return c    
c = add_numbers(5)
#print(c)
def cal_sum(a,b):
    c = a + b
    return c
c = cal_sum(5,6)
#print(c)
def calc_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average

average = calc_average(5, 6, 7)
#print(average) 

def suraj():
    #print("hekko suraj")
    return "hello suraj"
suraj()
def factorial(n):
    if n==0:
        return 1
    else:
      return n*factorial(n-1)
    result = factorial(5)
    print(result)
    