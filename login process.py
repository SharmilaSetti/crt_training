#login process
db=[
    {'amrutha@exampe.com':'amrutha'},
    {'sharmila@example.com':'sharmila'},
    {'anusha@example.com':'anusha'},
    {'sana@example.com':'sana'},
    ]
print(db)
username=input("enter username:")
password=input("enter password:")
temp={username:password}
if temp in db:
        print("matched")
else:
        print("not matched")

