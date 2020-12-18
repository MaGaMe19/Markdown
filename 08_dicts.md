# Dictionairies

Wir können Dictionairies brauchen um Daten mithilfe von _**key**-**value**-Paaren_ zu speichern. Man kürzt sie oft mit _dict_ ab.  
Der Name kommt _dictionary_ bedeutet auf deutsch **Lexikon** bzw. **Nachschlagewerk**, was genau der Sinn der dictionaries in Python ist.

---

## Grundsyntax:

```Python
dictionary = {
    key: value,
    ...
}
```

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
    1: "Element 1",
    2: "Element 2",
}
```

Zahlen könnte man für eine nummerierte Liste verwenden: 

```Python
for i, j in zutaten.items():
    print(f"{i}. {j}")
```