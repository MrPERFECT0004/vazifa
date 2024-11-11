import os

file_name = "users_info.txt"
user_id = 1
def save_to_file(data):
    with open(file_name, "a") as file:
        file.write(data + "\n")

def is_valid_phone(phone):
    return phone.startswith("+998") and phone[4:].isdigit()

def get_user_data():
    global user_id
    while True:
        name = input("Ismingizni kiriting: ")
        lastname = input("Familiyangizni kiriting: ")
        
        while True:
            try:
                age = int(input("Yoshingizni kiriting: "))
                if age <= 0:
                    print("Yosh musbat butun son bo'lishi kerak. Iltimos, qayta kiriting.")
                    continue
                break
            except ValueError:
                print("Yoshni butun son sifatida kiriting.")
    
        while True:
            phone = input("Telefon raqamingizni kiriting (+998 formatida): ")
            if is_valid_phone(phone):
                break
            else:
                print("Telefon raqami noto'g'ri formatda. Iltimos, qayta kiriting.")
        
        email = input("Elektron pochta manzilingizni kiriting: ")
        address = input("Manzilingizni kiriting: ")

        user_data = f"ID: {user_id}, Ism: {name}, Familiya: {lastname}, Yosh: {age}, Telefon: {phone}, Email: {email}, Manzil: {address}"
        save_to_file(user_data)
     
        user_id += 1
        another = input("Yana bir foydalanuvchi qo'shish kerakmi? (ha/yo'q): ")
        if another.lower() != "ha":
            break

def main():

    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            pass
    
    print("Foydalanuvchi ma'lumotlarini kiritishni boshlaymiz...")
    get_user_data()

if __name__ == "__main__":
    main()
