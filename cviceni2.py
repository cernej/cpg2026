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
    # pridejte klic "prumer"
    znamky = data["znamky"]
    prumer = sum(znamky) / len(znamky)
    prumer = round(prumer, 1)
    data["prumer"] = prumer
    # data["prumer"] = round(sum(data["znamky"]) / len(data["znamky"]), 1)
    print(data)
    # {"jmeno": "Vlada", "vek": 44, "znamky": [1, 2, 3, 1, 2, 1, 1, 1], "prumer": 1.5}