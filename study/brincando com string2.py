curso = "paralelepipedo" 

print("-".join(curso))
print(" ".count(" "))  # Example: count spaces in a string
print(curso.replace("a", "4"))



nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "     Olá mundo  !     " 

print (texto)
print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")


menu = "python;java;c;js;html;css"

print(menu.split(";"))
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(30, "#"))


for letra in menu:
    print(letra, end="|")
print()