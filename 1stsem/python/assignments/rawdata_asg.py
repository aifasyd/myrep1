raw_data = """ naveen KUMAR
naveen.kumar@COMPANY.com
+91-98765-43210
"""

lines = raw_data.strip().split("\n")
raw_name  = lines[0].strip()
raw_email = lines[1].strip()
raw_phone = lines[2].strip()

# Clean the name
name = raw_name.title()
words = name.split()
initials = words[0][0] + words[1][0]

# Clean the email
email = raw_email.lower()
domain = email.split("@")[1]

# Clean the phone number and mask all but the last 4 digits
digits = raw_phone.replace("+", "").replace("-", "")
masked_phone = "*" * (len(digits) - 4) + digits[-4:]

# Check if the email looks valid (basic check, no regex)
is_valid = "@" in email and "." in email.split("@")[1]

print("Name     :", name)
print("Initials :", initials)
print("Email    :", email)
print("Domain   :", domain)
print("Phone    :", masked_phone)
print("Valid    :", is_valid)