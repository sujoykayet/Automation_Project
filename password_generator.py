import random as r
def create_password():
    lstA_Z = []
    lsta_z = []
    lst0_9 = []
    lst_symbol = []
    password = []
    str_password = ""

    for i in range(65,91):
        lstA_Z.append(chr(i))
    # print(lstA_Z)

    for i in range(97,123):
        lsta_z.append(chr(i))
    # print(lsta_z)

    for i in range(10):
        lst0_9.append(str(i))
    # print(lst0_9)

    for i in range(33,42):
        lst_symbol.append(chr(i))
    # print(lst_symbol)

    for l in range(2):
        password.append(r.choice(lstA_Z))
    for l in range(2):
        password.append(r.choice(lsta_z))
    for l in range(2):
        password.append(r.choice(lst0_9))
    for l in range(2):
        password.append(r.choice(lst_symbol))
    
    r.shuffle(password)

    for k in password:
        str_password += k
    print("Your password is: ",str_password)
    return str_password