from random import randint as r
while True:
    login=input("Do you want to login (Y/YES) :").strip().upper()
    if login in ("YES","Y"):
        d=r(1,1000)
        print(f"Your otp is :{d}")
        user=int(input("Enter the Otp for Login :"))
        if user==d:
            print("Login Sucessfull....")
            break
        else:
            print("Incorrect otp")
    else:
        print("Thanks for Visiting....")
