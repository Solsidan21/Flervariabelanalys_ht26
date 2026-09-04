# Kapitel 13: Partiella derivator

> Sammanfattning av Adams & Essex, Calculus, kapitel 13 (10:e uppl.), avsnitt 13.1-13.9.
> Motsvarar kapitel 12 (9:e uppl.), som texten är hämtad ur.
> Fulltext: 07_fulltext/kap_13/

## Översikt

Det här är kursens mest omfattande kapitel och den centrala flervariabla
differentialkalkylen. Kapitlet bygger upp begreppen i en tydlig kedja: funktioner
av flera variabler och deras grafer/nivåkurvor (13.1) -> gränsvärden och
kontinuitet, som är mer subtila än i en variabel eftersom man kan närma sig en
punkt från oändligt många riktningar (13.2) -> partiella derivator, en variabel
i taget (13.3) -> högre ordningens derivator och likheten mellan blandade
partiella derivator (13.4) -> kedjeregeln i sina många varianter, homogena
funktioner och Jacobimatrisen (13.5) -> differentierbarhet som ett striktare
villkor än att partiella derivator existerar, med tangentplanet som geometrisk
tolkning (13.6) -> gradienten och riktningsderivator, som ger derivatan i en
godtycklig riktning (13.7) -> implicita funktioner, Jacobideterminanter och
Implicit Function Theorem (13.8) -> Taylors formel för flera variabler (13.9).

Den röda tråden är att varje ny idé (kontinuitet, derivata, differentierbarhet)
måste omdefinieras mer försiktigt än i envariabelfallet, eftersom flera
riktningar/vägar in mot en punkt måste ge samma resultat. Detta kapitel är
den direkta förutsättningen för kapitel 14 (extremvärden, som bygger på
gradient och Hessian) och används implicit i hela kapitel 15 (variabelbyte i
integraler bygger på Jacobideterminanter från 13.8).

## 13.1 Functions of Several Variables
[Fulltext: 07_fulltext/kap_13/13.1.md](../07_fulltext/kap_13/13.1.md)

- **DEFINITION 1**: en funktion f av n variabler tilldelar ett unikt reellt tal
  f(x_1,...,x_n) till varje punkt i en delmängd D(f) av R^n (domänkonventionen
  gäller precis som i en variabel).
- Grafen till z=f(x,y) är en yta i R^3; grafen till en funktion av tre variabler
  är en hyperyta i R^4 och kan inte ritas -- man använder istället **nivåytor**.
- **Nivåkurvor**: kurvorna f(x,y)=C i xy-planet, vertikala projektioner av
  skärningarna mellan grafen och de horisontella planen z=C. Tät gruppering av
  nivåkurvor indikerar branthet (jfr topografiska kartor).
  Viktigt: att nivåkurvorna är släta säger inget om huruvida grafen själv är
  slät (t.ex. f=x^2+y^2 och g=sqrt(x^2+y^2) har samma cirkulära nivåkurvor,
  men g:s graf, en kon, är inte slät i origo).
- **Nivåytor** för funktioner av tre variabler: f(x,y,z)=C ger en yta i R^3.

## 13.2 Limits and Continuity
[Fulltext: 07_fulltext/kap_13/13.2.md](../07_fulltext/kap_13/13.2.md)

- **DEFINITION 2 (epsilon-delta)**: lim_(x,y)->(a,b) f(x,y)=L om för varje
  epsilon>0 finns delta>0 så att |f(x,y)-L|<epsilon när 0<sqrt((x-a)^2+(y-b)^2)<delta
  och (x,y) i D(f). Gränsvärdet måste vara samma oavsett väg mot (a,b).
- Vanliga gränsvärdeslagar (summa, produkt, kvot, sammansättning) gäller precis
  som i en variabel.
- **Patologiska gränsvärden**: f(x,y)=2xy/(x^2+y^2) saknar gränsvärde i origo
  (olika värde längs olika räta linjer genom origo). f(x,y)=2x^2y/(x^4+y^2)
  har gränsvärde 0 längs VARJE rät linje genom origo, men gränsvärdet 1 längs
  y=x^2 -- alltså saknas gränsvärdet ändå. Detta visar att det INTE räcker att
  kontrollera räta linjer.
  f(x,y)=x^2y/(x^2+y^2) HAR gränsvärde 0 (bevisas med olikheten
  |f(x,y)| <= |y| <= sqrt(x^2+y^2)).
- **DEFINITION 3, kontinuitet**: f är kontinuerlig i (a,b) om
  lim_(x,y)->(a,b) f(x,y) = f(a,b). Kontinuitet längs varje enskild rät linje
  genom (a,b) medför INTE kontinuitet i (a,b).

## 13.3 Partial Derivatives
[Fulltext: 07_fulltext/kap_13/13.3.md](../07_fulltext/kap_13/13.3.md)

- **DEFINITION 1**: f_1(x,y) = lim(h->0) [f(x+h,y)-f(x,y)]/h (derivera mha x,
  håll y fast), analogt f_2. Notation: partial z/partial x = f_1 = D_1 f
  (boken föredrar numrerade subskript f_1,f_2 framför f_x,f_y för att undvika
  tvetydighet vid sammansatta funktioner).
- Alla vanliga deriveringsregler (summa, produkt, kvot) gäller variabelvis.
- **Tangentplan** till z=f(x,y) i (a,b,f(a,b)): normalvektor
  n = f_1(a,b) i + f_2(a,b) j - k, och planets ekvation
  z = f(a,b) + f_1(a,b)(x-a) + f_2(a,b)(y-b).
  Normallinjen: (x-a)/f_1(a,b) = (y-b)/f_2(a,b) = (z-f(a,b))/(-1).
- Viktig varning: att alla partiella derivator existerar i en punkt medför INTE
  att f är kontinuerlig där (till skillnad från envariabelfallet).

## 13.4 Higher-Order Derivatives
[Fulltext: 07_fulltext/kap_13/13.4.md](../07_fulltext/kap_13/13.4.md)

- Fyra andra ordningens partiella derivator för z=f(x,y): f_11, f_22 (rena) och
  f_12, f_21 (blandade). Subskript närmast f anger vilken derivering som görs
  först (f_12 = derivera först m.a.p. variabel 2, sedan variabel 1... läs
  boken noga -- konventionen anges explicit i texten).
- **THEOREM 1, likhet mellan blandade partiella derivator**: om de blandade
  partiella derivatorna av ordning n är kontinuerliga i en punkt P (och alla
  lägre ordningens derivator är kontinuerliga i en omgivning), så är de blandade
  derivatorna lika i P. Bevisas via två tillämpningar av envariabelns medelvärdessats.
  Utan kontinuitetsvillkoret kan f_12(0,0) != f_21(0,0) (motexempel finns i
  övningarna).
- **Laplaces ekvation**: partial^2 z/partial x^2 + partial^2 z/partial y^2 = 0.
  Funktioner som satisfierar den kallas **harmoniska**. Exempel: z=e^(kx)cos(ky).
  Harmoniska funktioner är C^oo, analytiska, och antar max/min endast på randen.
- **Vågekvationen**: partial^2 w/partial t^2 = c^2 partial^2 w/partial x^2.
  Lösning w=f(x-ct)+g(x+ct) för godtyckliga två gånger deriverbara f,g
  (vågor som rör sig åt höger/vänster med hastighet c).

## 13.5 The Chain Rule
[Fulltext: 07_fulltext/kap_13/13.5.md](../07_fulltext/kap_13/13.5.md)

- Grundversion: om z=f(x,y), x=u(t), y=v(t), så
    dz/dt = (partial z/partial x)(dx/dt) + (partial z/partial y)(dy/dt).
- Version med två "sekundära" variabler: x=u(s,t), y=v(s,t) ger
    partial z/partial s = (partial z/partial x)(partial x/partial s) + (partial z/partial y)(partial y/partial s),
  och analogt för partial z/partial t. Kan skrivas som matrisprodukt.
- Allmän regel (via "kartor"/träddiagram): en term för varje väg från den
  beroende variabeln till differentieringsvariabeln i beroendediagrammet.
- Notationsfälla: partial z/partial t kan betyda antingen den direkta partiella
  derivatan (en variabel hålls fast) eller den totala kedjeregel-derivatan när
  z beror på t både direkt och indirekt via andra variabler -- boken använder
  |_{x,y,s} för att förtydliga vilka variabler som hålls fasta.
- **Homogena funktioner**: f är positivt homogen av grad k om
  f(tx_1,...,tx_n) = t^k f(x_1,...,x_n) för t>0.
- **THEOREM 2, Eulers sats**: om f är positivt homogen av grad k med
  kontinuerliga partiella derivator, så gäller
    sum(i=1..n) x_i f_i(x_1,...,x_n) = k f(x_1,...,x_n).
- Laplaces ekvation i polära koordinater (härledd med kedjeregeln):
    partial^2 z/partial r^2 + (1/r) partial z/partial r + (1/r^2) partial^2 z/partial theta^2
    = partial^2 z/partial x^2 + partial^2 z/partial y^2.

## 13.6 Linear Approximations, Differentiability, and Differentials
[Fulltext: 07_fulltext/kap_13/13.6.md](../07_fulltext/kap_13/13.6.md)

- **Linearisering**: L(x,y) = f(a,b) + f_1(a,b)(x-a) + f_2(a,b)(y-b) approximerar
  f nära (a,b); grafen är tangentplanet.
- **DEFINITION 5, differentierbarhet**: f är differentierbar i (a,b) om
    lim_{(h,k)->(0,0)} [f(a+h,b+k)-f(a,b)-h f_1(a,b)-k f_2(a,b)] / sqrt(h^2+k^2) = 0.
  Detta är ett strängare villkor än att f_1,f_2 existerar -- differentierbarhet
  medför kontinuitet, men existens av partiella derivator gör det inte.
- **THEOREM 3 (Mean-Value Theorem)** och **THEOREM 4**: om f_1 och f_2 är
  kontinuerliga i en omgivning av (a,b), så är f differentierbar där. Detta är
  det praktiska testet man faktiskt använder.
- **THEOREM 5, formellt bevis av kedjeregeln** för z=f(x,y), x=u(s,t), y=v(s,t),
  givet att f är differentierbar (inte bara att partiella derivator existerar).
- **Differential**: dz = f_1 dx_1 + ... + f_n dx_n; approximerar Delta f med
  litet fel relativt avståndet mellan punkterna. Typisk tillämpning:
  felfortplantning/procentuell förändring (t.ex. pendelperiod T=2pi sqrt(L/g)).
- **Jacobimatrisen** Df(x) för en transformation f: R^n -> R^m (m funktioner av
  n variabler): matrisen av alla partial y_i/partial x_j. Kedjeregeln för
  sammansatta transformationer blir matrisprodukt: D(g o f)(x) = Dg(f(x)) Df(x),
  precis som i en variabel.

## 13.7 Gradients and Directional Derivatives
[Fulltext: 07_fulltext/kap_13/13.7.md](../07_fulltext/kap_13/13.7.md)

- **DEFINITION 6, gradient**: grad f(x,y) = f_1(x,y) i + f_2(x,y) j (del-operatorn
  nabla = i partial/partial x + j partial/partial y).
- **THEOREM 6**: om f är differentierbar i (a,b) och grad f(a,b) != 0, är
  grad f(a,b) en normalvektor till nivåkurvan genom (a,b).
- **DEFINITION 7, riktningsderivata**: för enhetsvektor u,
    D_u f(a,b) = lim(h->0+) [f(a+hu,b+hv)-f(a,b)]/h = d/dt f(a+tu,b+tv)|_(t=0).
- **THEOREM 7**: om f är differentierbar, D_u f(a,b) = u . grad f(a,b).
- **Geometriska egenskaper hos gradienten**:
  (i) f växer snabbast i riktning grad f(a,b), med maximal ökningstakt |grad f(a,b)|.
  (ii) f avtar snabbast i riktning -grad f(a,b).
  (iii) Riktningsderivatan är noll i riktningar tangentiella till nivåkurvan.
- **Gradient i tre eller fler dimensioner**: grad f(x,y,z) = f_x i + f_y j + f_z k;
  normal till nivåytan f(x,y,z)=C.

## 13.8 Implicit Functions
[Fulltext: 07_fulltext/kap_13/13.8.md](../07_fulltext/kap_13/13.8.md)

- Grundfrågan: när definierar F(x,y)=0 y som en funktion av x nära en punkt
  (a,b)? Villkor: F_2(a,b) != 0 (nivåkurvan har ej vertikal tangent där).
  Implicit derivering ger dy/dx|_(x=a) = -F_1(a,b)/F_2(a,b).
- Analogt för F(x,y,z)=0 -> z=z(x,y) nära P_0, kräver F_3(P_0) != 0:
    partial z/partial x = -F_1/F_3,   partial z/partial y = -F_2/F_3.
- **DEFINITION 8, Jacobideterminant**: för u=u(x,y), v=v(x,y),
    partial(u,v)/partial(x,y) = |partial u/partial x  partial u/partial y; partial v/partial x  partial v/partial y|
  (2x2-determinant); generaliseras till n funktioner av n variabler.
- **THEOREM 8, Implicit Function Theorem**: för ett system av n ekvationer
  F^(i)(x_1,...,x_m,y_1,...,y_n)=0 (i=1..n) i en punkt P_0, om Jacobianen
  partial(F^(1),...,F^(n))/partial(y_1,...,y_n) != 0 vid P_0, så kan systemet
  lösas för y_1,...,y_n som funktioner av x_1,...,x_m nära P_0, och de partiella
  derivatorna ges av kvoter av Jacobideterminanter (generalisering av Cramers
  regel).
- Praktiskt mönster: partial y_i/partial x_j = -[Jacobian med y_i ersatt av x_j]
  / [Jacobian av F m.a.p. y_1,...,y_n].
- Viktigt: partial u/partial x != 1/(partial x/partial u) i flervariabelfallet
  (till skillnad från envariabelfallet) -- det är Jacobianen, inte en enskild
  partiell derivata, som spelar rollen av "invers derivata".

## 13.9 Taylor's Formula, Taylor Series, and Approximations
[Fulltext: 07_fulltext/kap_13/13.9.md](../07_fulltext/kap_13/13.9.md)

- Taylors formel för f: R^n -> R kring a, med h=(h_1,...,h_n):
    f(a+h) = sum(j=0..m) [(h . grad)^j f(a)] / j! + R_m(h;theta),
  där (h . grad) = h_1 D_1 + ... + h_n D_n och resttermen är Lagrange-formen
  utvärderad vid a+theta h för något theta i [0,1]. Alternativt Big-O-form:
  f(a+h) = ... + O(|h|^(m+1)).
- P_m(h) kallas gradens m Taylorpolynom; för m=1 återfås tangentplans-
  approximationen från 13.6.
- Andra gradens Taylorpolynom för f(x,y) i (a,b) ges explicit med f_1,f_2 (första
  ordningen) och f_11,f_12,f_22 (andra ordningen), viktade med
  binomialkoefficienter (h^2, 2hk, k^2) -- kopplingen till kapitel 9:s
  binomialsats/multinomialsats är tydlig här: koefficienterna i P_m(h) för n
  variabler ges av multinomialkoefficienter.
- **Approximera implicita funktioner**: om F(x,y)=0 definierar y=f(x) nära
  x=0 (garanterat av Implicit Function Theorem, 13.8), kan man sätta in en
  obestämd Maclaurinserie y=a_1x+a_2x^2+... i F och lösa ut koefficienterna
  genom att jämföra termer av samma grad -- ofta enklare än att räkna ut
  derivator via implicit derivering upprepade gånger.

## Nyckelresultat i kapitlet

1. **DEFINITION 2, gränsvärde i flera variabler (13.2)** -- måste gälla oavsett
  väg; standardteknik för att visa att ett gränsvärde INTE finns är att hitta
  två olika vägar med olika gränsvärden.
2. **THEOREM 1, likhet mellan blandade partiella derivator (13.4)** -- kräver
  kontinuitet av de blandade derivatorna; grunden för att kunna byta
  deriveringsordning fritt i praktiken.
3. **Kedjeregeln i sina olika former (13.5)**, sammanfattad i Jacobimatris-formen
  D(g o f) = Dg(f) Df (13.6) -- den mest generella och användbara formuleringen.
4. **DEFINITION 5, differentierbarhet (13.6)** och **THEOREM 4** (kontinuerliga
  partiella derivator => differentierbar) -- det praktiska kriteriet för att
  få använda tangentplan, kedjeregel och gradient utan att behöva verifiera
  gränsvärdesdefinitionen direkt.
5. **THEOREM 7, D_u f = u . grad f (13.7)** och gradientens tre geometriska
  egenskaper -- kärnan i optimeringstillämpningarna i kapitel 14.
6. **THEOREM 8, Implicit Function Theorem (13.8)** -- när och hur ett
  ekvationssystem kan lösas lokalt, med Jacobideterminanter som avgör
  lösbarhet och ger derivatorna.
7. **Taylors formel för flera variabler (13.9)** -- generaliserar tangentplans-
  approximationen till godtycklig ordning; direkt förlängning av kapitel 9:s
  Taylorteori.

## Vanliga uppgiftstyper

- Visa att ett gränsvärde saknas genom att jämföra värden längs olika kurvor
  (räta linjer räcker INTE alltid -- prova även parabler y=kx^2 etc.).
- Beräkna partiella derivator (även av högre ordning och blandade) för
  explicita funktioner, och kontrollera/utnyttja att f_12=f_21.
- Sätta upp tangentplan och normallinje till en graf z=f(x,y) i en given punkt.
- Tillämpa kedjeregeln på sammansatta funktioner med flera "lager" av
  beroenden (rita beroendediagram/träd för att räkna termer).
- Visa att en given funktion är homogen och tillämpa Eulers sats, eller
  verifiera att en funktion satisfierar Laplaces ekvation/vågekvationen.
- Beräkna riktningsderivata i en given riktning, och hitta riktningen för
  maximal ökning/minskning samt dess värde.
- Använda Implicit Function Theorem och Jacobideterminanter för att avgöra
  om, och hur, ett ekvationssystem kan lösas lokalt för vissa variabler i
  termer av andra, samt beräkna partiella derivator av lösningen.
- Beräkna Taylorpolynom av given grad för en funktion av två variabler kring
  en punkt, och använda det för numerisk approximation.
- Bestämma seriekoefficienter för en implicit definierad funktion genom att
  sätta in en obestämd potensserie i ekvationen.

## Fallgropar

- Att tro att kontinuitet längs varje rät linje genom en punkt medför
  kontinuitet i punkten -- motexempel finns explicit i kapitlet (13.2, EXAMPLE 4).
- Att anta att existensen av f_1 och f_2 i en punkt medför att f är
  kontinuerlig eller differentierbar där -- båda är falska i allmänhet.
- Att byta deriveringsordning i blandade partiella derivator utan att
  kontrollera kontinuitetsvillkoret i THEOREM 1.
- Vid kedjeregeln: att glömma en term när en variabel bidrar till den
  beroende variabeln på flera olika "vägar" (både direkt och indirekt).
- Att blanda ihop partial z/partial t (delvis derivata, en variabel hålls fast)
  med den totala derivatan dz/dt när z beror på t både direkt och genom andra
  variabler som själva beror på t.
- Riktningsderivata: att glömma att u måste vara en ENHETSVEKTOR i formeln
  D_u f = u . grad f -- annars måste man normalisera först.
- Implicit Function Theorem: att glömma kontrollera att den relevanta
  Jacobideterminanten är nollskild vid just den aktuella punkten, inte bara
  någonstans i domänen.
- Att förväxla partial u/partial x med 1/(partial x/partial u) -- det sambandet
  gäller INTE i flera variabler generellt; man måste använda Jacobianer.
