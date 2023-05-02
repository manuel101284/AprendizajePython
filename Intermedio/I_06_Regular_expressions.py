### Regular Expressions ###

import re


# match
my_string_01 = "Esta es la lección  número 6: Lección sobre Expresiones regulares"
my_string_02 = "Esta no es la lección sobre manejo de errores"

# Con match se desea comparar una variable con un patrón determinado
match_01 = re.match("Esta es la lección", my_string_01, re.I)
match_02 = re.match("Esta es la lección", my_string_02)
match_03 = re.match("expresiones regulares", my_string_01)

print(match_01)
span_01 = match_01.span() # Muestra la ubicación donde se encuentra la cadena buscada
start_01, end_01 = match_01.span()
print(span_01) 
print(start_01)
print(end_01)
print(my_string_01[start_01:end_01])

match_04 = re.match("Esta no es la lección", my_string_02)
if (match_04 != None):
    print(match_04)
    start_02, end_02 = match_04.span()
    print(start_02)
    print(end_02)

#print(match_02)
#print(match_03)
#print(match_04)


# search
search_01 = re.search("lección", my_string_01, re.I)
print(search_01)
start_03, end_03 = search_01.span()
print(my_string_01[start_03: end_03])


# find
findall_01 = re.findall("lección", my_string_01, re.I)
print(findall_01)


# split
split_01 = re.split(":", my_string_01)
print(split_01)


# sub
sub_01 = re.sub("Expresiones regulares", "RegEx", my_string_01)
print(sub_01)
sub_02 = re.sub("lección|Lección", "LECCIÓN", my_string_01)
print(sub_02)
sub_03 = re.sub("[l|L]ección", "LECCIÓN", my_string_01)
print(sub_03)


# Patterns
# Para aprender más sobre expresiones regulares: https://regex101.com

pattern_01 = r"[l|L]ección"
print(re.findall(pattern_01, my_string_01))

pattern_02 = r"[l|L]ección | Expresiones"
print(re.findall(pattern_02, my_string_01))

pattern_03 = r"[0-9]"
print(re.findall(pattern_03, my_string_01))

pattern_04 = r"\d"
print(re.findall(pattern_04, my_string_01))

pattern_05 = r" "
print(re.findall(pattern_05, my_string_01))

pattern_06 = r"[l]."
print(re.findall(pattern_06, my_string_01))


# email regular expression
email_01 = "manuel101284@gmail.com"
email_02 = "ricardo@ricardo.com"
email_03 = "manuel ricardo . 123@gmail.com"

pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

print(re.match(pattern_email,email_01))
print(re.match(pattern_email,email_02))
print(re.match(pattern_email,email_03))

print(re.search(pattern_email,email_01))
print(re.search(pattern_email,email_02))
print(re.search(pattern_email,email_03))

print(re.findall(pattern_email, email_01))
print(re.findall(pattern_email, email_02))
print(re.findall(pattern_email, email_03))

