# Flervariabelanalys HT 2026 -- Projektkonfiguration för Claude

## Om kursen

MATB21 / ÄMAD02 Analysis in Several Variables 1 (Flervariabelanalys 1), 7,5 hp,
HT 2026, Lunds universitet. Halvfart, första halvan av terminen. Kursen ges på
engelska; detta repo förs på svenska.

Huvudbok: Adams & Essex, *Calculus: A Complete Course*, **10:e uppl.** (2021),
ISBN 9780135732588 (refereras som "A"). Bredvidläsning: Spivak, *Calculus*, 3rd ed.

Föreläsare: Marcus Carlsson (marcus.carlsson@math.lu.se). Seminarier: Marcus
Carlsson, Giang To, Théo Belin. Programmeringsprojekt: Valentina Schüller,
Carlos Santillan-Moreno.

## Upplaga -- LÄS DETTA FÖRST

Kursen följer **10:e upplagan**. Fulltext-extraktionen i `07_fulltext/` är
gjord ur en PDF av **9:e upplagan** -- alla `[sid NN]`-markörer i fulltexten
refererar därför till 9:e upplagans paginering, inte 10:e.

**Filerna är namngivna efter kursens (10:e uppl.) sektionsnummer.** Innehållet
i varje fil är hämtat ur motsvarande sektion i 9:e uppl.

### Kapitelförskjutningen

För flervariabeldelen (kapitel 12 och uppåt i 10:e uppl.) är kapitlen
förskjutna ett steg mot 9:e upplagan:

**10:e uppl. kapitel N = 9:e uppl. kapitel N−1, för N ≥ 12.**

Sektionsnumret inom kapitlet följer med rakt av (10:e 13.5 = 9:e 12.5, samma
sektion "5" men i kapitel 13 respektive 12). Kapitel 9 och 10 är oförändrade
mellan upplagorna (samma nummer i båda).

| 10:e uppl. (kursens numrering, = filnamn) | 9:e uppl. (PDF:ens numrering, = `[sid NN]`) | Innehåll |
|---|---|---|
| 9.8 | 9.8 | Binomialsatsen |
| 10.1, 10.5, 10.6 | samma | R^n, kvadriker, cylinder-/sfäriska koordinater |
| 12.1, 12.3 | 11.1, 11.3 | Vektorfunktioner, kurvor, båglängd |
| 13.1–13.9 | 12.1–12.9 | Partiella derivator, kedjeregel, gradient, implicita funktionssatsen, Taylor |
| 14.1, 14.2, 14.6 | 13.1, 13.2, 13.6 | Extremvärden, restriktioner, derivering under integraltecknet |
| 15.1–15.7 | 14.1–14.7 | Multipelintegraler, variabelbyte, ytintegraler |

**Regel: nämn alltid båda numren när en sektion refereras**, t.ex.
"se sektion 13.5 i 10:e uppl. (= 12.5 i 9:e uppl., boksidorna 703–712)".
Fullständig mappning med sidintervall finns i `scripts/section_map.json`.

Övningsnumreringen inom en sektion är i praktiken identisk mellan upplagorna.
Om en uppgift inte hittas på det förväntade numret, dubbelkolla mot fysiska
10:e-upplagan eller mot kursplanens övningslista i
`01_kursmaterial/kursplan_canvas.md`.

## Kapitel-till-ämne mappning (Adams, kursens 10:e uppl.-numrering)

- **Kap 9 (9.8):** Binomialsatsen -- kombinatorik, binomialkoefficienter, Pascals triangel
- **Kap 10 (10.1, 10.5, 10.6):** Rummet R^n -- punkter, vektorer, avstånd, kvadriska ytor, cylinderkoordinater, sfäriska koordinater
- **Kap 12 (12.1, 12.3):** Vektorfunktioner och kurvor -- parametriserade kurvor i rummet, tangentvektorer, båglängd
- **Kap 13 (13.1-13.9):** Differentialkalkyl för flera variabler -- gränsvärden, kontinuitet, partiella derivator, differentierbarhet, kedjeregeln, gradient, riktningsderivata, implicita funktionssatsen, Taylors formel
- **Kap 14 (14.1, 14.2, 14.6):** Extremvärdesproblem -- kritiska punkter, andraderivatatestet, restriktioner (Lagrangemultiplikatorer), derivering under integraltecknet
- **Kap 15 (15.1-15.7):** Integralkalkyl för flera variabler -- dubbelintegraler, itererad integration, generaliserade integraler, variabelbyte, trippelintegraler, ytintegraler

## Hitta en specifik uppgift

När användaren säger t.ex. "uppgift 11 i 13.5" eller "13.5: 9,11,15":

1. **Direktlänk** (alla sektioner har individuella `### Uppgift N`-headings
   med URL-anchor): `07_fulltext/kap_13/13.5.md#uppgift-11`
2. **Översiktstabell:** `00_index/uppgiftsindex.md` listar sektion, uppgiftsspann
   och filväg för varje sektion.
3. Filen ligger under `07_fulltext/kap_<kapitel>/<sektion>.md` där kapitel och
   sektion alltid är kursens (10:e uppl.) numrering -- se tabellen ovan om
   användaren råkar ange 9:e upplagans nummer.

## När användaren skickar en övningsuppgift

1. **Identifiera sektion:** använd uppgiftsnumret (t.ex. "13.6: 11" = kapitel
   13, sektion 6) eller ämnets natur för att slå upp rätt sektion.
2. **Hitta teorin:** all teori för sektionen finns samlad i
   `07_fulltext/kap_X/X.Y.md` -- läs igenom den relevanta delen innan du
   löser uppgiften, inklusive definitioner, satser och lösta exempel som
   föregår `## Exercises`-sektionen.
3. **Slå upp exakt uppgiftstext:** varje uppgift har en egen
   `### Uppgift N`-heading i samma fil.
4. **Visa fullständiga steg, inte bara svar.** Kursen examinerar matematisk
   kommunikation lika mycket som rätt svar -- motivera varje steg, definiera
   symboler du inför, och ange vilken sats/metod som används (t.ex. "enligt
   kedjeregeln, sektion 13.5/12.5" eller "Lagrangemultiplikatormetoden,
   sektion 14.1/13.1").
5. **Ange källa med båda upplagenumren** när du refererar till teori, t.ex.
   "se Taylors formel, sektion 13.9 (= 12.9 i 9:e uppl.), sid 745".
6. **Geometrisk/topologisk terminologi:** var noga med öppna/slutna mängder,
   inre punkter, randpunkter, kompakthet -- kursen lägger vikt vid grundläggande
   topologi i R^n (sektion 10.1).

## Viktiga datum

- **Programmeringsprojekt:** deadline 23 oktober 2026, 17:00 (grupparbete,
  grupper väljs i Canvas under People → Programming Project)
- **Tentaanmälan i Ladok:** öppnar ca 9 oktober, stänger ca 23 oktober 2026
- **Ordinarie tentamen:** fredag 30 oktober 2026, kl 14:00-19:00, Sparta
- **Omtentamen:** lördag 28 november 2026, kl 08:00-13:00, sal 309A/309B,
  Matematikhuset

## Filstruktur

- `00_index/README.md` -- Kursöversikt
- `00_index/uppgiftsindex.md` -- Snabbtabell för att hitta uppgifter per sektion
- `01_kursmaterial/kapitelguide.md` -- Detaljerad guide per kapitel med rekommenderade uppgifter
- `01_kursmaterial/kursplan_canvas.md` -- Kursplanens 22 föreläsningar, renskrivna
- `01_kursmaterial/ovningsblad/` -- Övningsblad 1-3 som kompletterar boken
- `02_forelasningar/README.md` -- Föreläsningsschema med länkar till fulltext per sektion
- `03_inlamningar/` -- Ev. inlämningar (programmeringsprojektet)
- `04_studieplan/veckoplan.md` -- Vecka-för-vecka-plan fram till tentan
- `05_tentor/skarpa_tentor/` -- Gamla tentor
- `05_tentor/losningsforslag/` -- Lösningsförslag till gamla tentor
- `06_bokinnehall/` -- Ev. kortare sammanfattningar per kapitel
- `07_fulltext/kap_X/X.Y.md` -- Fullständiga studieanteckningar per sektion,
  med `[sid NN]`-markörer (9:e upplagans paginering) och `### Uppgift N`-headings
- `scripts/section_map.json` -- Maskinläsbar mappning 10:e <-> 9:e uppl. med sidintervall

## Navigationshierarki

1. **Översikt** → `00_index/README.md`
2. **Vad händer när** → `01_kursmaterial/kursplan_canvas.md` och `02_forelasningar/README.md`
3. **Detaljerad teori och uppgifter** → `07_fulltext/kap_X/X.Y.md`
4. **Hitta en specifik uppgift snabbt** → `00_index/uppgiftsindex.md`
5. **Vad ska jag göra denna vecka** → `04_studieplan/veckoplan.md`
6. **Tentaträning** → `05_tentor/skarpa_tentor/` + `05_tentor/losningsforslag/`
