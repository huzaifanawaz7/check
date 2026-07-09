with open ("practice.txt","r") as f:
     data=f.read()
     print(data)
num=""
count=0
for i in range(len(data)):
     if data[i]==",":
          if int(num)%2==0:
               count+=1
               num=""
     else:
          num+=data[i]
if num!="":
     if int(num)%2==0:
          count+=1
print("total no of even no in the file are ",count)


# using split function to find the even numbers in the file..
