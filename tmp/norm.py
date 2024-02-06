import unicodedata
a = unicodedata.normalize('NFC', 'Bokm�ål')
print(a)
a = unicodedata.normalize('NFD', 'Bokmäl')
print(a, end = "")
