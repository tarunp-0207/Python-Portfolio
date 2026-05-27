def calculate():
    print("---advanced calculator---")

    try:
        n1=float(input("enter the first number:"))
        operator=input("enter operator(=,-,*,/,%,^) :").strip()
        n2=float(input("enter the second number:"))

    except ValueError:
        print("error!!!! , please enter a numeric value.")
        return
    
    if operator=="+":
        print(f"result:{n1+n2}")
        

    elif operator=="-":
        print(f"result:{n1-n2}")
        

    elif operator=="*":
        print(f"result:{n1*n2}")
        

    elif operator=="^":
        print(f"result:{n1**n2}")


    elif operator=="/":
        if n2==0: 
            print("custom error , you cannot divide a number by zero ")
        else:
            print(f"result:{n1/n2}")
            

    elif operator=="%":
        if n2==0:
            print(f"custom error ... cannot calculate remainder when dividing by zero")
        else:
            print(f"result:{n1%n2}")
            
    else:
        print("enter a valid operator")


calculate()
