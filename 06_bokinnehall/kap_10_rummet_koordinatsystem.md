# Kapitel 10: Rummet och koordinatsystem

> Sammanfattning av Adams & Essex, Calculus, kapitel 10 (10:e uppl.), avsnitt 10.1, 10.5, 10.6.
> Samma avsnittsnummer i 9:e uppl.
> Fulltext: 07_fulltext/kap_10/

## Översikt

Kapitel 10 lägger den geometriska grunden för hela flervariabelkursen: hur man
beskriver punkter, ytor och regioner i R^3 (och mer allmänt R^n). Kursen läser
bara ett urval av avsnitten -- 10.1 (analytisk geometri i tre dimensioner),
10.5 (kvadratiska ytor) och 10.6 (cylindriska och sfäriska koordinater) --
och hoppar över vektoralgebra, plan och räta linjer i rummet (10.2-10.4) samt
linjär algebra-delen (10.7), som förutsätts vara bekant eller hanteras på annat
håll i kursen.

10.1 introducerar koordinatsystemet i R^3, avståndsformeln, och de topologiska
grundbegreppen (öppen/sluten mängd, rand, inre, yttre) som sedan används rakt
igenom resten av flervariabelanalysen -- särskilt när gränsvärden, kontinuitet
och extremvärden diskuteras i kapitel 13-14. 10.5 katalogiserar de vanligaste
icke-degenererade andragradsytorna (kvadratytor): sfärer, cylindrar, koner,
ellipsoider, paraboloider och hyperboloider. Dessa ytor -- särskilt sfärer,
cylindrar och (elliptiska/hyperboliska) paraboloider -- används genomgående som
exempel och integrationsregioner i kapitel 13-15. 10.6 introducerar cylindriska
och sfäriska koordinater, som inte används på allvar förrän i kapitel 15 när
trippelintegraler beräknas över regioner med cylindrisk eller sfärisk symmetri.

## 10.1 Analytic Geometry in Three Dimensions
[Fulltext: 07_fulltext/kap_10/10.1.md](../07_fulltext/kap_10/10.1.md)

- Kartesiskt koordinatsystem i R^3: höger-handssystem, koordinataxlar x, y, z,
  koordinatplan (xy, xz, yz), åtta oktanter (första oktanten: x,y,z >= 0).
- **Avståndsformeln**: avståndet mellan P_1=(x_1,y_1,z_1) och P_2=(x_2,y_2,z_2) är
  r = sqrt((x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2). Specialfall: avstånd till origo
  r = sqrt(x^2+y^2+z^2).
- En ekvation i x,y,z representerar normalt en yta (2-dimensionellt objekt); saknas
  en variabel i ekvationen blir ytan en cylinder eller ett plan parallellt med den
  axeln. Två ekvationer representerar normalt en kurva (skärningslinje/kurva).
  Degenererade fall (t.ex. y^2+(z-1)^2=0 ger en linje, x^2+y^2+z^2=-1 ger tomma
  mängden) måste man kunna känna igen.
- **Euklidiskt n-rum R^n**: punkter som n-tipplar, avstånd generaliseras direkt,
  hyperplan är mängden x_n = 0.
- **Topologiska grundbegrepp** (för R^n, n >= 2): omgivning B_r(P) (öppen boll/skiva
  av radie r); öppen mängd (varje punkt har en omgivning helt i mängden); komplement
  S^c; sluten mängd (komplementet är öppet); randpunkt (varje omgivning innehåller
  punkter både i S och i S^c); rand bdry(S); inre punkt/inre int(S); yttre punkt/yttre
  ext(S). Hela rummet och tomma mängden är de enda mängder som är både öppna och slutna.

## 10.5 Quadric Surfaces
[Fulltext: 07_fulltext/kap_10/10.5.md](../07_fulltext/kap_10/10.5.md)

- Allmän andragradsekvation i tre variabler: A x^2+B y^2+C z^2+D xy+E xz+F yz+G x+H y+I z = J.
  Om vänsterledet faktoriseras i två linjära faktorer blir grafen ett par plan
  (degenererat fall).
- Sex ickedegenererade kvadratytor (kanoniska former, axlar längs koordinataxlarna):
  1. **Sfär**: x^2+y^2+z^2 = a^2 (eller centrerad i (x_0,y_0,z_0)).
  2. **Cylinder**: t.ex. x^2+y^2 = a^2 (cirkulär, axel längs z), eller z = x^2
     (parabolisk cylinder); allmänt: en ekvation som saknar en variabel ger en cylinder.
  3. **Kon**: z^2 = x^2+y^2 (rät cirkulär kon); alla kvadratkoner har en riktning där
     tvärsnitten är cirklar.
  4. **Ellipsoid**: x^2/a^2 + y^2/b^2 + z^2/c^2 = 1; alla plana tvärsnitt är ellipser.
  5. **Paraboloider**: elliptisk z = x^2/a^2 + y^2/b^2 (tvärsnitt z=k är ellipser);
     hyperbolisk z = x^2/a^2 - y^2/b^2 (sadelform, tvärsnitt är hyperbler; är en
     "ruled surface" -- genomlöps av två familjer av räta linjer).
  6. **Hyperboloider**: en mantelyta x^2/a^2+y^2/b^2-z^2/c^2 = 1 (sammanhängande,
     "ruled surface"); två mantelytor x^2/a^2+y^2/b^2-z^2/c^2 = -1 (två separata
     skålar). Båda är asymptotiska mot konen x^2/a^2+y^2/b^2 = z^2/c^2.

## 10.6 Cylindrical and Spherical Coordinates
[Fulltext: 07_fulltext/kap_10/10.6.md](../07_fulltext/kap_10/10.6.md)

- **Cylindriska koordinater** [r, theta, z]: generaliserar plana polära koordinater
  genom att lämna z oförändrad.
    x = r cos(theta), y = r sin(theta), z = z.
  Koordinatytor: r=r_0 (cirkulär cylinder), theta=theta_0 (halvplan genom z-axeln),
  z=z_0 (horisontellt plan). Lämplig för problem med axiell symmetri kring z-axeln.
- **Sfäriska koordinater** [R, phi, theta]: R = avstånd till origo, phi = vinkel från
  positiva z-axeln (0 <= phi <= pi), theta = vinkel i xy-planet (som i cylindriska/
  polära koordinater).
    x = R sin(phi) cos(theta), y = R sin(phi) sin(theta), z = R cos(phi).
  Samband: R^2 = x^2+y^2+z^2 = r^2+z^2, r = R sin(phi), tan(phi) = r/z, tan(theta) = y/x.
  Koordinatytor: R=R_0 (sfär), phi=phi_0 (konmantel), theta=theta_0 (halvplan).
  Lämplig för problem med sfärisk symmetri.
- Ordningen R, phi, theta (inte R, theta, phi) väljs så att enhetsvektor-trippeln
  blir höger-handad.
- Dessa koordinatsystem används inte på allvar förrän kapitel 15 (trippelintegraler),
  men bör läras in geometriskt redan här: vilken yta/kurva svarar mot "en koordinat
  konstant".

## Nyckelresultat i kapitlet

1. **Avståndsformeln i R^3 och R^n** (10.1) -- grundläggande för alla senare
   gränsvärdes- och kontinuitetsdefinitioner (jfr avsnitt 13.2: definitionen av
   gränsvärde använder just avståndet sqrt((x-a)^2+(y-b)^2) < delta).
- **Öppen/sluten mängd, rand, inre, yttre** (10.1) -- terminologi som återanvänds
  ordagrant i definitionen av kontinuitet, differentierbarhet och extremvärdesteori
  (kapitel 13-14: domänens rand är en av de tre platser där extremvärden kan uppstå).
2. **Klassificering av de sex kvadratytorna** (10.5) -- att direkt känna igen en
  yta från sin ekvation (eller tvärtom) är en förutsättning för att sätta upp
  rätt integrationsgränser i kapitel 15.
3. **Transformationsformlerna för cylindriska och sfäriska koordinater** (10.6)
  -- används direkt i kapitel 15 tillsammans med volymelementen dV = r dr dtheta dz
  respektive dV = R^2 sin(phi) dR dphi dtheta (dessa volymelement härleds i
  avsnitt 15.6, men transformationsformlerna kommer härifrån).

## Vanliga uppgiftstyper

- Identifiera vilken yta en given andragradsekvation representerar, eventuellt
  efter kvadratkomplettering (t.ex. hitta sfärens centrum och radie).
- Beskriva skärningskurvan mellan två givna ytor (t.ex. ett plan och en sfär,
  eller två cylindrar).
- Konvertera en punkt eller en ekvation mellan kartesiska, cylindriska och
  sfäriska koordinater.
- Avgöra om en given mängd är öppen, sluten, varken eller, och ange dess rand,
  inre och yttre.
- Skissa (eller beskriva) en kvadratyta utifrån dess kanoniska ekvation, och
  ange dess tvärsnitt i horisontella/vertikala plan.

## Fallgropar

- Att blanda ihop cylinderbegreppet i rummet (en yta ruled av parallella linjer,
  t.ex. x^2+y^2=a^2 utan begränsning på z) med "cylinder" som en begränsad kropp
  -- i det här kapitlet är en cylinder en obegränsad yta om inget annat sägs.
- Att glömma att en ekvation som saknar en variabel representerar en yta parallell
  med den saknade variabelns axel, inte en kurva i planet.
- Sfäriska koordinater: att förväxla ordningen och betydelsen av phi (vinkel från
  z-axeln, 0 till pi) och theta (vinkel i xy-planet, som i polära koordinater) --
  detta är ett klassiskt källa till teckenfel vid konvertering.
- Att tro att alla kvadratkoner är räta cirkulära koner -- allmänna kvadratkoner
  kan vara sneda, även om de alltid har någon riktning med cirkulära tvärsnitt.
- Randpunkter: en sluten mängd innehåller alla sina randpunkter, en öppen mängd
  innehåller ingen -- en mängd definierad med både strikta och icke-strikta
  olikheter (t.ex. 0 < x <= 1) är varken öppen eller sluten.
