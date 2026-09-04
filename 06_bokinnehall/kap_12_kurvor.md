# Kapitel 12: Kurvor

> Sammanfattning av Adams & Essex, Calculus, kapitel 12 (10:e uppl.), avsnitt 12.1, 12.3.
> Motsvarar 11.1 och 11.3 i 9:e uppl., som texten är hämtad ur.
> Fulltext: 07_fulltext/kap_12/

## Översikt

Kapitel 12 handlar om vektorfunktioner av en variabel, r(t) = x(t)i + y(t)j + z(t)k,
och kurvor i rummet -- alltså envariabelkalkyl fast med vektorvärda funktioner. Det
här är den naturliga bryggan mellan envariabelanalysen och de flervariabla begreppen
i kapitel 13: en kurva r(t) beskriver en enskild variabel t som "flyter genom" R^3,
och derivering/integrering görs komponentvis precis som för skalära funktioner.
Kursen läser 12.1 (vektorfunktioner, hastighet/acceleration) och 12.3 (kurvor och
parametriseringar, bågländ), men hoppar över 12.2 (rymdkurvornas differentialgeometri:
krökning, torsion, Frenet-ramen) samt Keplers lagar (12.4-12.6).

Begreppen härifrån -- särskilt bågländ ds = |dr/dt| dt och tangentvektorn v(t) --
återkommer i kapitel 13 (gradientens tolkning som normalvektor till nivåkurvor
bygger på att differentiera längs en kurva) och i kapitel 15.7 (ytarea-formeln
generaliserar samma idé till två variabler).

## 12.1 Vector Functions of One Variable
[Fulltext: 07_fulltext/kap_12/12.1.md](../07_fulltext/kap_12/12.1.md)

- **Positionsvektor**: r = r(t) = x(t)i + y(t)j + z(t)k beskriver en partikels
  läge vid tiden t; kurvan C är banan partikeln ritar upp.
- **Hastighet**: v(t) = dr/dt = lim(Delta t -> 0) [r(t+Delta t)-r(t)]/Delta t,
  tangent till C i rörelseriktningen. **Fart**: v(t) = |v(t)|.
- Kurvan är **slät** (glatt) där v existerar, är kontinuerlig och v != 0.
  Om v = 0 kan kurvan ha en spets/singularitet även om komponenterna är C^oo
  (klassiskt exempel: r = t^3 i + t^2 j har v=0 vid origo -> "kink" där, trots
  släta komponentfunktioner).
- Vektorfunktioner deriveras/integreras komponentvis (givet fixa basvektorer).
- **Acceleration**: a(t) = dv/dt = d^2r/dt^2. Newtons andra lag: F = ma.
- **THEOREM 1 -- Deriveringsregler för vektorfunktioner**: för deriverbara u(t),
  v(t) och skalär phi(t):
    d/dt[u+v] = u'+v'
    d/dt[phi u] = phi' u + phi u'
    d/dt[u . v] = u' . v + u . v'   (produktregel för skalärprodukt)
    d/dt[u x v] = u' x v + u x v'   (produktregel för kryssprodukt, ordning viktig!)
    d/dt|u| = (u . u')/|u|          (kedjeregel via |u| = sqrt(u . u))
- Klassiska tillämpningar: projektilbanor (konstant acceleration -gk, dubbel
  integration ger parabelbana), cirkulär rörelse med centripetalacceleration
  a = -omega^2 r, och att fart är konstant omm hastighet och acceleration är
  vinkelräta (v . a = 0).

## 12.3 Curves and Parametrizations
[Fulltext: 07_fulltext/kap_12/12.3.md](../07_fulltext/kap_12/12.3.md)

- En kurva ses som mängden punkter r(t), a <= t <= b -- men samma geometriska
  kurva har oändligt många olika parametriseringar (olika "hastighet" längs kurvan).
- **Sluten kurva**: r(a) = r(b). **Icke-självskärande kurva**: r(t_1) = r(t_2)
  medför t_1=a, t_2=b (dvs. skär sig inte annat än ev. i ändpunkterna).
  **Enkel sluten kurva**: sluten och icke-självskärande (t.ex. cirkel, ellips).
- Att parametrisera en skärningskurva mellan två ytor: om en av ytorna är en
  cylinder (ekvation oberoende av en variabel), parametrisera den cylindern
  först och lös sedan ut den saknade koordinaten via den andra ytans ekvation.
  Om ingen yta är en cylinder: subtrahera ekvationerna för att eliminera en
  variabel och skapa en ny yta (ofta en cylinder) som innehåller kurvan.
- **Bågländ**: för r(t) med kontinuerlig v(t),
    s = integral(t1 to t2) |v(t)| dt = integral(t1 to t2) v(t) dt.
  Bågelementet: ds = v(t) dt = |dr/dt| dt. Specialfall: plan kurva y=f(x) ger
  ds = sqrt(1+(f'(x))^2) dx; polär kurva r=g(theta) ger
  ds = sqrt(g(theta)^2 + g'(theta)^2) dtheta.
- **Styckvis slät kurva**: ändligt många släta bågar C_1+...+C_k sammanfogade;
  total längd = summan av delbågarnas längder.
- **Bågländsparametrisering** r(s): kurvan genomlöps med konstant fart 1
  (v(s)=1 identiskt). Existerar alltid för släta kurvor men kan sällan skrivas
  explicit -- kräver att s(t)=integral |dr/dtau| dtau kan inverteras till t(s).

## Nyckelresultat i kapitlet

1. **Deriveringsreglerna för vektorfunktioner (THEOREM 1, 12.1)** -- produktregler
  för skalär-, dot- och kryssprodukt; grunden för all vidare vektorkalkyl.
2. **Bågländsformeln s = integral |v(t)| dt (12.3)** -- den geometriska (parameter-
  oberoende) definitionen av kurvlängd; ligger till grund för ytarea-formeln i
  15.7 och för att förstå gradientens tolkning i 13.7.
3. **Sambandet mellan smidighet och v != 0** -- en kurva kan ha kontinuerligt
  deriverbara komponenter men ändå inte vara "slät" i punkter där v = 0.

## Vanliga uppgiftstyper

- Beräkna hastighet, fart och acceleration för en given r(t), och beskriva
  rörelsen (t.ex. cirkulär bana, projektilbana).
- Visa ett samband om fart/acceleration genom att derivera |r|^2 eller v^2 med
  produktregeln (jfr EXAMPLE 6-7 i 12.1).
- Parametrisera skärningskurvan mellan två givna ytor.
- Beräkna bågländ för en given kurva över ett parameterintervall, ofta med
  substitution.
- Avgöra om en given parametrisering representerar en sluten/enkel sluten kurva,
  och ange dess orientering.

## Fallgropar

- Att anta att en kurva är slät bara för att komponentfunktionerna är
  deriverbara -- kontrollera alltid att v(t) != 0 i den aktuella punkten.
- Vid kryssproduktens derivataregel: ordningen på faktorerna måste bevaras
  (kryssprodukten är inte kommutativ) -- d/dt[u x v] = u' x v + u x v', INTE
  v' x u + v x u'.
- Att blanda ihop bågländ (en geometrisk, parameteroberoende storhet) med
  "avstånd tillryggalagt i parametern t" -- olika parametriseringar av samma
  kurva ger samma bågländ men olika hastighetsprofiler.
- Vid skärningskurvor: att glömma att kontrollera vilket värdeintervall för
  parametern som faktiskt ger hela (eller den önskade delen av) kurvan.
