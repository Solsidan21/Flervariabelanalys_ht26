# Extraktionsspec — fulltext från kursbok till Markdown

Gäller `07_fulltext/kap_X/X.Y.md`. Följer samma format som
`Envariabelsanalys_vt26/06_fulltext/` (referensfil: `kap_5/5.1.md`, `kap_5/5.5.md`).

## Källa och mål
- Råtext: `07_fulltext/_raw/<sektion>.txt` (utdata från `pdftotext -layout`).
- Målfil: `07_fulltext/kap_<K>/<K>.<N>.md` där K.N är **kursens** sektionsnummer.

## Filhuvud
```
# Section K.N: <engelsk titel ur boken>
> Studieanteckningar baserade på <bok>, sid <a>-<b>
```
Om upplagorna skiljer sig, lägg till på raden efter:
```
> Kursens numrering (Adams 10:e uppl.) = K.N. Motsvarar <M.P> i 9:e uppl., som texten är hämtad ur.
```

## Innehållsregler
1. **Fullständighet före komprimering.** All matematisk substans ska med:
   definitioner, satser, bevis, exempel med lösningar, anmärkningar, och alla
   övningsuppgifter. Skriv inte ihop, hoppa inte över, sammanfatta inte.
2. **Språk:** behåll bokens engelska. Skriv inte om till svenska.
3. **Ingen LaTeX.** Ren text/unicode, som i referensfilerna:
   `sum(i=m to n) f(i)`, `x^2`, `sqrt(x)`, `integral(a to b) f(x) dx`,
   `d/dx`, `partial f/partial x`, `<=`, `>=`, `!=`, `->`, `oo` för oändligheten.
   Flerradiga formler indenteras med 4 mellanslag.
4. **Sidmarkörer:** `[sid NN]` på egen rad där en ny sida i originalboken börjar.
   NN = sidnumret i boken (syns i sidhuvudet i råtexten), inte PDF-sidan.
   Markörerna ska vara strikt växande.
5. **Figurer:** ersätt med `[FIGUR K.N: <beskrivning av vad figuren visar>]` på egen
   rad, placerad där figuren refereras. Beskriv matematiskt innehåll, inte utseende.
6. **Rubriker:**
   - `## DEFINITION n -- <titel>` / `## THEOREM n -- <titel>` / `## EXAMPLE n`
   - `### PROOF` för bevis
   - `## Exercises K.N` för övningsavsnittet, sist i filen
   - `### Uppgift N` före varje numrerad övningsuppgift (siffran tas bort ur
     uppgiftstexten)
7. **Uppgiftsmarkörer:** behåll bokens markeringar som prefix i uppgiftstexten:
   `[!]` för svårare uppgifter, `[CAS]` för datoralgebra-uppgifter.
8. **Städa bort:** löpande sidhuvuden ("ADAMS & ESSEX: ... October 2016"),
   "CHAPTER n <titel>"-rader, marginalnoter som bara upprepar brödtexten,
   avstavning över radbrytning, och kolumnbrus från `-layout`.
9. Kapitelinledning (texten före första sektionen) läggs i kapitlets **första**
   sektionsfil under rubriken `## Chapter K Introduction`.
   `Chapter Review`-uppgifter läggs i kapitlets **sista** sektionsfil under
   `## Chapter Review`.

## Kvalitetskrav
- Ingen uppgift får saknas. Kontrollera att uppgiftsnumren är sammanhängande
  1..max och rapportera luckor i stället för att tysta hoppa över.
- Ingen sats eller definition får saknas.
- Filen ska gå att läsa fristående utan tillgång till PDF:en.

---

## Sessioner och kapitelgränser — lärdom från envariabelextraktionen (VT26)

**Vad som gick fel förra gången.** Sidintervallen per sektion var *uppskattade*
(`.claude/plans/extraction-plan.md` rad 271: "Sidnumren ovan är UPPSKATTADE ...
justera ±2 sidor vid behov"). Varje sub-agent fick ett eget intervall och
instruktionen "ta bara med din egen sektion". På en sida där en sektion slutar
och nästa börjar — och särskilt vid kapitelbyten, där sidan också innehåller
kapitelinledning eller Chapter Review — trodde båda agenterna att innehållet
tillhörde den andra, och sidan föll bort. Ingen upptäckte det, eftersom
verifieringen bara kollade att filerna *fanns* och att det fanns *några*
`[sid NN]`-markörer.

**Tre regler som gör om det omöjligt:**

1. **Härled sidintervall ur PDF:en, gissa aldrig.** Sektionsstart läses ur bokens
   löpande sidhuvuden / innehållsförteckning, och bok→PDF-offset verifieras på
   minst tre spridda sidor innan något extraheras.
2. **Överlappa alltid råtexten med ±1 sida** och gör gränsen till ett uttryckligt
   beslut i agentprompten: *"Om gränssidan innehåller början på nästa sektion —
   ta med allt fram till den rubriken och sluta där. Om den innehåller slutet på
   din sektion — ta med hela sidan."* Aldrig "ta bara med din egen sektion" utan
   den preciseringen.
3. **Extrahera per kapitel när kapitlet är litet nog.** En agent som äger hela
   kapitlet kan inte tappa en sektionsgräns. Kvar blir bara kapitelgränserna, som
   alltid ligger på ny sida och därför är ofarliga.

**Verifieringen som fångar det ändå:** `scripts/verify_coverage.py` kontrollerar att
varje boksida i det extraherade intervallet förekommer som `[sid NN]` i exakt en
fil, och att markörerna är strikt växande inom varje fil. Saknad sida = fel, inte
varning. Kör den efter varje session, före commit.
