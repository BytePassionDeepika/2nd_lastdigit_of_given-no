number=int(input("Enter the number:"))
num_str=str(number)
len_num=len(num_str)
if len_num <2:
    print("The Number is less than 2 digit") 
else:
    print("The Second last digit of the number is",num_str[-2])
