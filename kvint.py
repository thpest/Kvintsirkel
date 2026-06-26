def kvintsirkel_akkorder(toneart, modus="dur"):
    # Kvintsirkelen med dur- og moll-tonearter
    kvintsirkel = [
        ("C", "A-moll"),
        ("G", "E-moll"),
        ("D", "B-moll"),
        ("A", "F#m"),
        ("E", "C#m"),
        ("B", "G#m"),
        ("F#", "D#m"),
        ("Db", "Bbm"),
        ("Ab", "Fm"),
        ("Eb", "Cm"),
        ("Bb", "Gm"),
        ("F", "Dm")
    ]

    # Akkordtyper for ulike moduser
    akkordtyper = {
        "dur": (["I", "ii", "iii", "IV", "V", "vi", "vii°"], ["dur", "moll", "moll", "dur", "dur", "moll", "dim"]),
        "moll": (["i", "ii°", "III", "iv", "v", "VI", "VII"], ["moll", "dim", "dur", "moll", "moll", "dur", "dur"]),
        "harmonisk moll": (["i", "ii°", "III+", "iv", "V", "VI", "vii°"], ["moll", "dim", "aug", "moll", "dur", "dur", "dim"]),
        "dorisk": (["i", "ii", "III", "IV", "v", "vi°", "VII"], ["moll", "moll", "dur", "dur", "moll", "dim", "dur"])
    }

    if modus not in akkordtyper:
        return "Modus må være 'dur', 'moll', 'harmonisk moll' eller 'dorisk'."

    skala_trinn, akkordtype = akkordtyper[modus]

    # Finn indeks for den valgte tonearten
    for i, (dur, moll) in enumerate(kvintsirkel):
        if (modus in ["dur", "harmonisk moll", "dorisk"] and dur == toneart) or (modus == "moll" and moll == toneart):
            # Lag akkorder i skalaen
            akkorder = []
            for trinn, type_akkord in zip(skala_trinn, akkordtype):
                akkord_index = (i + skala_trinn.index(trinn)) % 12
                rot_tone = kvintsirkel[akkord_index][0 if type_akkord in ["dur", "dim", "aug"] else 1]
                akkorder.append((trinn, f"{rot_tone}{'' if type_akkord == 'dur' else ('m' if type_akkord == 'moll' else '°' if type_akkord == 'dim' else '+')}"))
            return akkorder

    return "Tonearten ble ikke funnet i kvintsirkelen."


def foresla_modulasjoner(toneart, modus="dur"):
    # Modulasjoner skjer ofte til nærliggende tonearter i kvintsirkelen
    kvintsirkel_dur = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]
    index = kvintsirkel_dur.index(toneart) if toneart in kvintsirkel_dur else -1

    if index == -1:
        return "Tonearten ble ikke funnet for modulasjoner."

    # Nærliggende tonearter
    modulasjoner = [
        kvintsirkel_dur[(index - 1) % 12],  # En kvint ned
        toneart,  # Grunntone
        kvintsirkel_dur[(index + 1) % 12]   # En kvint opp
    ]
    return modulasjoner


# Hovedfunksjon med GUI (Tkinter)
def gui_program():
    import tkinter as tk
    from tkinter import ttk

    def oppdater_resultat():
        toneart = toneart_var.get()
        modus = modus_var.get()
        akkorder = kvintsirkel_akkorder(toneart, modus)
        if isinstance(akkorder, list):
            resultat.set("\n".join([f"{trinn}: {akkord}" for trinn, akkord in akkorder]))
            modulasjoner = foresla_modulasjoner(toneart, modus)
            modulasjon_var.set(f"Mulige modulasjoner: {', '.join(modulasjoner)}")
        else:
            resultat.set(akkorder)
            modulasjon_var.set("")

    # Opprett vindu
    root = tk.Tk()
    root.title("Kvintsirkel og modulasjoner")

    # Inndatafelt
    ttk.Label(root, text="Velg toneart:").grid(row=0, column=0, padx=10, pady=10)
    toneart_var = tk.StringVar(value="C")
    ttk.Entry(root, textvariable=toneart_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="Velg modus:").grid(row=1, column=0, padx=10, pady=10)
    modus_var = tk.StringVar(value="dur")
    ttk.Combobox(root, textvariable=modus_var, values=["dur", "moll", "harmonisk moll", "dorisk"]).grid(row=1, column=1, padx=10, pady=10)

    # Resultatfelt
    resultat = tk.StringVar()
    ttk.Label(root, text="Akkorder:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Label(root, textvariable=resultat, wraplength=400, justify="left").grid(row=2, column=1, padx=10, pady=10)

    modulasjon_var = tk.StringVar()
    ttk.Label(root, textvariable=modulasjon_var, wraplength=400, justify="left", foreground="blue").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Kjør-knapp
    ttk.Button(root, text="Vis akkorder", command=oppdater_resultat).grid(row=4, column=0, columnspan=2, pady=20)

    root.mainloop()


# Start programmet
if __name__ == "__main__":
    gui_program()
