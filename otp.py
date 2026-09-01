import random 

otp = random.randint(100000, 999999) 
print("OTP has been generated.") 

for attempt in range(3):    
    entered = int(input("Enter OTP: "))    
    if entered == otp:        
        print("OTP verified successfully!")        
        break    
    else:        
        print("Incorrect OTP.")

else:    
    print("Too many incorrect attempts.")
    print(f"The correct OTP was {otp}")