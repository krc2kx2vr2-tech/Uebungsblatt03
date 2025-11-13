#B) Noten Auswertung
noten = [1.7, 5.0, 2.3, 4.0, 3.3, 2.0, 3.7]

def sortiere_noten(noten_liste):

    return sorted(noten_liste)


noten_sorted = sortiere_noten(noten)


def berechne_median_sortiert(sortierte_liste):
    n = len(sortierte_liste)
    if n % 2 == 1:
        # ungerade Anzahl → mittleres Element
        return sortierte_liste[n // 2]
    else:
        # gerade Anzahl → Mittelwert der beiden mittleren Elemente
        return (sortierte_liste[n // 2 - 1] + sortierte_liste[n // 2]) / 2

median = berechne_median_sortiert(noten_sorted)
#Durchschnittsnote berechnen
durchschnitt = sum(noten) / len(noten)
#Beste und schlechteste Note finden
beste_note = min(noten)
schlechteste_note = max(noten)
#Ausgabe der Ergebnisse
print(f"Durchschnittsnote: {durchschnitt:.2f}")
print(f"Beste Note: {beste_note:.2f}")
print(f"Schlechteste Note: {schlechteste_note:.2f}")
print(f"Noten sortiert: {noten_sorted}")
print(f"Median: {median:.2f}")

#Durchschnittsnote auswerten (<2.0 "Gute Leistungen!", sonst: "Da ist noch Luft nach oben")
if durchschnitt < 2.0:
    print("Gute Leistungen!")
else:
    print("Da ist noch Luft nach oben")
