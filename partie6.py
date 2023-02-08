
def cc():
    f = open(r"C:\Users\Lenovo\Desktop\compte.txt", "a")
    idc = int(dernier()) + 1
    dp = input("donner l'identifiant du prop:")
    solde = input("donner le solde:")
    d = date()
    b = ['True', 'False']
    while 1:
        typee = input("donner le type:(True/False)")
        if typee in b: break
    ligne = str(idc) + ";" + dp + ";" + str(solde) + ";" + d + ";" + typee + "\n"
    f.write(ligne)
    f.close()
