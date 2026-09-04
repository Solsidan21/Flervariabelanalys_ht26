# Kapitel 14: Extremvärden

> Sammanfattning av Adams & Essex, Calculus, kapitel 14 (10:e uppl.), avsnitt 14.1, 14.2, 14.6.
> Motsvarar kapitel 13 (9:e uppl.), som texten är hämtad ur.
> Fulltext: 07_fulltext/kap_14/

## Översikt

Kapitlet handlar om hur man hittar och klassificerar max- och minvärden för
funktioner av flera variabler -- den viktigaste tillämpningen av partiella
derivator och gradient från kapitel 13. Kursen läser 14.1 (fria extremvärden:
kritiska punkter, singulära punkter, andraderivatatestet med Hessianen), 14.2
(extremvärden på begränsade/slutna domäner, inklusive en kort introduktion till
linjärprogrammering) och 14.6 (parameterproblem: derivering under integraltecken,
envelopper, perturbationer). Kursen hoppar över 14.3-14.5, vilket betyder att
**Lagrangemultiplikatorer för bivillkorade extremvärdesproblem behandlas INTE
i denna kurs enligt den lista som ges här** -- kapitlets egen introduktion
nämner metoden som kommande material i 14.3, men den ingår inte i kursens urval.

Metodiken bygger direkt på 13.6-13.7: kritiska punkter hittas via grad f = 0,
och andraderivatatestet bygger på definithet hos Hessianmatrisen (kvadratiska
former, som i sin tur bygger på linjär algebra från kapitel 10.7). 14.6 är
mer fristående och samlar tre udda men användbara tekniker: derivering genom
en integral (med parameter), envelopper av kurvfamiljer, och perturbationsmetoder
för ekvationer nära en enkel lösning.

## 14.1 Extreme Values
[Fulltext: 07_fulltext/kap_14/14.1.md](../07_fulltext/kap_14/14.1.md)

- Lokalt max/min definieras precis som i en variabel: f(x,y)<=f(a,b) (eller >=)
  för alla (x,y) i domänen tillräckligt nära (a,b). Globalt/absolut om
  olikheten gäller överallt i domänen.
- **THEOREM 1, nödvändiga villkor**: ett extremvärde kan bara inträffa i
  (a) en kritisk punkt (grad f(a,b)=0), (b) en singulär punkt (grad f(a,b)
  existerar ej), eller (c) en randpunkt av domänen.
- **THEOREM 2, tillräckliga villkor**: en kontinuerlig funktion på en sluten
  och begränsad delmängd av R^n antar absolut max och min där (generalisering
  av Max-Min-satsen från envariabelfallet).
- **Sadelpunkt**: en inre kritisk punkt där f varken har lokalt max eller min
  (t.ex. h(x,y)=y^2-x^2 i origo). OBS: grafen behöver inte se ut som en sadel
  vid en sadelpunkt (motexempel: f=-x^3 har en hel linje sadelpunkter längs
  y-axeln).
- Klassificering "för hand" via differensen Delta f = f(a+h,b+k)-f(a,b): om
  alltid >=0 (resp <=0) nära (0,0) -> lokalt min (max); byter tecken -> sadelpunkt.
- **THEOREM 3, andraderivatatestet (n variabler)**: vid en inre kritisk punkt a
  med kontinuerliga andra partiella derivator, bilda Hessianmatrisen
  H(x) = [f_ij(x)]. Då:
  (a) H(a) positivt definit -> lokalt min.
  (b) H(a) negativt definit -> lokalt max.
  (c) H(a) indefinit -> sadelpunkt.
  (d) annars (H(a) varken def. eller indef.) -> testet ger inget besked.
  Bevis via Taylors formel: f(a+h)-f(a) = (1/2) h^T H(a+theta h) h.
- **Tvåvariabelversionen** (paraphrase av (a)-(d) via 2x2-determinant): sätt
  A=f_11(a,b), B=f_12(a,b)=f_21(a,b), C=f_22(a,b).
  (a) B^2-AC<0 och A>0 -> lokalt min.
  (b) B^2-AC<0 och A<0 -> lokalt max.
  (c) B^2-AC>0 -> sadelpunkt.
  (d) B^2-AC=0 -> inget besked (kan vara max, min eller sadel).
- Klassiskt exempel: lådan utan lock med given volym V och minimal area --
  konstrained-problem som löses genom att eliminera en variabel (z=V/(xy)) och
  reducera till ett fritt tvåvariabelproblem (jfr Lagrangemultiplikatorer i
  14.3, som INTE ingår i kursens urval här, men som är den generella metoden
  för denna typ av problem när eliminering är obekväm).

## 14.2 Extreme Values of Functions Defined on Restricted Domains
[Fulltext: 07_fulltext/kap_14/14.2.md](../07_fulltext/kap_14/14.2.md)

- **Metod för extremvärden på en sluten, begränsad domän D**:
  1. Hitta kritiska/singulära punkter i det inre av D.
  2. Undersök randen (parametrisera hela eller delar av randen; kom ihåg
     ändpunkterna av varje randbit).
  3. Utvärdera f i alla punkter från 1-2 och jämför.
- Exempel: f(x,y)=2xy på skivan x^2+y^2<=4 -- kritisk punkt (0,0) (sadelpunkt),
  randen parametriseras med x=2cos t, y=2sin t och reduceras till ett
  envariabelproblem g(t)=8 cos t sin t = 4 sin 2t.
- Viktig distinktion: ett randpunkt-lokalt-max för den endimensionella
  restriktionen g(t) behöver INTE vara ett lokalt extremvärde för f själv, och
  behöver inte heller vara en sadelpunkt för f (den kan helt enkelt inte vara
  en kritisk punkt av f alls, eftersom den ligger på randen).
- **Linjärprogrammering** (kort introduktion, ej huvudmaterial): maximera/
  minimera en linjär funktion (målfunktionen) under linjära bivillkor. Lösningsmängden
  är en konvex polygon/polyeder; extremvärdet av en linjär funktion antas alltid
  i en hörnpunkt (aldrig i det inre om domänen har ett inre). Praktisk lösningsmetod:
  utvärdera målfunktionen i alla hörn, eller (bättre) utnyttja gradientens riktning
  för att utesluta hörn som uppenbart inte kan vara optimala.

## 14.6 Parametric Problems
[Fulltext: 07_fulltext/kap_14/14.6.md](../07_fulltext/kap_14/14.6.md)

- **Derivering genom en integral**: om F(x) = integral(a to b) f(x,t) dt, vill
  man ofta kunna byta plats på derivering och integrering:
    F'(x) = integral(a to b) (partial/partial x) f(x,t) dt.
  Detta kräver motivering eftersom både derivering och integrering är
  gränsvärdesoperationer (byte av ordning på gränsvärden är inte alltid tillåtet
  -- jämför likheten mellan blandade partiella derivator i 13.4).
- **THEOREM 6, Differentiating through an integral**: ger tillräckliga villkor
  (integralerna av f och f_1 existerar, och |f_11(x,t)| är dominerad av en
  integrerbar funktion g(t) oberoende av x) för att derivering genom integralen
  är giltig, även för generaliserade (improper) integraler.
- Klassisk tillämpning: beräkna integral(0 to oo) t^n e^(-t) dt = n! genom att
  derivera integral(0 to oo) e^(-xt) dt = 1/x upprepade gånger m.a.p. x.
- Om integrationsgränserna själva beror på x (a(x), b(x)):
    d/dx integral(a(x) to b(x)) f(x,t) dt
    = integral(a(x) to b(x)) (partial/partial x) f(x,t) dt + f(x,b(x)) b'(x) - f(x,a(x)) a'(x).
  (Kombination av Theorem 6 och envariabelns fundamentalsats via kedjeregeln.)
- **Envelopper**: en kurva C är envelopp till kurvfamiljen f(x,y,c)=0 om varje
  kurva i familjen tangerar C i någon punkt (beroende på c). Envelopens ekvation
  fås genom att eliminera c mellan
    f(x,y,c)=0   och   (partial/partial c) f(x,y,c)=0.
  Exempel: familjen av linjer x/c+cy-2=0 har envelopp xy=1 (hyperbel).
  Tillämpning: **Mach-konen** för ett överljudsflygplan -- envelopp av alla
  sfäriska ljudvågsfronter skapade vid tidigare tidpunkter, ger konen
  x = vt - (sqrt(v^2-c^2)/c) sqrt(y^2+z^2).
- **Perturbationsmetoden**: för en ekvation med en liten term (t.ex.
  y + epsilon ln(1+y) = x^2 med epsilon litet), sök lösningen som en serie i
  epsilon: y(x,epsilon) = y(x,0) + epsilon y_epsilon(x,0) + (epsilon^2/2!) y_(epsilon epsilon)(x,0) + O(epsilon^3),
  och bestäm termerna genom att derivera ekvationen m.a.p. epsilon och sätta
  epsilon=0.

## Nyckelresultat i kapitlet

1. **THEOREM 1 (14.1)** -- var extremvärden kan finnas: kritisk punkt, singulär
  punkt, eller randpunkt. Grundmönstret för alla optimeringsproblem i kapitlet.
2. **THEOREM 3, andraderivatatestet med Hessianen (14.1)**, samt dess
  tvåvariabelversion via B^2-AC -- det praktiska verktyget för att klassificera
  kritiska punkter.
3. **Metoden för extremvärden på slutna, begränsade domäner (14.2)**: kritiska
  punkter i det inre PLUS en fullständig genomgång av randen.
4. **Linjär programmering: extremvärden av linjära funktioner antas i hörnpunkter
  av det konvexa området (14.2)**.
5. **THEOREM 6, derivering genom en integral (14.6)** -- villkoren för att byta
  ordning på derivering/integrering, med tillämpning på parameterintegraler.
6. **Envelopp-metoden: eliminera c ur f=0 och partial f/partial c=0 (14.6)**.

## Vanliga uppgiftstyper

- Hitta och klassificera alla kritiska punkter för en given funktion av två
  (eller fler) variabler, med Hessianen/B^2-AC-testet.
- Visa att en given funktion har (eller saknar) globala extremvärden, ofta
  genom att argumentera om funktionens beteende i oändligheten kombinerat med
  Max-Min-satsen på en tillräckligt stor sluten skiva.
- Hitta max/min av en funktion på en explicit given sluten, begränsad domän
  (skiva, triangel, rektangel): kritiska punkter i det inre + parametrisering
  av randen bit för bit.
- Lösa ett enkelt konstruerat optimeringsproblem (minimal area/max volym under
  bivillkor) genom att eliminera en variabel med bivillkoret.
- Lösa en enkel linjärprogrammeringsuppgift genom att identifiera det konvexa
  områdets hörn och utvärdera målfunktionen i varje hörn.
- Beräkna en integral med parameter genom att derivera under integraltecknet
  upprepade gånger.
- Bestämma envelopp av en given kurv- eller ytfamilj genom att eliminera
  parametern mellan f=0 och partial f/partial c=0.

## Fallgropar

- Att glömma att kontrollera domänens rand vid sökning efter globala
  extremvärden -- en funktions enda kritiska punkt behöver inte vara det
  globala extremvärdet om domänen har en rand.
- Andraderivatatestet: om B^2-AC=0 ger testet inget besked -- man måste då
  undersöka Delta f direkt eller hitta annan metod. Att ändå dra en slutsats
  härifrån är ett vanligt fel.
- Vid randundersökning: ett lokalt extremvärde för den endimensionella
  restriktionen på en randbit betyder inte automatiskt ett lokalt extremvärde
  (eller sadelpunkt) för den ursprungliga funktionen f.
- Linjärprogrammering: att glömma att extremvärdet för en linjär målfunktion
  under linjära bivillkor ALLTID kan hittas bland hörnpunkterna -- att leta
  efter "kritiska punkter" i det inre av en polyeder är meningslöst eftersom
  gradienten till en linjär funktion aldrig är noll (om funktionen inte är
  konstant).
- Derivering genom integraltecken: att göra det utan att kontrollera något av
  villkoren i Theorem 6 (särskilt vid generaliserade/improper integraler, där
  det lätt går fel).
- Envelopp: att glömma att den härledda kurvan bara är en KANDIDAT till
  envelopp -- den ska verifieras genom att kontrollera att den verkligen
  tangerar familjens kurvor.
