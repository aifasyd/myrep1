wish='good morning' #single line string
greeting="helllo" #single line string
intro='''my name is aifa. 
nice to meet you'''  #multi-line string

print(greeting)
print(wish)
print(intro)


#indexing

print(wish[0])
print(wish[1])
print(wish[2])
print(wish[3])
print(wish[5])
print(wish[6])
print(wish[7])
print(wish[8])
print(wish[9])
print(wish[10])
print(wish[11])

print("  ")
print(wish[-1])      
print(wish[-2])
print(wish[-3])
print(wish[-4])
print(wish[-5])
print(wish[-6])
print(wish[-7])
print(wish[-9])
print(wish[-10])
print(wish[-11])
print(wish[-12])

#slicing

print(" ")
print(wish[0:11])
print(wish[5:])
print(wish[::2])
print(wish[::-1])

#built in

print("")  # prints an empty line (just for spacing)

print(len(wish))
print(wish.upper())        # converts entire string to UPPERCASE
print(wish.lower())        # converts entire string to lowercase
print(wish.title())        # capitalizes the First Letter Of Each Word
print(wish.capitalize())   # capitalizes only the first letter of the whole string, rest lowercase

# Whitespace
print(wish.strip())    # removes leading & trailing spaces (not the ones in the middle)
print(wish.lstrip())   # removes only leading (left-side) spaces
print(wish.rstrip())   # removes only trailing (right-side) spaces

# Searching
print(wish.find("good"))       # returns the index where "good" starts, or -1 if not found (case-sensitive!)
print(wish.count("o"))         # counts how many times "o" appears in the string
print(wish.startswith("g"))    # checks if string starts with "g" -> True/False (case-sensitive)
print(wish.endswith("  "))     # checks if string ends with two spaces -> True/False
print("ood" in wish)        # checks if "python" exists anywhere inside wish -> True/False

# Splitting & joining
print(wish.split())    # splits string into a list of words, breaking at whitespace

# Replacing
print(wish.replace("good", "bad"))   # replaces all occurrences of "good" with "bad" (case-sensitive, so won't match "Good")

# Checking content
print(wish.strip().isalpha())   # checks if string has ONLY letters (no spaces/numbers/punctuation) -> False here because of spaces/commas
print(wish.strip().islower())   # checks if all letters in string are lowercase -> False here because "Good" starts with capital G

# Formatting
name = "Alex"
print(f"{name} wishes: {wish.strip()}")   # f-string: inserts variable values directly into the string

print(wish.strip().ljust(30, '.'))   # left-justifies string in a field of 30 chars, filling extra space with '.'