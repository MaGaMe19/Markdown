# Dictionairies

Wir können Dictionairies brauchen um Daten mithilfe von _**key**-**value**-Paaren_ zu speichern. Man kürzt sie oft mit _dict_ ab.  
Der Name kommt _dictionary_ bedeutet auf deutsch **Lexikon** bzw. **Nachschlagewerk**, was genau der Sinn der dictionaries in Python ist.  
Alle Code-Beispiele dieses Markdown-Dokuments sind in der datei [examples.py](https://github.com/MaGaMe19/Markdown/dicts/examples.py) zu finden.

---

## Grundsyntax:

```Python
dictionary = {
    key: value,
    ...
}
```  

###### Kein tatsächlich ausführbarer python code, nur zur Darstellung.

&nbsp;  

## Mögliche Datentypen als Key:

### Strings:

```Python
steckbrief = {
    "Vorname": "Klaus",
    "Nachname": "Müller",
    "Wohnort": "Zürich",
}
```

Strings werden am häufigsten als Keys verwendet, da sie vielseitig einsetzbar sind.  
&nbsp;  

### Zahlen:

```Python
zutaten = {
    1: "Mehl",
    2: "Eier",
    3: "Zucker",
}
```

Zahlen könnte man z.B. für eine nummerierte Liste verwenden: 

```Python
for i, j in zutaten.items():
    print(f"{i}. {j}")

>>>
 1. Mehl
 2. Eier
 3. Zucker
```

&nbsp;  

## Mögliche Datentypen als Value:
