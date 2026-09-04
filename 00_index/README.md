# Flervariabelanalys HT 2026

## Kursfakta

- **Kurskod:** MATB21 / ÄMAD02 -- Analysis in Several Variables 1
- **Omfattning:** 7,5 hp, halvfart, första halvan av HT 2026
- **Lärosäte:** Lunds universitet, Matematikcentrum
- **Undervisningsspråk:** engelska
- **Canvas-kurs:** id 42188
- **Föreläsare:** Marcus Carlsson (marcus.carlsson@math.lu.se, Matematik NF,
  plan 5, rum 508A)
- **Seminarier:** Marcus Carlsson, Giang To, Théo Belin
- **Programmeringsprojekt:** Valentina Schüller, Carlos Santillan-Moreno

## Kurslitteratur

- **Huvudbok:** R.A. Adams, C. Essex, *Calculus: A Complete Course*, **10:e
  uppl.**, Pearson Canada, 2021 (ISBN 9780135732588)
- **Bredvidläsning:** Spivak, *Calculus*, 3rd ed.

> Studentens PDF av kursboken är av **9:e upplagan**. Se `CLAUDE.md` och
> `01_kursmaterial/kapitelguide.md` för hur sektionsnumren mappar mellan
> upplagorna -- det gäller framför allt kapitel 12 och uppåt, som är
> förskjutna ett steg (10:e uppl. kap N = 9:e uppl. kap N−1, N ≥ 12).

## Kursinnehåll

Enligt kursplanen: funktioner av flera variabler, kontinuitet och
grundläggande topologi i R^n, differentialkalkyl (partiella derivator,
differentierbarhet, kedjeregeln, gradient, riktningsderivata, Taylors formel,
extremvärden) och integralkalkyl (multipelintegraler, variabelbyte, derivering
under integraltecken, generaliserade integraler).

## Examination

| Del | Hp | Betyg |
|---|---|---|
| Skriftlig tentamen | 6 | U/G/VG |
| Programmeringsprojekt (grupparbete) | 1,5 | U/G |

- Tentan har 6 uppgifter à 0-5 poäng. **15/30 poäng** krävs för godkänt.
- **VG** kräver ≥75 % på tentan **och** godkänt programmeringsprojekt.
- Godkänd kurs kräver godkänd tentamen och godkänt programmeringsprojekt.

## Viktiga datum

| Datum | Vad |
|---|---|
| 1 sep 2026 | Kursstart, F1 |
| 23 okt 2026, 17:00 | **Deadline programmeringsprojekt** |
| ca 9 okt -- 23 okt 2026 | Anmälan till tentamen öppen i Ladok |
| **30 okt 2026, 14:00-19:00** | **Ordinarie tentamen, Sparta** |
| **28 nov 2026, 08:00-13:00** | **Omtentamen, sal 309A/309B, Matematikhuset** |

Programmeringsprojektets grupper väljs i Canvas under People →
Programming Project -- skapa inga egna grupper.
Canvas-uppgift: https://canvas.education.lu.se/courses/42188/assignments/299463

## Mappstruktur

| Mapp | Innehåll |
|---|---|
| `00_index/` | Denna översikt + `uppgiftsindex.md` för att slå upp uppgifter |
| `01_kursmaterial/` | Kapitelguide, renskriven kursplan, övningsblad |
| `02_forelasningar/` | Föreläsningsschema med länkar till fulltext per sektion |
| `03_inlamningar/` | Ev. inlämningar (t.ex. programmeringsprojektet) |
| `04_studieplan/` | Vecka-för-vecka-plan fram till tentan |
| `05_tentor/skarpa_tentor/` | Gamla tentor |
| `05_tentor/losningsforslag/` | Lösningsförslag till gamla tentor |
| `06_bokinnehall/` | Ev. kortare kapitelsammanfattningar |
| `07_fulltext/kap_X/` | Fullständiga studieanteckningar per sektion (kursens 10:e uppl.-numrering), med `[sid NN]`-markörer till 9:e upplagans sidor och `### Uppgift N`-headings |
| `scripts/` | Extraktionsskript och `section_map.json` (upplagemappning + sidintervall) |

## Arbetsflöde

1. Se vad som är på tur i `01_kursmaterial/kursplan_canvas.md` eller
   `02_forelasningar/README.md`.
2. Läs teorin i `07_fulltext/kap_X/X.Y.md` för aktuell sektion.
3. Räkna rekommenderade uppgifter -- hitta dem direkt via
   `07_fulltext/kap_X/X.Y.md#uppgift-N` eller slå upp spann i
   `00_index/uppgiftsindex.md`.
4. Följ `04_studieplan/veckoplan.md` för att ligga i fas fram till tentan
   30 oktober.
5. Inför tentan: räkna gamla tentor i `05_tentor/skarpa_tentor/` och jämför
   med `05_tentor/losningsforslag/`.
6. PDF:er av kursboken och gamla tentor sparas lokalt men gitignoras --
   textversionerna i `07_fulltext/` är det som trackas och som Claude läser.

## Använda repot som Claude-projekt

Det här repot kan kopplas till ett **projekt** på claude.ai så att Claude får
tillgång till hela kursmaterialet i varje konversation:

1. Skapa (eller öppna) ett projekt på claude.ai.
2. Gå till **Projekt → Lägg till kunskap → GitHub** och koppla detta repo
   (`Flervariabelanalys_ht26`).
3. Öppna **Projektinstruktioner** och klistra in texten nedan -- det är en
   kort version av `CLAUDE.md` som ger Claude de viktigaste reglerna direkt,
   utan att behöva läsa hela filträdet varje gång.

Klistra in i projektinstruktionerna:

> Det här projektet innehåller kursmaterial för MATB21/ÄMAD02
> Flervariabelanalys 1, Lunds universitet. Kursboken är Adams & Essex,
> *Calculus: A Complete Course*, **10:e upplagan**. Fulltexten i
> `07_fulltext/kap_X/X.Y.md` är dock hämtad ur **9:e upplagan** av samma bok --
> filerna är namngivna efter kursens (10:e uppl.) sektionsnummer, men
> `[sid NN]`-markörerna i texten refererar till 9:e upplagans sidor. För kapitel
> 12 och uppåt är kapitelnumren förskjutna ett steg: 10:e uppl. kapitel N = 9:e
> uppl. kapitel N−1. Ange alltid båda sektionsnumren när du refererar till teori
> (t.ex. "13.5 i 10:e uppl. = 12.5 i 9:e uppl."). Full mappningstabell finns i
> `scripts/section_map.json` och `CLAUDE.md`. När jag skickar en övningsuppgift:
> slå upp rätt sektion, läs teorin i motsvarande `07_fulltext`-fil, och visa
> fullständiga lösningssteg -- inte bara svaret, eftersom kursen examinerar
> matematisk kommunikation. Uppgifter kan slås upp direkt via
> `07_fulltext/kap_X/X.Y.md#uppgift-N` eller via tabellen i
> `00_index/uppgiftsindex.md`.
