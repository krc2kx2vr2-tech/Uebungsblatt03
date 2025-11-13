#B) Noten Auswertung
noten = [1.7, 5.0, 2.3, 4.0, 3.3, 2.0, 3.7]
#Durchschnittsnote berechnen
durchschnitt = sum(noten) / len(noten)
#Beste und schlechteste Note finden
beste_note = min(noten)
schlechteste_note = max(noten)
#Ausgabe der Ergebnisse
print(f"Durchschnittsnote: {durchschnitt:.2f}")
print(f"Beste Note: {beste_note:.2f}")
print(f"Schlechteste Note: {schlechteste_note:.2f}")

#Durchschnittsnote auswerten (<2.0 "Gute Leistungen!", sonst: "Da ist noch Luft nach oben")
if durchschnitt < 2.0:
    print("Gute Leistungen!")
else:
    print("Da ist noch Luft nach oben")
