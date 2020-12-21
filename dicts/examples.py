# Beispiel zum Zugriff auf Values:
beispiel = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

ausgabe = beispiel["key2"]
print(ausgabe) # Man erhält "value2".


# Beispiele zum Bearbeiten des Dictionairies:
beispiel["key2"] = "newValue2"
print(beispiel["key2"]) # Man erhält nun "newValue2".

beispiel["key4"] = "gugus" # der key "key4" wird mit dem wert "gugus" erstelltt
print(beispiel)  # Man sieht, dass der neue Wert hinzugefügt wurde.


# Beispiel zu Strings als Key:
steckbrief = {
    "vorname": "Klaus",
    "nachname": "Müller",
    "wohnort": "Zürich",
}
print(steckbrief)


# Beispiel zu Zahlen als Key:
zutaten = {
    1: "Mehl",
    2: "Eier",
    3: "Zucker",
}
for i, j in zutaten.items():
    print(f"{i}. {j}")


# Beispiel zu Strings bzw. Zahlen als Value:
charakter = {
    "vorname": "James",
    "nachname": "Bond",
    "alter": 35,
    "gewicht": 75,
}
print(charakter)


# Beispiel zu Booleans bzw. "None" als Value:
spielInfo = {
    "spielGestartet": True,
    "spielGewonnen": False,
    "ausrüstung": None,
}
print(spielInfo)


# Beispiel zu Dictionairies bzw. Listen als Value:
schüler = {
    "Fritz": {
        "klasse": 7,
        "noten": [5.1, 4.5, 5.8],
    },
    "Lisa": {
        "klasse": 8,
        "noten": [4.8, 5.9, 5.6],
    },
}
print(schüler["Fritz"]["noten"][1])