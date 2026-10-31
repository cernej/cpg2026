def prumer(znamky):
    return round( sum(znamky) / len(znamky), 1 )


if __name__ == "__main__":

    sachovnice = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    print(sachovnice[5][1])

    ntice = ("a", "b", "c")
    _, prvek2, _ = ntice
    print(prvek2)

    data = {
        "jmeno": "Vlada",
        "vek": 44,
        "znamky": [1, 2, 3, 1, 2, 1, 1, 2]
    }

    # for k, v in data.items():
    #     print(f"klic je: {k} a hodnota: {v}")

    # pridejte klic "prumer"
    # znamky = data["znamky"]
    # prumer = sum(znamky) / len(znamky)
    # prumer = round(prumer, 1)
    # data["prumer"] = prumer
    # data["prumer"] = round(sum(data["znamky"]) / len(data["znamky"]), 1)
    data["prumer"] = prumer(data["znamky"])
    print(data)
    # {"jmeno": "Vlada", "vek": 44, "znamky": [1, 2, 3, 1, 2, 1, 1, 1], "prumer": 1.5}
    databaze = [
        {"jmeno": "Vlada", "vek": 44, "znamky": [1, 2, 3, 1, 2, 1, 1, 1]},
        {"jmeno": "Jana", "vek": 24, "znamky": [1, 3, 3, 3, 2, 3, 1, 1]}
    ]
    for data in databaze:
        data["prumer"] = prumer(data["znamky"])
    print(databaze)

    mnozina = {1,2,3,3,2,3,4,5,1,2}
    print(mnozina)