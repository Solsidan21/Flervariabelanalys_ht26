# Kapitelguide -- Adams *Calculus: A Complete Course* (10:e uppl.)

Denna guide mappar varje kapitel/sektion i kursens numrering (10:e uppl.)
till motsvarande sektion i 9:e upplagan (som fulltexten i `07_fulltext/` är
hämtad ur), till ämnesinnehåll och till rekommenderade uppgifter enligt
kursplanen. Se `CLAUDE.md` för den fullständiga förklaringen av
upplageförskjutningen.

---

## Kapitel 9 (9.8): Binomialsatsen

### 9.8 The Binomial Theorem (samma nummer i 9:e uppl.)
- **Kursinnehåll:** Binomialkoefficienter, Pascals triangel, binomialsatsen
  för (a+b)^n. Används senare som verktyg i Taylors formel för flera
  variabler (kap 13.9).
- **Fulltext:** `07_fulltext/kap_9/9.8.md`
- **Typiska lösningar:** utveckla (a+b)^n, beräkna enskilda termer/koefficienter,
  bevis med induktion.

---

## Kapitel 10 (10.1, 10.5, 10.6): Rummet R^n

### 10.1 Analytic Geometry in Three Dimensions (samma nummer i 9:e uppl.)
- **Kursinnehåll:** Punkter och vektorer i R^n, avstånd, grundläggande
  mängdlära och topologi (öppna/slutna mängder, inre punkter, randpunkter).
- **Fulltext:** `07_fulltext/kap_10/10.1.md`
- **Uppgifter:** 10.1: 7, 8, 18, 22, 32
- **Typiska lösningar:** avståndsberäkningar, avgöra om en mängd är öppen/sluten,
  beskriva geometriska objekt med olikheter.

### 10.5 Quadric Surfaces (samma nummer i 9:e uppl.)
- **Kursinnehåll:** Klassificering av kvadriska ytor (ellipsoider, paraboloider,
  hyperboloider, koner).
- **Fulltext:** `07_fulltext/kap_10/10.5.md`
- **Uppgifter:** 10.5: 5, 7, 9*, 11, 14, 23*
- **Typiska lösningar:** identifiera ytans typ från ekvationen, skissera snitt
  med koordinatplan.

### 10.6 Cylindrical and Spherical Coordinates (samma nummer i 9:e uppl.)
- **Kursinnehåll:** Cylinderkoordinater och sfäriska koordinater, omvandling
  till/från kartesiska koordinater.
- **Fulltext:** `07_fulltext/kap_10/10.6.md`
- **Uppgifter:** 10.6: 5, 7, 13*, 14*
- **Typiska lösningar:** koordinatbyten, beskriva ytor/kroppar i respektive
  koordinatsystem (grundläggande inför variabelbyte i multipelintegraler,
  kap 15.6-15.7).

**Övningsblad 1: uppgift 1, 2** hör till detta avsnitt (se
`01_kursmaterial/ovningsblad/`).

---

## Kapitel 12 (12.1, 12.3): Vektorfunktioner och kurvor

### 12.1 Vector Functions of One Variable (= 11.1 i 9:e uppl.)
- **Kursinnehåll:** Parametriserade kurvor i rummet, vektorfunktioner,
  gränsvärden och kontinuitet för vektorfunktioner.
- **Fulltext:** `07_fulltext/kap_12/12.1.md`
- **Uppgifter:** 12.1: 15, 16, 17
- **Typiska lösningar:** parametrisera kurvor, beräkna gränsvärde/derivata
  komponentvis.

### 12.3 Curvature, Torsion, and the Frenet Frame -- båglängd (= 11.3 i 9:e uppl.)
- **Kursinnehåll:** Tangentvektor, båglängd som integral av farten,
  omparametrisering med avseende på båglängd.
- **Fulltext:** `07_fulltext/kap_12/12.3.md`
- **Uppgifter:** 12.3: 5, 6, 7, 15, 17*, 19*, 20 samt 10, 11, 16. Review
  exercises kap 12: 2, 3, 4, 9, 10
- **Typiska lösningar:** beräkna båglängd, hitta tangent-/normalriktning,
  omparametrisering.

---

## Kapitel 13 (13.1-13.9): Differentialkalkyl för flera variabler

Kapitlet motsvarar kapitel 12 i 9:e upplagan (12.1-12.9). Detta är kursens
tyngdpunkt och upptar flest föreläsningar (F3-F12).

### 13.1 Functions of Several Variables (= 12.1)
- **Kursinnehåll:** Definitionsmängd, nivåkurvor/nivåytor, grafer av
  funktioner av flera variabler.
- **Fulltext:** `07_fulltext/kap_13/13.1.md`
- **Uppgifter:** 13.1: 5, 7, 14, 23, 24, 40
- **Typiska lösningar:** bestäm definitionsmängd, skissera nivåkurvor.

### 13.2 Limits and Continuity (= 12.2)
- **Kursinnehåll:** Gränsvärden för funktioner av flera variabler
  (svårare än en variabel -- oändligt många vägar mot en punkt), kontinuitet.
- **Fulltext:** `07_fulltext/kap_13/13.2.md`
- **Uppgifter:** 13.2: 3, 5, 7, 9, 10, 12, 14, 15, 20*. Även 12.3: 10, 11, 16
  och 13.2: 9, 11, 14 (F13)
- **Typiska lösningar:** visa att gränsvärde saknas (olika vägar ger olika
  värden), epsilon-delta-liknande uppskattningar, polära koordinater för
  gränsvärden i R^2.

### 13.3 Partial Derivatives (= 12.3)
- **Kursinnehåll:** Definition av partiell derivata, geometrisk tolkning,
  högre ordningens partiella derivator.
- **Fulltext:** `07_fulltext/kap_13/13.3.md`
- **Uppgifter:** 13.3: 3, 5, 9, 11, 12, 14, 15, 23, 24, 35, 37, 38
- **Typiska lösningar:** beräkna partiella derivator, blandade
  andraderivator, verifiera Clairauts sats.

### 13.4 Higher-Order Derivatives; Differentiability; Linear Approximations (= 12.4)
- **Kursinnehåll:** Differentierbarhet (starkare krav än att partiella
  derivator existerar), linjär approximation/tangentplan.
- **Fulltext:** `07_fulltext/kap_13/13.4.md`
- **Uppgifter:** 13.4: 1, 3, 6, 9, 11, 15, 16, 17. Review exercises kap 13: 5, 6.
  Övningsblad 2: uppgift 3
- **Typiska lösningar:** visa differentierbarhet från definitionen, ställ upp
  tangentplan, linjär felapproximation.

### 13.5 The Chain Rule (= 12.5)
- **Kursinnehåll:** Kedjeregeln för sammansatta funktioner av flera variabler
  -- trädformalism för att räkna ut alla termer.
- **Fulltext:** `07_fulltext/kap_13/13.5.md`
- **Uppgifter:** 13.5: 9, 11, 15, 17, 19, 22 samt 24, 26, 29
- **Typiska lösningar:** rita variabelträd, tillämpa kedjeregeln steg för
  steg, implicit derivering med kedjeregeln.

### 13.6 The Chain Rule -- forts. + partiella differentialekvationer (= 12.6)
- **Kursinnehåll:** Kedjeregeln i fler led, exempel på partiella
  differentialekvationer (t.ex. vågekvationen).
- **Fulltext:** `07_fulltext/kap_13/13.6.md`
- **Uppgifter:** 13.6: 3, 5, 11 samt 12, 15, 16, 19, 20
- **Typiska lösningar:** verifiera att en given funktion löser en PDE,
  variabelbyte i differentialekvationer.

### 13.7 Gradients and Directional Derivatives (= 12.7)
- **Kursinnehåll:** Gradientvektor, riktningsderivata, gradientens riktning
  som riktning för brantaste ökning, nivåkurvor och gradientens vinkelräthet
  mot dem.
- **Fulltext:** `07_fulltext/kap_13/13.7.md`
- **Uppgifter:** 13.7: 7, 9, 12, 14, 17, 22, 23, 26, 31. Review exercises
  kap 12: 2, 3, 4, 9, 10
- **Typiska lösningar:** beräkna riktningsderivata via gradienten, hitta
  riktning för störst ökning/minskning, tangentplan via gradient.

### 13.8 Implicit Functions (= 12.8) -- Inverse and Implicit Function Theorem
- **Kursinnehåll:** Implicita funktionssatsen, inversa funktionssatsen --
  när en implicit ekvation definierar en funktion lokalt, och hur man
  deriverar den. Se även föreläsningsanteckning 10 och extramaterial om
  implicita funktionssatsen (Lecture notes på Canvas).
- **Fulltext:** `07_fulltext/kap_13/13.8.md`
- **Uppgifter:** 13.7: 7, 9, 12, 14, 17, 22, 23, 26, 31 (F9); 13.8: 3, 5, 13,
  15, 16, 17, 18, 23, 24 (F10). Övningsblad 3: uppgift 1, 2, 6
- **Typiska lösningar:** verifiera villkoren i implicita funktionssatsen
  (Jacobian ≠ 0), beräkna derivator av implicit definierade funktioner.

### 13.9 Taylor's Formula (= 12.9)
- **Kursinnehåll:** Taylors formel för funktioner av flera variabler (andra
  ordningens approximation med Hessianen), samband med binomialsatsen (9.8).
- **Fulltext:** `07_fulltext/kap_13/13.9.md`
- **Uppgifter:** 13.9: 1, 3, 5, 7, 9, 10, 11, 13, 14, 15. Övningsblad 3: uppgift 7
- **Typiska lösningar:** ställ upp Taylorpolynom av grad 2, uppskatta
  approximationsfel, klassificera kritiska punkter via Hessianen (kopplar
  till kap 14).

---

## Kapitel 14 (14.1, 14.2, 14.6): Extremvärdesproblem

Motsvarar kapitel 13 i 9:e upplagan (13.1, 13.2, 13.6).

### 14.1 Extreme Values of Functions Defined on Restricted Domains -- Optimering (= 13.1)
- **Kursinnehåll:** Fria och restriktionsbelagda extremvärdesproblem,
  Weierstrass sats (existens av extremvärden på kompakta mängder, F11).
- **Fulltext:** `07_fulltext/kap_14/14.1.md`
- **Uppgifter:** 14.1: 4, 5, 19, 20, 21, 22
- **Typiska lösningar:** hitta kritiska punkter, klassificera med
  andraderivatatestet (Hessianen, se 13.9), jämför med randvärden.

### 14.2 Lagrange Multipliers -- restriktioner (= 13.2)
- **Kursinnehåll:** Lagrangemultiplikatormetoden för extremvärden under
  bivillkor.
- **Fulltext:** `07_fulltext/kap_14/14.2.md`
- **Uppgifter:** 14.2: 1, 3, 7, 10, 13 samt 13.2: 9, 11, 14
- **Typiska lösningar:** ställ upp Lagrangefunktionen, lös ekvationssystemet
  ∇f = λ∇g, hantera flera bivillkor.

### 14.6 Differentiation of Integrals with Respect to a Parameter (= 13.6)
- **Kursinnehåll:** Derivering under integraltecknet (Leibniz regel),
  inklusive fall med rörliga integrationsgränser.
- **Fulltext:** `07_fulltext/kap_14/14.6.md`
- **Uppgifter:** 14.6: 1, 2, 3, 5, 7, 10. Övningsblad 3: uppgift 8-12
- **Typiska lösningar:** tillämpa Leibniz regel, beräkna integraler genom att
  derivera med avseende på en parameter.

---

## Kapitel 15 (15.1-15.7): Integralkalkyl för flera variabler

Motsvarar kapitel 14 i 9:e upplagan (14.1-14.7). Kursens sista block
(F14-F18).

### 15.1 Double Integrals (= 14.1)
- **Kursinnehåll:** Definition av dubbelintegral som gränsvärde av
  Riemannsummor, integral över rektangel.
- **Fulltext:** `07_fulltext/kap_15/15.1.md`
- **Uppgifter:** 15.1: 17, 19
- **Typiska lösningar:** beräkna dubbelintegraler över rektanglar,
  geometrisk tolkning som volym.

### 15.2 Iteration of Double Integrals in Cartesian Coordinates (= 14.2)
- **Kursinnehåll:** Itererad integration, Fubinis sats, generella områden
  (mellan kurvor), generaliserade dubbelintegraler.
- **Fulltext:** `07_fulltext/kap_15/15.2.md`
- **Uppgifter:** 15.2: 1, 3, 5, 9, 11, 13, 17, 19, 22, 23
- **Typiska lösningar:** ställa upp itererade integraler i rätt ordning,
  byta integrationsordning, hantera generaliserade (oegentliga) integraler.

### 15.3 Improper Integrals and a Mean-Value Theorem -- variabelbyte (= 14.3)
- **Kursinnehåll:** Generaliserade dubbelintegraler, medelvärdessats för
  integraler, inledning till variabelbyte.
- **Fulltext:** `07_fulltext/kap_15/15.3.md`
- **Uppgifter:** 15.3: 3, 5, 7, 9, 11, 13, 14, 26, 27, 28, 29
- **Typiska lösningar:** avgöra konvergens av generaliserade integraler,
  jämförelsemetoder.

### 15.4 Double Integrals in Polar Coordinates (= 14.4)
- **Kursinnehåll:** Variabelbyte till polära koordinater i dubbelintegraler,
  Jacobianen för polärt byte.
- **Fulltext:** `07_fulltext/kap_15/15.4.md`
- **Uppgifter:** 15.4: 5, 9, 11, 13, 15, 21, 23, 25, 33, 35, 38
- **Typiska lösningar:** byta till polära koordinater, bestämma nya
  integrationsgränser, beräkna Jacobian.

### 15.5 Triple Integrals (= 14.5)
- **Kursinnehåll:** Trippelintegraler över kroppar i R^3, itererad
  integration i tre variabler.
- **Fulltext:** `07_fulltext/kap_15/15.5.md`
- **Uppgifter:** 15.5: 3, 5, 7, 9, 11, 12, 14, 27
- **Typiska lösningar:** ställa upp trippelintegraler, välja
  integrationsordning utifrån områdets form.

### 15.6 Change of Variables in Triple Integrals (= 14.6)
- **Kursinnehåll:** Variabelbyte i trippelintegraler, cylinder- och sfäriska
  koordinater (koppling till kap 10.6), allmän Jacobianformel.
- **Fulltext:** `07_fulltext/kap_15/15.6.md`
- **Uppgifter:** 15.6: 1, 3, 5, 6, 13, 15, 16, 17, 18
- **Typiska lösningar:** byta till cylinder-/sfäriska koordinater, beräkna
  Jacobianen, bestämma nya gränser.

### 15.7 Applications of Multiple Integrals to Surface Area -- ytintegraler (= 14.7)
- **Kursinnehåll:** Ytarea som ytintegral, parametriserade ytor.
- **Fulltext:** `07_fulltext/kap_15/15.7.md`
- **Uppgifter:** 15.7: 1, 3, 5, 6, 7, 8, 9
- **Typiska lösningar:** parametrisera ytan, beräkna kryssprodukt av
  partiella derivator, integrera normens belopp.

---

## Sammanfattning: kapitel -> föreläsningar

| Kapitel | Sektioner (10:e uppl.) | Föreläsningar |
|---|---|---|
| 9 | 9.8 | F10 |
| 10 | 10.1, 10.5, 10.6 | F1 |
| 12 | 12.1, 12.3 | F2-F3 |
| 13 | 13.1-13.9 | F3-F12 |
| 14 | 14.1, 14.2, 14.6 | F12-F14 |
| 15 | 15.1-15.7 | F14-F18 |

(`*` markerar uppgifter kursplanen anger som svårare.)
