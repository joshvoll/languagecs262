#Specifying Tokens

# Write code for the LANGLESLASH token to match </ in our HTML.
def t_LANGLESLASH(token):
	r'</'
	return token

def t_NUMBER(token):
    r"[0-9]"
    token.value = int(token.value)
    return token

# Quoted Strings

# Suppose a string starts with " and ends with " and contains any number of
# characters except ". Write a definition for t_STRING.

# Match Exactly:
#     "cuneiform"
#     "sumerian writing"
# Do Not Match Exactly:
#     "esc \" ape"
# 
def t_STRING(token):
    r'"[^"]*"'
    return token

def t_WORD(token):
    r"[^ <> \n]+"
    return token
