# Kapitel 15: Multipelintegraler

> Sammanfattning av Adams & Essex, Calculus, kapitel 15 (10:e uppl.), avsnitt 15.1-15.7.
> Motsvarar kapitel 14 (9:e uppl.), som texten är hämtad ur.
> Fulltext: 07_fulltext/kap_15/

## Översikt

Kapitlet generaliserar den bestämda integralen (kapitel 5 i envariabelkursen)
till funktioner av två och tre variabler. Strukturen är analog rakt igenom:
definiera integralen som gränsvärde av Riemannsummor (15.1), utveckla en
praktisk beräkningsmetod genom iteration/upprepad envariabelintegrering (15.2),
hantera obegränsade domäner/integrander samt medelvärdessatsen (15.3), införa
variabelbyte -- först polära koordinater som specialfall, sedan den allmänna
formeln med Jacobideterminant (15.4) -- generalisera allt till tre dimensioner
med trippelintegraler (15.5), variabelbyte i tre dimensioner med cylindriska
och sfäriska koordinater (15.6), och avsluta med tillämpningar: ytarea, massa,
tyngdpunkt, tröghetsmoment (15.7).

Kapitlet knyter ihop nästan allt tidigare: Jacobideterminanten från 13.8
används rakt av i variabelbytesformeln (15.4, 15.6); cylindriska/sfäriska
koordinater från 10.6 används direkt i 15.6; och de kvadratiska ytorna från
10.5 dyker upp genomgående som integrationsområden. Detta är den mest
räkneintensiva delen av kursen och den där rätt val av koordinatsystem
(kartesiskt, polärt, cylindriskt, sfäriskt) ofta avgör om en uppgift är
görbar för hand eller inte.

## 15.1 Double Integrals
[Fulltext: 07_fulltext/kap_15/15.1.md](../07_fulltext/kap_15/15.1.md)

- Partition av en rektangel D i mn delrektanglar R_ij, Riemannsumma
  R(f;P) = sum_i sum_j f(x_ij,y_ij) A_ij. **DEFINITION 1**: dubbelintegralen
  doubleintegral over D f(x,y) dA är gränsvärdet av R(f;P) då normen ||P||->0,
  oberoende av val av punkter.
- Utvidgning till allmänna (icke-rektangulära) domäner D: förläng f med noll
  utanför D till en rektangel R som innehåller D (**DEFINITION 2**).
- **THEOREM 1**: kontinuerlig f på en sluten, begränsad domän med rand av
  ändlig längd är integrerbar.
- Egenskaper: nollarea ger integral 0; doubleintegral 1 dA = area av D;
  positiv/negativ f ger volym/negativ volym; linjaritet; monotoni; triangelolikhet;
  additivitet över icke-överlappande delområden.
- Vissa integraler kan beräknas "by inspection" via symmetri (udda integrand
  över symmetriskt område ger 0) eller genom att tolka integralen som en känd
  volym (t.ex. halvsfär).

## 15.2 Iteration of Double Integrals in Cartesian Coordinates
[Fulltext: 07_fulltext/kap_15/15.2.md](../07_fulltext/kap_15/15.2.md)

- **y-enkelt område**: begränsat av x=a, x=b och y=c(x), y=d(x). **x-enkelt
  område**: begränsat av y=c, y=d och x=a(y), x=b(y). **Regulärt område**:
  union av ändligt många icke-överlappande x-enkla och y-enkla delområden.
- **THEOREM 1, iteration**: för y-enkelt D,
    doubleintegral over D f(x,y) dA = integral(a to b) dx integral(c(x) to d(x)) f(x,y) dy,
  och analogt för x-enkla områden med omvänd ordning. Den inre integralen
  beräknas först (med den yttre variabeln fixerad som konstant), vilket ger en
  funktion av den yttre variabeln.
- Många områden (rektanglar, trianglar, skivor) är BÅDA x-enkla och y-enkla --
  iteration kan då göras i valfri ordning, och båda ger samma svar. Ibland är
  en riktning mycket enklare att räkna ut än den andra (t.ex. om inre
  integralen saknar elementär primitiv i en ordning: integral(0 to 1) dx
  integral(x to 1) e^(y^3) dy måste omordnas till dy dx-ordning för att gå
  att beräkna).
- Praktiskt: rita/tolka domänen D, avgör iterationsriktning, sätt upp gränser.

## 15.3 Improper Integrals and a Mean-Value Theorem
[Fulltext: 07_fulltext/kap_15/15.3.md](../07_fulltext/kap_15/15.3.md)

- Generaliserade (improper) dubbelintegraler uppstår när domänen är obegränsad
  eller integranden obegränsad nära ett randpunkt. För f>=0 avgörs
  konvergens/divergens genom att iterera och undersöka konvergensen hos de
  resulterande envariabelsintegralerna.
- Exempel: en generaliserad integral kan vara konvergent trots att integranden
  är obegränsad (integrerbar singularitet), eller divergera trots att den
  "ser konvergent ut" ytlig sett (t.ex. RR 1/(xy) dA över ett triangulärt
  område med hörn i origo divergerar).
- Varning: för integrander som byter tecken kan olika iterationsordningar ge
  olika (felaktiga) svar pga. kanceleringseffekter -- absolut konvergens
  (RR |f| dA konvergerar) garanterar att alla iterationer ger samma, korrekta
  värde.
- **THEOREM 1, medelvärdessats för dubbelintegraler**: om f kontinuerlig på
  sluten, begränsad, SAMMANHÄNGANDE mängd D, finns punkt (x_0,y_0) i D så att
    doubleintegral over D f(x,y) dA = f(x_0,y_0) * (area av D).
- **DEFINITION 1, medelvärde**: f-bar = (1/area(D)) doubleintegral over D f(x,y) dA.
  Specialfall: medelvärdet av x över D är just x-koordinaten för D:s tyngdpunkt
  (jfr 15.7).

## 15.4 Double Integrals in Polar Coordinates
[Fulltext: 07_fulltext/kap_15/15.4.md](../07_fulltext/kap_15/15.4.md)

- Areaelementet i polära koordinater: dA = dx dy = r dr dtheta (approximativt
  en rektangel med sidorna dr och r dtheta).
- Typisk iteration: doubleintegral over D f dA = integral(theta=alpha..beta) dtheta integral(r=r1(theta)..r2(theta)) f*r dr.
- Arean av ett polärt område r=f(theta), alpha<=theta<=beta:
    A = (1/2) integral(alpha to beta) f(theta)^2 dtheta.
- Byt till polära koordinater när domänen har cirkulär/radiell symmetri, eller
  när integranden förenklas i polär form (t.ex. y^2/x^2 = tan^2(theta)), även
  om integranden blir "fulare".
- Klassiskt resultat: integral(-oo to oo) e^(-x^2) dx = sqrt(pi), bevisas genom
  att kvadrera integralen, tolka som en dubbelintegral över R^2, och byta till
  polära koordinater (den enda kända metoden -- går inte med envariabelteknik).
- **Allmänt variabelbyte**: för x=x(u,v), y=y(u,v) en-till-en transformation
  med kontinuerliga partiella derivator och Jacobian
    partial(x,y)/partial(u,v) != 0,
  gäller dA = dx dy = |partial(x,y)/partial(u,v)| du dv. Polära koordinater är
  specialfallet med Jacobian = r.
- **THEOREM 4, variabelbytesformeln**:
    doubleintegral over D f(x,y) dx dy = doubleintegral over S g(u,v) |partial(x,y)/partial(u,v)| du dv,
  där g(u,v)=f(x(u,v),y(u,v)) och S är motsvarande område i uv-planet.

## 15.5 Triple Integrals
[Fulltext: 07_fulltext/kap_15/15.5.md](../07_fulltext/kap_15/15.5.md)

- Trippelintegralen tripleintegral over R f(x,y,z) dV definieras analogt med
  dubbelintegralen, via Riemannsummor över en partition av en rektangulär box.
  tripleintegral over D dV = volym av D. Om rho(x,y,z) är densitet (massa per
  volymenhet), är massan = tripleintegral over D rho dV.
- Iteration: dela upp domänen med plan parallella med koordinatplanen, "skiva"
  i en riktning, dubbelintegrera över varje skiva, integrera sedan resultatet
  över den kvarvarande variabeln. Sex möjliga iterationsordningar (x,y,z i
  valfri ordning) ger alla samma resultat, men vissa är mycket enklare.
- Praktisk teknik för att bestämma projektion: om regionen begränsas av två
  ytor, eliminera en variabel mellan deras ekvationer för att hitta den
  begränsande cylindern (som ger projektionen på ett koordinatplan).
- Att omordna en given iterering (byta ordning på x,y,z-integralerna) kan
  göras antingen grafiskt (skissa regionen från de givna gränserna) eller
  algebraiskt (skriva om olikhetskedjorna för varje variabel så att inre
  variablers gränser bara beror på yttre variabler som kommer "ovanför" dem i
  den nya ordningen).

## 15.6 Change of Variables in Triple Integrals
[Fulltext: 07_fulltext/kap_15/15.6.md](../07_fulltext/kap_15/15.6.md)

- Generell variabelbytesformel: för x=x(u,v,w), y=y(u,v,w), z=z(u,v,w) med
  Jacobian partial(x,y,z)/partial(u,v,w) != 0,
    dV = dx dy dz = |partial(x,y,z)/partial(u,v,w)| du dv dw,
  och
    tripleintegral over D f dV = tripleintegral over S g(u,v,w) |Jacobian| du dv dw.
- **Cylindriska koordinater** (från 10.6): x=r cos theta, y=r sin theta, z=z.
  Jacobian = r, så dV = r dr dtheta dz. Lämpligt vid axiell symmetri kring
  z-axeln (cylindrar, koner med axel längs z).
- **Sfäriska koordinater** (från 10.6): x=R sin(phi)cos(theta),
  y=R sin(phi)sin(theta), z=R cos(phi). Jacobian = R^2 sin(phi), så
  dV = R^2 sin(phi) dR dphi dtheta. Lämpligt vid sfärisk symmetri (sfärer,
  koner med spets i origo).
- Tumregel för val av koordinatsystem: använd cylindriska koordinater om
  integranden/domänen involverar x^2+y^2, sfäriska om den involverar
  x^2+y^2+z^2. Om det är oklart, låt integranden vara vägledande.
- Volymen av en ellipsoid x^2/a^2+y^2/b^2+z^2/c^2<=1 räknas enklast genom
  variabelbytet x=au,y=bv,z=cw (Jacobian abc), vilket reducerar problemet
  till volymen av enhetsklotet: (4/3)pi abc.

## 15.7 Applications of Multiple Integrals
[Fulltext: 07_fulltext/kap_15/15.7.md](../07_fulltext/kap_15/15.7.md)

- **Ytarea** för z=f(x,y) över domän D:
    S = doubleintegral over D sqrt(1 + (partial z/partial x)^2 + (partial z/partial y)^2) dA.
  Härleds via normalvektorn n=-f_1 i - f_2 j + k och sambandet
  dS = sec(theta) dA där theta är vinkeln mellan n och k.
- **Gravitationsattraktion från en skiva**: exempel på hur ett fysikaliskt
  problem (kraften från en cirkulär skiva med areadensitet sigma på en
  punktmassa på symmetriaxeln) reduceras till en dubbelintegral i polära
  koordinater. Om skivans radie -> oo fås en konstant kraft oberoende av
  avstånd (kraften från ett oändligt plan).
- **Moment och tyngdpunkt**: för en kropp med volymdensitet rho(x,y,z) i region R,
    massa m = tripleintegral over R rho dV,
    x-bar = (tripleintegral over R x rho dV) / m,  analogt y-bar, z-bar.
  Om densiteten är konstant kallas (x-bar,y-bar,z-bar) **centroiden** (geometrisk
  tyngdpunkt, oberoende av densitet).
- **Tröghetsmoment**: I = tripleintegral over R D(x,y,z)^2 rho dV, där D är
  vinkelrätt avstånd till rotationsaxeln. Kopplas till kinetisk energi vid
  rotation: KE = (1/2) I omega^2 (jämför KE=(1/2)mv^2 för translation).
  **Tröghetsradie**: D-bar = sqrt(I/m).
- Klassiskt exempel: rullande klot nedför ett lutande plan -- energiprincipen
  (translation + rotation) ger accelerationen a = (5/7) g sin(alpha), där
  faktorn 5/7 kommer direkt från klotets tröghetsmoment I=(2/5)ma^2 kring en
  diameter.

## Nyckelresultat i kapitlet

1. **DEFINITION 1 och THEOREM 1 (15.1)** -- dubbelintegralen som gränsvärde av
  Riemannsummor; kontinuitet på en sluten begränsad domän med "väluppfostrad"
  rand räcker för integrerbarhet.
2. **THEOREM 1, iteration (15.2)** -- den praktiska metoden: reducera en
  dubbelintegral till två efter varandra följande envariabelintegraler, med
  x-enkla/y-enkla områden som ramverk för att sätta upp gränserna.
3. **THEOREM 1, medelvärdessatsen för dubbelintegraler (15.3)** -- kräver
  sammanhängande domän; kopplar integralmedelvärde till en punktvärdering.
4. **Variabelbytesformeln med Jacobideterminant, dA = |partial(x,y)/partial(u,v)| du dv
  (15.4) resp. dV = |partial(x,y,z)/partial(u,v,w)| du dv dw (15.6)** -- den
  centrala tekniken för att förenkla integraler via polära/cylindriska/sfäriska
  koordinater eller andra variabelbyten.
5. **Volymelementen r dr dtheta dz (cylindriskt) och R^2 sin(phi) dR dphi dtheta
  (sfäriskt) (15.6)** -- måste kunna utan att härleda om varje gång.
6. **Ytarea-, massa-, tyngdpunkts- och tröghetsmomentformlerna (15.7)** -- de
  vanligaste tillämpningarna på tentan.

## Vanliga uppgiftstyper

- Sätta upp och beräkna en itererad dubbel- eller trippelintegral över ett
  givet område, i den ordning som är enklast (ibland måste man byta ordning
  för att kunna beräkna den inre integralen alls).
- Byta till polära, cylindriska eller sfäriska koordinater för att förenkla
  en integral, inklusive att korrekt räkna med volym-/areaelementet
  (glöm inte faktorn r respektive R^2 sin(phi)).
- Beräkna volym, area, massa, tyngdpunkt eller tröghetsmoment för en given
  kropp/skiva med given (eventuellt icke-konstant) densitet.
- Avgöra konvergens/divergens för en generaliserad multipelintegral, och
  beräkna dess värde när den konvergerar.
- Beräkna ytarean av en explicit given graf z=f(x,y) över ett angivet område.
- Byta variabler i en dubbel- eller trippelintegral med en given (icke-polär)
  transformation och räkna ut Jacobideterminanten.

## Fallgropar

- Att glömma extrafaktorn r (polära/cylindriska koordinater) eller R^2 sin(phi)
  (sfäriska koordinater) när integralen skrivs om -- detta är den vanligaste
  enskilda missen i hela kapitlet.
- Att sätta upp integrationsgränserna i fel ordning, dvs. låta en inre
  integrals gränser bero på en variabel som integreras längre ut (gränserna
  för den yttersta variabeln måste alltid vara konstanter).
- Vid byte av iterationsordning: att inte rita/tolka regionen ordentligt
  innan gränserna skrivs om -- lätt att missa att regionen faktiskt består av
  flera delar med olika gränser.
- Generaliserade integraler med integrand som byter tecken: att lita på att
  en iterationsordning konvergerar utan att kontrollera absolut konvergens --
  olika ordningar kan då ge olika svar.
- Val av koordinatsystem: att välja sfäriska koordinater för ett problem med
  bara cylindrisk (inte sfärisk) symmetri, vilket ofta ger en betydligt svårare
  integral (jämför EXAMPLE 4 i 15.6, där cylindriska koordinater är enklare
  trots att både sfär och cylinder ingår).
- Tyngdpunkt/centroid: att blanda ihop centroiden (geometrisk, densitet=1)
  med tyngdpunkten för en kropp med icke-konstant densitet -- centroidformeln
  gäller bara om densiteten är konstant (eller om man definierar den om med
  rho=1).
