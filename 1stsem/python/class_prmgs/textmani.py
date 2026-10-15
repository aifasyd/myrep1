mystring = ''' cushan KUMAR
           cushan@GMAIL.COM
           +91-1234-5687-11'''

lines = mystring.strip().splitlines() 
name = lines[0].strip().title()                
email = lines[1].strip().lower()        
no = lines[2].strip().replace("+", "").replace("-", "")  

print(f"name:{name}")
print(f"email:{email}")
print(f"no:{no}")




















