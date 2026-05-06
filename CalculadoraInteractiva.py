#Definim les variables

num1=float(input("Insereix el primer numero:"))
num2=float(input("Insereix el segon numero:"))
operadors=input("Insereix operador (+,-,*,/):")

#Creem el bucle que fara que si posa un operador que no es correcte sortira la pregunta una altra vegada

while operadors != "+" and operadors != "-" and operadors != "*" and operadors != "/":
    print("Operador incorrecte!")
    operadors=input("Insereix operador (+,-,*,/):")
    
if operadors == "+":
    operacio=num1+num2
    
elif operadors == "-":
    operacio=num1-num2
   
elif operadors == "*":
    operacio=num1*num2     
    
elif operadors == "/":
    operacio=num1/num2

#Mostrem la solució

print(f"Resultat:{operacio}")
