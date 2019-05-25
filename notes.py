# Manipulating Text

# 1. var[i:f:j] once printed will output the string from the character of position i to the character of position f-1, jumping "j" times from one position to another. If i is ommited, python will use the character of position 0 as the initial. If the j is ommited python will use the character of the last position + 1 as the final. If j is ommited, python will understand as you are jumping from one character to the very next one. Examples:

var = 'Physics Rocks' # [P(0) h(1) y(2) s(3) i(4) c(5) s(6) (7) R(8) o(9) c(10) k(11) s(12)]
print(var) #output == Physics
print(var[2]) #output == y
print(var[3:9]) #output == sics R
print(var[:12:2]) #output == PyisRc

# 2. len(var) once printed will output how many characters there are in a string associated to a variable. Example:

var = 'Mathematics Rocks' # [M(0) ... s(16)] as there are characters from 0 to 16, the total amount of characters is 17.
print(len(var)) # output == 17

# 3. var.count('x',i,f) once printed will output how many times x appeared between the interval of the character of position i to the character of position f-1. If the output is -1, what python means is that there's no such x in the string. Example:

var = 'Astrophysics Rocks' # [A(0) ... s(17)] 
print(var.count('o')) # output == 2
print(var.count('o',8,17)) # output == 1

# 4. var.find('x') once printed will output which position x starts in the interval of the sequence of characters of the string associated to the variable var. If the output is -1, what python means is that there's no such x in the string. Example:

var = 'Hawking Radiation' # [H(0) ... n(16)]
print(var.find('Ball')) # output == -1
print(var.find('Rad')) # output == 8

# 5. 'x' in var once printed will output True or False depending if x appears in the string associated to the variable var. Example:

var = 'Black Hole' 
print('Black' in var) # output == True

# 6. var.replace('x','y') once printed will output almost the same string associated to the variable var, the unique difference is that where is 'x' now is 'y', x is indeed being replaced. Example:

var = 'Derivatives Rocks!'
print(var.replace('Derivatives','Integrals')) # output == Integrals Rocks!

# 7. var.upper() once printed will output the same string but now with all characters in uppercase format. var.lower() once printed will output the same string but now with all characters in lowercase format. var.capitalize() once printed will output the same string but now with only the first character of the string in uppercase format and all the others characters in lowercase format. var.title() once printed will output the same string but now with every first character of each word being in uppercase format and all the others characters being in lowercase format. Examples:

var = 'Sir McDonald had a farm'
print(var.upper()) # output == SIR MCDONALD HAD A FARM
print(var.lower()) # output == sir mcdonald had a farm
print(var.capitalize()) # output == Sir mcdonald had a farm
print(var.title()) # output == Sir Mcdonald Had A Farm

# 8. var.strip() once printed will output the associated string without possible additional blank spaces at the left end and the right end of the string. var.lstrip() just removes the additional blank spaces from the left end and var.rstrip() just removes the additional blank spaces from the right end. Examples:

var = '[blankspace][blankspace][blankspace]Awful example[blankspace][blankspace]'
print(var.strip()) # output == 'Awful example'
print(var.lstrip()) # output == 'Awful example[blankspace][blankspace]
print(var.rstrip()) # output == '[blankspace][blankspace][blankspace]Awful example'

# 9. var.split() this manipulation will divide a list of characters into a new list with n+1 number of characters, each one being actually a lists of characters where n is the number of blank spaces between two characters of the first list. Example:

var = 'Python is great' # [P(0) y(1) t(2) h(3) o(4) n(5) (6) i(7) s(8) (9) g(10) r(11) e(12) a(13) t(14)]
var.split() # that will generate a new list: [(Python)(0) (is)(1) (great)(2)]

# 10. 'x'.join(var) once printed will output the associated string but between every two consecutive characters there'll be an x. Example:

var = 'Ohmygod'
print('-'.join(var)) # output == O-h-m-y-g-o-d




