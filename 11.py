txt = input("Insira o texto: ")
if (len(txt)%2 == 0):
    print("Texto inserido possui ", len(txt), " caracteres [PAR]")
else:
    print("Texto inserido possui ", len(txt), " caracteres [IMPAR]")
