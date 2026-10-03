def secti(a, b, c):
    # funkce secte 3 cisla a, b, c a vrati vysledek pomoci return
    vysledek = a + b + c
    return vysledek

def je_delitelne_3(x):
    zbytek = x % 3
    if zbytek == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    x = je_delitelne_3(5)
    print("Je delitelne:", x)
    #x = secti(1, 2, 3)
    #print("Vysledek:", x)