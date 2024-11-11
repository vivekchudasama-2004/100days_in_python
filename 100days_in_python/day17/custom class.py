# class User:
#     def __init__(self, first_name, last_name):
#         is_over=True
#         while is_over:
#             all_user=" "
#             user=input("do you want to create a new user?(y/n) ").lower()
#             if user=='y':
#                 first_name=input("Enter your first name: ")
#                 last_name=input("Enter your last name: ")
#
#                 #creating the attribute self.attribute names
#                 self.first_name = first_name
#                 self.last_name = last_name
#                 print(f"Hello {first_name} {last_name}")
#                 all_user+=all_user+self.first_name+self.last_name
#             elif user=="all user":
#                 print(all_user)
#             else:
#                 is_over=False

#
# user1 = User(first_name="", last_name="")



# class User:
#     def __init__(self,user_id,user_name):
#         id=input("enter your id :")
#         name=input("enter your name :")
#         #creating that attribute which is associated with the class
#         self.id=user_id
#         self.name=user_name
# #         print(f"id:{id} , name:{name}")
# # user=User(user_id="",user_name="")
#
#
# #we can inisilize the value with this also
#
# # user=User("001","vivek")
# # print(user.id)
# # print(user.name)

#if function is atteched to object it known as method

class User:
    def __init__(self,user_id,user_name):
        #creating that attribute which is associated with the class
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        #if user follow someone
        self.following+=1

user1=User("001","vivek")
user2=User("002","v")

user1.follow(user2)
print(f"user1 followers :{user1.followers},user1 following : {user1.following}")
print(f"user2 followers :{user2.followers},user2 following  :{user2.following}")

