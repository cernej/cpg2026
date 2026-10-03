def faktorial(x):
    # Vypocet faktorialu x! = x * (x-1) * (x-2) * ... * 1
    if x == 1:
        return 1
    vysledek = x * faktorial(x - 1)
    return vysledek

if __name__ == "__main__":
    vysledek = faktorial(10)
    print(vysledek)