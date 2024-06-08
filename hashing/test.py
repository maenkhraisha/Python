import hashlib

print("============ output ==================")
hash = hashlib.new("SHA256")

user_input_password = "maen888831919999"
hash.update(user_input_password.encode())

print(hash.hexdigest())

