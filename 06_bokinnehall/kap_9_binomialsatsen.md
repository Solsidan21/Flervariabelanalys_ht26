# Kapitel 9: Binomialsatsen och binomialserien

> Sammanfattning av Adams & Essex, Calculus, kapitel 9 (10:e uppl.), avsnitt 9.8. Samma avsnittsnummer i 9:e uppl.
> Fulltext: 07_fulltext/kap_9/

## Översikt

Det här är det sista avsnittet i kapitlet om oändliga serier och Taylor/Maclaurin-utveckling,
och det fungerar som en brygga till flervariabelanalysen: den binomiala utvecklingen
(a + x)^n för heltal n generaliseras här till binomialserien (1 + x)^r för godtyckligt
reellt r, med hjälp av Taylors formel med Lagranges restterm. Metoden -- utveckla, visa
att restterm eller konvergens fungerar, identifiera gränsen -- återkommer i flervariabelanalysen
när Taylors formel generaliseras till flera variabler (avsnitt 13.9) och restterm/gränsvärde
måste hanteras mer noggrant.

Kapitlet fungerar också som förkunskap: multiindex-notationen och Multinomialsatsen som
introduceras här dyker upp igen i generaliserade Taylor-utvecklingar för funktioner av
flera variabler, och binomialkoefficienter används genomgående när högre ordningens
partiella derivator (Leibniz regel-liknande uttryck) diskuteras.

Även om avsnittet i sig är algebraiskt/serieteoretiskt snarare än geometriskt, är
tekniken -- Maclaurinserie via binomialserien, sedan integration termvis för att få
serien för arcsin -- ett standardknep som återkommer så fort man behöver en seriedel
lösning på en implicit ekvation (jämför avsnitt 13.9, "Approximating Implicit Functions").

## 9.8 The Binomial Theorem and Binomial Series
[Fulltext: 07_fulltext/kap_9/9.8.md](../07_fulltext/kap_9/9.8.md)

- **Binomialsatsen** (heltalsfall): för positivt heltal n,
  (a + x)^n = sum(k=0..n) (n choose k) a^(n-k) x^k, där (n choose k) = n! / ((n-k)! k!).
  Bevisas med Taylors formel: f(x) = (a+x)^n har f^(k)(x) = 0 för k > n, så
  Maclaurinserien har bara ändligt många termer och är exakt lika med funktionen.
- **Binomialserien** (THEOREM 23): för |x| < 1 och godtyckligt reellt r,
  (1 + x)^r = 1 + sum(n=1..oo) [r(r-1)...(r-n+1)/n!] x^n.
  Beviset bygger inte på Taylors restterm utan på ett smart trick: visa att serien
  f(x) satisfierar differentialekvationen (1+x)f'(x) = r f(x) med f(0) = 1, varav
  f(x)/(1+x)^r är konstant lika med 1.
- Specialfall r = -1/2 ger Maclaurinserien för 1/sqrt(1+x); genom substitution
  x -> -t^2 och termvis integration fås serien för sin^(-1) x (arcsin).
- **Multinomialsatsen** (THEOREM 24): generaliserar binomialsatsen till summor av
  n termer. Med multiindex m = (m_1,...,m_n), |m| = m_1+...+m_n = grad,
  (x_1+...+x_n)^k = sum över |m|=k av (k choose m_1,...,m_n) x_1^(m_1)...x_n^(m_n),
  där multinomialkoefficienten (k choose m_1,...,m_n) = k!/(m_1!...m_n!).
  Används bl.a. för att räkna antalet distinkta ordningar av objekt som inte alla
  är olika (kombinatorisk tolkning).

Vad man ska kunna efter avsnittet:
- Ställa upp och använda binomialserien för att hitta Maclaurinserien för
  uttryck av typen (1+x)^r, inklusive rotuttryck.
- Använda substitution och termvis integration/derivation på kända serier
  för att härleda nya serier (t.ex. arcsin).
- Räkna ut multinomialkoefficienter och tolka dem kombinatoriskt.

## Nyckelresultat i kapitlet

1. **Binomialsatsen** (heltalsexponent) -- ändlig summa, exakt likhet, avsnitt 9.8.
2. **THEOREM 23, Binomialserien** -- (1+x)^r som oändlig serie för |x| < 1, med
   bevis via en differentialekvation snarare än direkt restterm-analys. Detta är
   den viktigaste satsen i avsnittet och den vanligaste tentafrågan.
3. **THEOREM 24, Multinomialsatsen** -- generalisering till flera variabler; central
   för att senare räkna högre ordningens partiella derivator och Taylor-koefficienter
   i flera variabler (jämför (h . grad)^j f i avsnitt 13.9, som utvecklas just med
   multinomialkoefficienter för h = (h_1,...,h_n)).

## Vanliga uppgiftstyper

- Hitta Maclaurinserien för en given funktion genom att identifiera den som
  (1+g(x))^r för lämpligt r och g, och sedan sätta in i binomialserien.
  Vanliga exempel: 1/sqrt(1+x), sqrt(1-x^2), (1+x)^(-2) osv.
- Bestämma konvergensintervallet (och ibland konvergens vid ändpunkterna, som kräver
  t.ex. alternerande serietestet).
- Använda känd binomialserie plus substitution/integration för att härleda en
  serie för en besläktad funktion (mönstret i EXAMPLE 2 -> EXAMPLE 3: 1/sqrt(1+x)
  ger via x -> -t^2 och integration serien för arcsin).
- Räkna ut en specifik multinomialkoefficient eller använda Multinomialsatsen för
  att hitta koefficienten framför en viss monomial i en utvecklad potens av en
  flertermssumma.

## Fallgropar

- Att blanda ihop den ändliga (exakta) binomialsatsen för heltal n med den
  oändliga binomialserien för godtyckligt r -- den senare kräver |x| < 1 för
  konvergens, den förra gäller för alla x.
- Att glömma teckenmönstret i koefficienterna r(r-1)(r-2)...(r-n+1)/n! när r är
  negativt eller icke-heltal (lätt att tappa ett minustecken).
- Vid härledning av nya serier via substitution: att glömma räkna om
  konvergensintervallet för den nya variabeln.
- Att förväxla binomialkoefficient (n choose k) med multinomialkoefficient
  (k choose m_1,...,m_n) -- den förra är specialfallet n = 2.

## Kort exempel på metoden

Sök Maclaurinserien för f(x) = 1/sqrt(1+x):
1. Skriv om som (1+x)^r med r = -1/2.
2. Sätt in i binomialserien:
   (1+x)^(-1/2) = 1 + sum(n=1..oo) [(-1/2)(-3/2)...(-1/2-n+1)/n!] x^n
                = 1 + sum(n=1..oo) (-1)^n (1*3*5*...*(2n-1)) / (2^n n!) x^n.
3. Ange konvergensområdet: |x| < 1, med specialkontroll av ändpunkter
   (här konvergerar serien även för x = 1 via alternerande serietestet, men inte för x = -1).

Samma serie kan sedan återanvändas: byt x mot -t^2 för att få serien för
1/sqrt(1-t^2), och integrera termvis från 0 till x för att få arcsin(x). Detta
är ett exempel på det generella arbetssättet i kapitel 9: bygg nya serier ur
kända serier genom substitution, addition/subtraktion, multiplikation,
derivation och integration -- att räkna ut alla koefficienter direkt från
definitionen (a_n = f^(n)(0)/n!) är nästan alltid mer arbete.
