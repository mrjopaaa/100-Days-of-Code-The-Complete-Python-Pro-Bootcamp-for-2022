class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "joe_joe_joe")
user_2 = User("002", "angela")

user_1.foolow(user_2)






"""Adding new attributes in class"""
"""ATTRIBUTE == variable associated with an object"""


user_1.id = "001"
user_1.username = "joe_joe"

print(user_1.username)