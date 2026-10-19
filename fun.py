#recursion method
#def show(n):
  #  if(n==0):
 #       return
    #print(n)
    #show(n-1)
    #print("end")
#show(3)

# recursion through factorial
#def factorial(n):
 #   if(n==0 or n==1):
  #      return 1
   # return n*factorial(n-1)
#print(factorial(5))

#practice question
def add(n):
    

    if (n==0):
     return 0
    return add(n-1)+n
print(add(10))

#print list to using recursion
def print_list(list,idx=0):
   if(idx==len(list)):
      return
   print(list[idx])
   print_list(list,idx+1)
fruits=["mango","banana","apple"]
print_list(fruits)
