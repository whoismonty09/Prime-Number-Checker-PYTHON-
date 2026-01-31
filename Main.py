print("Prime Number Checker developed by Monty")
while True:
    try:
        num = int(input("Enter a number (or type 0 to exit):"))

        if num == 0:
            print('Good Byee!')
            break

        if num <=1:
            print("Not a prime number")
        else:
            is_prime = True
            for i in range (2 ,int(num ** 0.5) +1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print("Prime Number")
            else:
                print("Not a Prime Number")  

    except ValueError:
        print("Please enter a valid integer!")                        
