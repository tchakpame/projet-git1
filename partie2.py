

def rec(x):
    f = open(r"C:\Users\Lenovo\Desktop\compte.txt", "r")
    d = {}
    for ligne in f:
        l = ligne.split(";")
        if l[0].strip() == x:
            d['idProp'] = l[1]
            d['solde'] = l[2]
            d['Dte'] = l[3]
            d['Type'] = l[4]
            return d
        else:
            return "Compte n'existe pas"
    f.close()



