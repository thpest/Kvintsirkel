# Kvintsirkelen 🎵

Et interaktivt musikkverktøy i nettleseren – kvintsirkel, diatoniske akkorder, skalaer og lyd. Ingen installasjon: åpne `index.html`, eller bruk den publiserte versjonen via GitHub Pages.

## Funksjoner

- **Klikkbar kvintsirkel** med dur ytterst og relativ moll innerst
- **Fire moduser**: dur, naturlig moll, harmonisk moll og dorisk
- **Diatoniske akkorder** med romertall, akkordnavn og toner
- **Septimakkorder** (av/på) og **arpeggio**-modus
- **Tempo-regulator** for skala og akkordrekke
- **Lyd** via Web Audio API med fire instrumenter: piano, gitar, el-piano og orgel
- **Grep-visning** for hver akkord:
  - Piano-tangenter med grunntone markert
  - Ekte gitargrep (åpne grep + barré, dim7 og aug) med fingersetting
- **Kopier akkorder** som tekst
- Musikalsk korrekt staving (hver bokstav brukes én gang per skala)

## Bruk

Åpne `index.html` i en nettleser. Lyd starter ved første klikk (nettleser-krav). Klikk en akkord eller et felt i sirkelen for å høre den og se grepet.

Opprinnelig laget som et Python/Tkinter-program (`kvint.py`), portet til frittstående HTML/JavaScript.
