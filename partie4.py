


def sp():
    f = open(r"C:\Users\Lenovo\Desktop\prop.txt", "a")
    idp = input("donner l'identifiant du prop:")
    nom = input("donner le nom du prop:")
    cin = input("donner le numéro cin du prop:")
    tel = input("donner le num du tel du prop:")
    ad = input("donner l'adresse du prop:")
    ligne = idp + ";" + nom + ";" + cin + ";" + tel + ";" + ad + "\n"
    f.write(ligne)
    f.close()
    return ligne



