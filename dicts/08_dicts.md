# Dictionairies

![Dictionairy](https://www.collinsdictionary.com/images/full/dictionary_168552845.jpg)

###### Quelle: Collin's Dictionary

<br>

Wir können Dictionairies brauchen um Daten mithilfe von _**key**-**value**-Paaren_ zu speichern. Man kürzt sie oft mit _dict_ ab.  
Der Name _dictionary_ bedeutet auf deutsch **Lexikon** bzw. **Nachschlagewerk**, was genau der Sinn der dictionaries in Python ist.  
Alle Code-Beispiele dieses Markdown-Dokuments sind in der datei [examples.py](https://github.com/MaGaMe19/Markdown/blob/master/dicts/examples.py) zu finden.  
<br>

---

## Grundsyntax

```Python
dictionary = {
    key: value,
    ...
} *
```  

###### * Kein tatsächlich ausführbarer python code, nur zur Darstellung.

Wichtig: Ohne Kommas hinter jedem Eintrag funktioniert das Ganze nicht!  
<br>

---

## Grundfuktionen

Verwendetes dictionairy für diese Erklärung:

```Python
beispiel = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
```  
<br>

### Zugriff auf das Dictionairy
```Python
ausgabe = beispiel["key2"]

>>> print(ausgabe)
 value2
```
Das Zugreifen auf Values innerhalb von Dictionairies ist vergleichbar mit dem Zugreifen auf Listen, es werden eckige Klammern verwendet. Anders als bei Listen gibt man jedoch den **namen des Keys** in die eckigen Klammern.  
<br>
Eine andere Methode um die Keys bzw. die Values zu erhalten ist die Verwendung der Funktionen _.keys()_, _.values()_ sowie _.items()_:

```Python
>>> beispiel.keys()
dict_keys(['key1', 'key2', 'key3'])

>>> beispiel.values()
dict_values(['value1', 'value2', 'value3'])

>>> beispiel.items()
dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
```
Die Outputs dieser Funktionen könnte man z.B. mit einem For-Loop darstellen.  
(siehe [Beispiel zu Zahlen als Key](https://github.com/MaGaMe19/Markdown/blob/master/dicts/08_dicts.md#zahlen))  
<br>

### Bearbeiten des Dictionairies

Wir können Werte verändern...
```Python
beispiel["key2"] = "newValue2"

>>> print(beispiel["key2"])
 newValue2
```

...oder auch Werte hinzufügen:

```Python
beispiel["key4"] = "gugus" # der key "key4" wird mit dem wert "gugus" erstellt.

>>> print(beispiel)
 {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'gugus'}
```  
<br>

---

## Häufigste Datentypen als Key

### Strings

```Python
steckbrief = {
    "vorname": "Klaus",
    "nachname": "Müller",
    "wohnort": "Zürich",
}
```

Strings werden am häufigsten als Keys verwendet, da sie vielseitig einsetzbar sind.  
<br>

### Zahlen

```Python
zutaten = {
    1: "Mehl",
    2: "Eier",
    3: "Zucker",
}
```

Zahlen könnte man z.B. für eine nummerierte Liste verwenden: 

```Python
>>> for i, j in zutaten.items():
        print(f"{i}. {j}")

 1. Mehl
 2. Eier
 3. Zucker
```

<br>

---

## Häufigste Datentypen als Value

### Strings und Zahlen

```Python
charakter = {
    "vorname": "James",
    "nachname": "Bond",
    "alter": 35,
    "gewicht": 75,
}
```
Dies ist nützlich wenn man z.B. Einstellungen eines Nutzers speichern möchte, wie beispielsweise den zusammengestellten Spielcharakter in einem Game.  
<br>

### Booleans und "None"

```Python
spielInfo = {
    "spielGestartet": True,
    "spielGewonnen": False,
    "ausrüstung": None,
}
```
Diese Datentypen könnten wiederum in einem Game nützlich sein.  
<br>

### Dictionaries und Listen

```Python
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
```
Das ganze kann jedoch schnell kompliziert werden.  
Um z.B. Fritz' zweite Note zu erhalten, müsste man so vorgehen:

```Python
>>> schüler["Fritz"]["noten"][1]
4.5
```

<br>

---

## Beispiel

_Zeugnis mit Noten_ testing.py

```Python

```