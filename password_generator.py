import tkinter as tk
import random
import string

def generate_password():
    length = length_var.get()
    use_uppercase = upper_var.get()
    use_lowercase = lower_var.get()
    use_special = special_var.get()
    use_numbers = numbers_var.get()
    avoid_ambig = ambig_var.get()
    min_numbers = min_numbers_var.get()
    min_special = min_special_var.get()

    password = ""
    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_special:
        char_pool += string.punctuation
    if use_numbers:
        char_pool += string.digits
    if avoid_ambig:
        char_pool = char_pool.translate(str.maketrans('', '', '1Il0O5S8B'))

    while len(password) < length:
        password += random.choice(char_pool)

    # Ensure minimum number of numbers and special characters
    password_list = list(password)
    num_numbers = sum(c.isdigit() for c in password_list)
    num_special = sum(c in string.punctuation for c in password_list)
    while num_numbers < min_numbers:
        password_list[random.randint(0, length - 1)] = str(random.randint(0, 9))
        num_numbers += 1
    while num_special < min_special:
        password_list[random.randint(0, length - 1)] = random.choice(string.punctuation)
        num_special += 1
    password = ''.join(password_list)
    password_label.config(text=password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_label['text'])
    root.update()
    message_label.config(text="Password copied to clipboard.")
    root.after(3000, lambda: message_label.config(text=""))

root = tk.Tk()
root.geometry("400x400")
root.title("Random Password Generator")

length_var = tk.IntVar(value=8)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
ambig_var = tk.BooleanVar(value=True)
min_numbers_var = tk.IntVar(value=0)
min_special_var = tk.IntVar(value=0)

length_label = tk.Label(root, text="Password length:")
length_label.pack()
length_slider = tk.Scale(root, from_=8, to=128, orient="horizontal", variable=length_var)
length_slider.pack()

upper_check = tk.Checkbutton(root, text="Uppercase", variable=upper_var)
upper_check.pack()
lower_check = tk.Checkbutton(root, text="Lowercase", variable=lower_var)
lower_check.pack()
special_check = tk.Checkbutton(root, text="Special Characters", variable=special_var)
special_check.pack()
numbers_check = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
numbers_check.pack()
ambig_check = tk.Checkbutton(root, text="Avoid Ambiguous Characters", variable=ambig_var)
ambig_check.pack()

min_numbers_label = tk.Label(root, text="Minimum Number of Numbers:")
min_numbers_label.pack()
min_numbers_spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=min_numbers_var)
min_numbers_spinbox.pack()

min_special_label = tk.Label(root, text="Minimum Number of Special Characters:")
min_special_label.pack()
min_special_spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=min_special_var)
min_special_spinbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="", wraplength=350)
password_label.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

message_label = tk.Label(root, text="")
message_label.pack()

root.mainloop()
