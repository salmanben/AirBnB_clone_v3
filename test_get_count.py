#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

# #!/usr/bin/python3
# """ Test .get() and .count() methods
# """
# from models import storage
# from models.user import User

# # user = User(
# #         email = "lacen@gmail.com",
# #         password = "12345",
# #         first_name = "lah",
# #         last_name = "cen"
# #         )
# # storage.new(user)
# # storage.save()

# print("All objects: {}".format(storage.count()))
# print("User objects: {}".format(storage.count(User)))

# first_state_id = list(storage.all(User).values())[0].id
# print(first_state_id)
# print("First User: {}".format(storage.get(User, first_state_id)))
