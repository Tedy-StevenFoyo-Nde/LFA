# 0 und 1 beginnen mit der Reihe
from collections import Counter

def analyze_frequency(ciphertext):
    letter_counts = Counter(ciphertext)
    return letter_counts

#ciphertex = "VwJ ywzwAEFAKNGDDw XJwEvw KuzJALL vMJuz vAw vMFCDwF YsKKwF vwJ kLsvL.VwJ eGFv zAFy LAwx sE ZAEEwD, KwAF xszDwK dAuzL OsJx ywKHwFKLAKuzw kuzsLLwF sMx vAw sDLwF YwEäMwJ.VAw kLADDw OMJvw FMJ NGE DwAKwF cDsHHwJF vwJ kuzJALLw vwK XJwEvwF vMJuztJGuzwF.aF KwAFwJ ZsFv zAwDL wJ wAFwF sDLwF, NwJyADtLwF TJAwxMEKuzDsy.kwAFw SMywF zMKuzLwF FwJNöK NGF wAFwJ vMFCDwF WuCw RMJ FäuzKLwF, sDK wJ KAuz vwE NwJwAFtsJLwF lJwxxHMFCL FäzwJLw. WAF ZsMuz NGF SFyKL Dsy AF vwJ dMxL, OäzJwFv wJ KAuz vwE MFtwCsFFLwF kuzAuCKsD wFLywywF twOwyLw."
with open('C:/Users/steve/Downloads/Aufgabe1.txt', 'r', encoding='utf-8') as file:
    ciphertext = file.read().lower()
letter_counts = analyze_frequency(ciphertext)
letter_counts.pop(' ')
print(letter_counts)

#sortieren von letter_counts
sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

#erzeugung einer Liste mit sortierten Keys
list1= [item[0] for item in sorted_counts]

#liste von deutschem Alphabet sortiert
list2 = ['e', 'n', 's', 'r', 'i', 'a', 't', 'd', 'h', 'u', 'l', 'g', 'c', 'm', 'w', 'b', 'f', 'k', 'z', 'ü', 'v', 'p', 'ä', 'ö', 'ß', 'j', 'y']

replaced_chars = [] #array für die schon ersetzenen Buchstaben
for i in range(0, 4):
    if list1[i] not in replaced_chars:
        print(i , list1[i], list2[i])
        ciphertext = ciphertext.replace(list1[i], list2[i])
        replaced_chars.append(list2[i])
print(ciphertext)
print("testons voir si ca marche")