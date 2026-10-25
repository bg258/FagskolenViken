# **Arbeidskrav 1 – Programmering**
I denne oppgaven var hovedmålet mitt å lage et program som gjør det enkelt å finne og lese bibelvers, uten at man trenger å huske alle bible vers.
Programmet skal kjøres i terminalen og lar deg:

- Se gjennom en tabell med 8 forskjellige bibelvers.
- Søke etter et bestemt bibelvers ved å skrive inn en henvisning (for eksempel John 3:16).
- Få et tilfeldig bibelvers fra Bibelen.
- Sammenligne det samme bibelverset ved hjelp av to forskjellige bibel-API-er.

**NB:** Jeg har en IT utdanning fra før og mye av har jeg jobbet med før. Dette er et prosjekt som jeg har jobbet med før som jeg har faktisk klart å ta opp igjen. Jeg har kommentert på koden i engelsk for å gjøre det lettere for Richard å rette og komme med tilbakemeldinger.  

## API-er som er brukt

Programmet mitt henter informasjon fra to forskjellige API-er:

1. **[bible-api.com](https://bible-api.com/)** – henter teksten til bibelvers. Denne API-en krever ingen API-nøkkel.
2. **[API.Bible](https://api.bible/)** – henter bibelvers fra en annen engelsk bibeloversettelse. Denne API-en krever en egen API-nøkkel.

API-nøkkelen til API.Bible blir hentet fra en lokal `.env`-fil i stedet for å bli skrevet direkte i Python-koden. I mitt tilfelle er GitHub-repositoriet privat, så nøkkelen er ikke offentlig tilgjengelig.

## Hvordan kjører jeg programmet?

For å kunne kjøre programmet trenger vi:

- Python 3.10 eller nyere
- Internettforbindelse
- En egen API-nøkkel fra API.Bible (i dette tilfellet trenger du ikke å skaffe en, siden jeg allerede har lagt inn min egen nøkkel)

**Fremgangsmåte**

1. Last ned prosjektet fra GitHub og åpne mappen i VS Code (eller en annen kodeeditor).

2. Åpne terminalen i prosjektmappen og kjør følgende kommando for å installere pakkene som trengs:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Gå til [api.bible](https://api.bible/), opprett en konto og skaff deg en API-nøkkel.

4. Opprett en fil som heter `.env` i samme mappe som `main.py`, og legg inn følgende linje:

   ```env
   API_BIBLE_KEY=OcmdrFRICnENxcWh3IjgD

   ```

5. Start programmet:

   ```bash
   python3 main.py
   ```

**NB:** Du trenger egentlig bare å installere pakkene fra `requirements.txt` og kjøre `main.py`, siden jeg allerede har inkludert min egen API-nøkkel.

---

Når programmet starter, får du opp en meny der du kan velge mellom forskjellige funksjoner.

For å sjekke at **begge API-ene** fungerer, kan du velge alternativ **(4)** og skrive inn `John 3:16`. Dette alternativet lar deg sammenligne ett bibelvers om gangen.

Prøv gjerne de forskjellige alternativene for å lære mer om Jesus og Bibelen.
