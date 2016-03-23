
def dodawanie(a,b):
    return a+b

def get_info():
    return "to jest program kalkulator stworzony przez Michala"

try:
    a = int(input('podaj pierwsza liczbe: '))
    b = int(input('podaj druga liczbe: '))
    print(dodawanie(a,b))

except ValueError as ve:
    print("wprowadzono bledne dane, koncze dzialanie...")

print (get_info())
dodawanie(a,b)
input()