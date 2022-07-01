# Alexander Mallalieu
# Dec 8th, 2021

print("")
print("Password must contain at least 1 capital, 3 numbers and 1 special character, spaces are not permitted.")
password = input("Please enter your new password:")
count_nums = 0
count_special_characters = 0
count_capitals = 0
newPassword = ("")
passwordAttempt = ("")
for x in password:
    if x.isdigit():
        count_nums = count_nums+1
    if x.isupper():
        count_capitals = count_capitals+1
    if x.isalpha() == 0 and x.isdigit() == 0:
        count_special_characters = count_special_characters + 1
    if x.isspace():
        print("Error: Password cannot not contain spaces.")
        exit()
if count_capitals >= 1 and count_nums >= 1 and count_special_characters >= 1 and len(password) >= 8:
    print("Valid Password")
else:
    print("Error:")
if count_capitals == 0:
    print("- Password must contain at least one capital letter.")
if count_nums == 0:
    print("- Password must contain at least one number.")
if count_special_characters == 0:
    print("- Password must contain at least one special character.")
if len(password) < 8:
    print("- Password must contain at least 8 characters.")

confirmPassword = input("Confirm Password:")

if confirmPassword == password:
    print("Password Confirmed")
    newPassword = password
else:
    print("Password incorrect")

while passwordAttempt != newPassword:
    passwordAttempt = input("Enter Password to gain access to files:")
    print("Incorrect Password")
if passwordAttempt == newPassword:
    print("Access Granted:")
    print("")
    print("")
    print("────░░░───────────────────────────░░░───")
    print("─░░░─────────░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓─────░───")
    print("░░──────▒█████████████▓▓▓▓▓▒▓▓██▓────░──")
    print("░────▒███▓▒▒░──░▒▒░──░░░░░░░────██────░─")
    print("░───██░───░░▒░░░░───░─░░▒▒▓▓▒░───██───░░")
    print("───▓█───▒░───▒░────▒───────▒▒▒░──░█────░")
    print("───█▒─────────░──────▓████▒───────██────")
    print("──██────██████─────██▓▓█████▓─░────██───")
    print("─██▒░───▓███████──░████▓█▓▒█▒─▓▓▓█▒─██▓─")
    print("▓█─░▓██▓──────█─────▒───▒█▓░▒███▓░██──█▒")
    print("██──▒░▒███▒──██───────────▒▒▒──▒█──██─░█")
    print("░█─░──█────██▓─────▓██▒─────▒██▒██▒▓█──█")
    print("─██░─██░───██▓───██▓░█──▒████───█░─█░─██")
    print("──█──████▓───▒██───░████▓░─██▒███────██─")
    print("──█▓─█▓█░███████████▒░█──▒███▒██────██──")
    print("──█▓─███░█▓──█▒─░█───▒███████▓█────██───")
    print("──██─███████████████████───░██────▓█────")
    print("──██─██████████████▒───█──██▓────░█░───░")
    print("──█▓─░██▓█─█─▒█───█────████─────██▒───░░")
    print(" ──█▒──▒██████▒█▒▒███████▒──░▒▓███─────░─")
    print("──█░──────▒▒██████▒▒░░──░▒░▓███▒──────░─")
    print("──█──▒─▒▒──────────░▒▒░──▓██░────░░────░")
    print("──█──░▒▒▒▒▒░░─░─░─░───░███████▒───░────░")
    print("──██─────────────░▒▒▓███████████──░░───░")
    print("───██▓░──────▒▓████▓░──█████████▒──░────")
    print("──░──█████████████───▒▓██████████──░░───")
    print("──░──██████████████▒▓████████████░──░───")
    print("──░──▓███████████▓───░███████████▓──░───")
    print("──░───███████████─────████████████──░───")
    print("───░───██████████░▒███████████████──░───")
    print("───░░───▓███████████████████▒─▓██───░───")
    print("───░▒───█████████████████████──────░░───")
    print("──░░───██████████████████████───░░░─────")
    print("─░░───████████████████████████──░▒─────░")
    print("─░───█████████████████████████───▒─────░")
    print("░───██████████████████████████▓───░░────")
    print("░──▓███████████████████████████░───░░───")
    print("──░█████████████████████████████▓───░░──")
    print("░──▓██████████████████████████████────░─")
    print("░────▓█████████████████████████████░───░")
    print("▒────███████████████████████████████▒──░")
    print("───▒█████████████████████████████████───")
    print("──▒███████████████████████████████████──")
    print("─░████████████████████████████████████──")
    print("─█████████████░─────────░█████████████░─")
    print("─███████████░─────────────████████████──")
    print("─▓██████████───░░░░░░▒▒───▒███████████──")
    print("──██████████──░░────░░───░███████████▒──")
    print("──██████████──░─────░───█████████████───")
    print("───█████████──░░───░───█████████████───░")
    print("░──█████████───░───░───███████████▒───░░")
    print("░──▒████████░──░───░──██████████▒────░░─")
    print("░───████████▓──░───░──███▓████▒────░░───")
    print("░░──████████───░───░───██░─▓─────░░░────")
    print("─░──▒███▒─█▓──░░───░░───▒███───░░───────")
    print("─░░───░█░─▓█──░░────░░───███──░░──────░░")
    print("──░────█▓███──░──────░░───░───░────░░░──")
    print("──░░──█▒─██───░────────░─────░░───░░────")
    print("──░──░████───░░─────────░░░░░─────░─────")
    print("──░░──▒░────░░────▒░─────────────░──────")







