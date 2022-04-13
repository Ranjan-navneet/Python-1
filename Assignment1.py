radius=int(input("ENTER THE RADIUS :"))
area_circle= 3.14*radius*radius;
print("AREA OF CIRCLE IS :",area_circle)

f_name=str(input("Enter the file name "))
if f_name==".py":
    print("python")
elif f_name==".c":
    print("C program")
else:
    print("C++")
