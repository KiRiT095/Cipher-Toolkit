while True :
    try:
       password=int(input("Enter your password \n Allowed characters : 0-9\n\t"))
       break
    except:
        print("try again with only numeric values\n\t")

while True :

  encryption=input("Enter the kind of encryption you wanna make in (Binary, Octal, Hexadecimal) : \n\t").lower()

  if encryption=="hexadecimal" :
   print(hex(password)[2:])  
   break
  
  elif encryption =="binary" :
    print(bin(password)[2:])
    break
  
  elif encryption=="octal":
    print(oct(password)[2:])
    break
  
  else :
    print("Invalid encryption type")