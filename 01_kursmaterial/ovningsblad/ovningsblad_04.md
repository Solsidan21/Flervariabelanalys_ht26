# Övningsblad 4 — MATB21 Flervariabelanalys
> Hämtat från Canvas (Ex_sheet4.pdf), kurs 42188. Originalet är daterat "Spring 2019".
> Temat är likformig kontinuitet — kompletterar Weierstrass sats (F11).

Let D be a subset of R^n and f : D -> R a function. We have the following definitions.

**(I)** f is said to be *continuous* in D if for each point x in D and each epsilon > 0 there exists a number delta = delta(x, epsilon) > 0 such that y in D, ||y - x|| < delta implies |f(y) - f(x)| < epsilon.

**(II)** f is *uniformly continuous* in D if for each epsilon > 0 there exists delta = delta(epsilon) > 0 such that x, y in D, ||x - y|| < delta implies |f(y) - f(x)| < epsilon.

Notice the subtle difference: in (II), the same number delta > 0 is chosen uniformly throughout D (depending only on epsilon), whereas in (I) one is allowed to choose different deltas at different points x in D. Clearly it is harder to satisfy (II), i.e. each uniformly continuous function is continuous.

An important theorem states that the two definitions (I) and (II) are in fact equivalent provided that the set D is compact. The following exercises aim at proving this statement.

### Uppgift 1
Prove that the function f(x) = 1/x is continuous on the interval D = (0, 1), but not uniformly continuous.

### Uppgift 2
Let B = {x in R^n : ||x|| < 1} be the open unit ball in R^n. Prove that each uniformly continuous f : B -> R is bounded on B.

### Uppgift 3
Prove that a function f : D -> R is continuous if and only if f obeys the implication

    x_j in D, x in D, x_j -> x  =>  f(x_j) -> f(x).

### Uppgift 4
Prove that f fails to be uniformly continuous on D if and only if there is some epsilon > 0 and two sequences x_j, y_j of points in D such that ||x_j - y_j|| <= 1/j for all j in {1, 2, 3, ...} and yet |f(x_j) - f(y_j)| > epsilon for all j. (We can here replace "1/j" by any sequence delta_j of positive real numbers such that delta_j -> 0 as j -> oo.)

### Uppgift 5
Prove that if K is a compact subset of R^n and if f : K -> R is continuous, then f is uniformly continuous.
Hint: Assume that f is continuous but not uniformly continuous and choose epsilon > 0 and sequences x_j, y_j in K as above. Then use Bolzano–Weierstrass' theorem to extract suitable subsequences and finally use the continuity of f to obtain a contradiction.
