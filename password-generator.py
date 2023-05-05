import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = input("Enter the length of your password : ")
    if plen.isdigit():
        plen = int(plen)
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        t = s
        #way 1
        random.shuffle(s)
        password1 = "".join(s[0:plen])
        print(f"Your generated passwod is : {password1}")
        #way2
        password2 = "".join(random.sample(t, plen))
        print(f"Your generated passwod is : {password2}")
    else:
        print("Please enter a numeric value")