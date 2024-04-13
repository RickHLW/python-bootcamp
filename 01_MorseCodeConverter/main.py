

morsecode = {"A":".-", "B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",
             "M":"--","N":"-.","O":"---", "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
             "1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"
             }

instring = input("Input a string need converted to Morse Code:")

print(f"{instring}")
outstring = ""
instring = instring.upper()
for c in instring:
    if c != " ":
        outstring = outstring + morsecode[c] + " "

print(f"{outstring}")