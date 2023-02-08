


def dernier():
    f = open(r"C:\Users\Lenovo\Desktop\compte.txt", "r")
    lignes = f.readlines()
    # print(len(lignes))
    if (len(lignes)) == 0:
        print("fichier vide")
    else:
        last_line = lignes[-1].split(";")
    f.close()
    return last_line[0]



