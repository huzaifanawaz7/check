num=3
# i=0
# while True:
#       i=int(input ("enter a number you want to check :"))
#       if(i==num):
#             print("this is th number you tare trying to find",num,"and the count is ",count)
#       else:      
#         print("this is not that number ")
#         count+=1
#         print("you have tried ",count ,"times ")
# with open ("demo.txt","r") as f :
#         l=f.read()
#         print(l)

# with open ("demo.txt","w") as f:
#     f.write("new data has come ")
# import os
# os.remove()
with open ("sample.txt","w") as f :
    f.write("thsi is new file created from the code")
import os
os.remove("sample.txt")
