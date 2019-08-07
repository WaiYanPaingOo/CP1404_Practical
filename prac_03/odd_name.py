"""WaiYanPaingOo"""
user_name = input("Enter your name: ")
name_count = len(user_name)

while name_count < 0:
    print("User name cannot be empty!")
    user_name = input("Enter your name: ")

print("Your Name is: ", end='')
for i in range(0, name_count+1, 2):
    print(user_name[i], end='')