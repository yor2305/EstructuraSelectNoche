# estructura simple

a = 33
b = 200

if b > a:
    print(b, "es mayor que", a)

# condicional doble

if a > b:
    print(b, "es mayor que", a)
else:
    print(b, "no es mayor que", a)

# condicion multiplke
c = 200
d = 207

if a > b:
    print(c, "es mayor que", d)
elif a < b:
    print(c, "es menor que", d)
else:
    print(c, "es igual que", d)

# condiciones
X = 28

if X > 20:
    print("por encima de diez")
    if X > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20")

print("Estudia los sabados", end=' ')
print("es genial")

# print("estudiar los sabados")
# print("es genial")

print("daniela", "luis", "carlos", "camila")  # Agrega un espacio por defecto
print("daniela", "luis", "carlos", "camila", sep="")  # quita el espacio
print("daniela", "luis", "carlos", "camila", sep=",")  # Agrega una coma
print("daniela", "luis", "carlos", "camila", sep="_", end="curso_python")  # implementacion end y sep



