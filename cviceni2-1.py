def jaccard_index(mnozina1, mnozina2):
    prunik = len(mnozina1.intersection(mnozina2))
    sjednoceni = len(mnozina1.union(mnozina2))
    jackarduv_index = prunik / sjednoceni
    return jackarduv_index

def levenstein_dist(text1, text2):
    levenstein = 0
    lenght = min(len(text1), len(text2))
    i = 0
    while i < lenght:
        if text1[i] != text2[i]:
            levenstein += 1
        i += 1
    levenstein += abs(len(text1) - len(text2))
    return levenstein

def levnestein_for(text1, text2):
    levenstein = 0
    for i in range(min(len(text1), len(text2))):
        if text1[i] != text2[i]:
            levenstein += 1
    levenstein += abs(len(text1) - len(text2))
    return levenstein

if __name__ == "__main__":

    mnozina1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    mnozina2 = {2, 3, 5, 6, 8, 10}
    jackarduv_index = jaccard_index(mnozina1, mnozina2)
    print(f"Podobnost mnozin je: {jackarduv_index}")

    print(levenstein_dist("seznam", "seznam"))   # 0
    print(levenstein_dist("seznam", "zoznam"))   # 2
    print(levenstein_dist("seznam", "seznamka")) # 2
    print(levenstein_dist("seznamka", "zoznam")) # 4

    print(levnestein_for("seznam", "seznam"))   # 0
    print(levnestein_for("seznam", "zoznam"))   # 2
    print(levnestein_for("seznam", "seznamka")) # 2
    print(levnestein_for("seznamka", "zoznam")) # 4
