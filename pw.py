import random 
import string 

def generate_passsowrd(length=12):
  if length < 8:
    print("password lenght should be at least 8 X)") 
    return None 
    
  low = string.ascii_lowercase 
  up = string.ascii_uppercase 
  digits = string.digits
  symbols = string.punctuation 

  all_carc = up + low + digits + symbols

  password = [ 
    random.choice(low),
    random.choice(up),
    random.choice(digits),
    random.choice(symbols),
    random.choice(symbols),
    ]
    
  password += random.choices(all_carc, k=length - len(password)) 
  random.shuffle(password)
  return ''.join(password) 
  
if __name__ == "__main__":
    try:
       length = int(input("enter desired password length (minimum 8 ): "))
       password = generate_passsowrd(length)
       if password :
          print(f"password : {password}")
    except ValueError:
          print("Please enter a valid lenght")
