# with open("practice.txt","w") as f:
#       f.write("Hi every one \n we are learning file IO \n using Java\ni like programming in Java")
# def check_fun():
#     with open("practice.txt","r") as f:
#         data=f.read()
#         print(data)
#     if(data.find("learnings")!=-1):
#        print("found and the index is  ",data.find("learning"))
#     else:
#          print("not fornd ")


# new_data =data.replace("java","pthon")
# print(new_data)

# with open ("practice.txt","w") as f:
#       f.write(new_data)
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

# make  a logic to find a line no of the given word
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
# def check_for_line():

#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no+=1
#     return -1
# check_for_line()
# def check_line_no():
#     lineno=1
#     data=True
#     word="are"
#     with open("practice.txt","r") as f:
#         data=f.readline()
#         while data:
#             if word in data:
#                 print(lineno)
#                 return 
#             lineno+=1
#     return -1
# l=check_line_no()
# print(l)

    
#    FIND even numbers from the file



    # print(data)
# def even_numbers():
#     count=0
#     with open("practice.txt","r") as f:
#         data=f.read()
#         while data==True:
#             for i in range(data(1,)):
#                 i%2==0
#                 count+=1
# with open ("practice.txt","r") as f:
#     data=f.read()
#     print(data)

# num=""
# for i in range(len(data)):
#     if (data[i]==","):
#         print(int(num))
#         num=""
#     else:
#         num+=data[i]

# program to check the number of the even numbers in the file
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



              



