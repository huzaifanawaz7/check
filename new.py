# print ("i have made a new file now which is untracked by the git now i am im initilizing a git in the new file ")
# first function
# def calc_sum(a,b):
#     return a+b
# a=calc_sum(2,3)
# print(a)

# recursion with examples 
# when we c
# all a function with  in the body of that function  of again with the base condition as a stopping thing instead of it will moving infinitely
# one of the most basic question to understand the recursion.
# def rec(n):  
#     if n==6:
#         return 
#     print (n)
#     rec(n+1) 
# rec(1)

# def fectorial(n):
#     if n==1:
#         return
#     fectorial(n*n-1)
# fectorial(3)
    
# def xyz():
#     print("this is the recursion in the which is non sense")
#     xyz()
# xyz()
# n=int(input("enter the number you want to find the sum"))
# def sum(s):
#     if s==1:
#         return 1
#     else:
#         return(s+sum(s-1))
# z=sum(n)
# print(z)
# fabonacchi series through the RecursionError...
# def pri(n):
#     if n==0:
#         return
#     print(n)
#     pri(n-1)
# pri(5)
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))
# print sum of the n narural numbers 

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# print( sum(5))
# print from the list with the recursive function.///

# def show(list , idx):
#     if idx==len(list):
#         return 
#     print(list[idx])
#     return show(list , idx+1)
# lis=[1,2,3,4]
# show(lis,0)
# jfidfkds
# f=open("demo.txt","r")
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# print(f.tell())


# file input and output in the file.
# f=open("demo.txt", "r")
# data=f.read()
# print(data)
# f=open("demo.txt","a")
# f.write("now i have open a file in the append mode like now i can write a new data in the file like no the previous data will be lost")
# f.close()
# f=open("demo.txt","r+")
# f.write("he is my brother and i want live with him")
# data=f.read()
# print(data)
# f.close()
# print()
# find the smallest value 
def small(n1,n2,n3):
    if n1<n2 and n1<n3:
        print("n1 is the smallest number")
    elif n2<n3 and n2<n1:
        print("n2 is the smallest number ")
    else:
        print("thr smsllest number is 1")

     
     
    #  a small loop game 
        count=0
# num=3
# i=0
# while True:
#       i=int(input ("enter a number you want to check :"))
#       if(i==num):
#             print("this is th number you tare trying to find",num,"and the count is ",count)
#       else:      
#         print("this is not that number ")
#         count+=1
#         print("you have tried ",count ,"times ")


        # factorial using a function
l=int(input("enter a number :"))
def factorial(n):
    f=1

    for i in range(1,n):
        if(i<=n):
            f*=i
            i+=1
    print("the factorial is ",f)

    
    factorial(l)












 

