email = input("Enter your Email : ")
k, d, j = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            domain_part = email.split("@")[1]  # Get the domain part
            if "." in domain_part and not (domain_part.startswith(".") or domain_part.endswith(".")):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong email 5")
                else:
                    print("right email")
            else:
                print("wrong email 4")     
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")
