# Övningsblad 1 — MATB21 Flervariabelanalys
> Hämtat från Canvas (Ex_sheet1.pdf), kurs 42188. Originalet är daterat "Spring 2016".
> Används i kursplanen vid F2 (uppgift 1–2) och F4 (uppgift 3–10).

### Uppgift 1
Sketch the boundary ∂M where M is the subset of R^2 consisting of all points (x, y) such that
(a) x^2 + y^2 < 1
(b) x^2 > y and x^2 + y^2 >= 1
(c) x^2 - y^2 < 0
(d) |x| + |y| <= 1
(e) |x| <= 1 and |y| <= 1
(f) |x| <= 1 or |y| < 1
(g) 0 < |y| <= x and 0 < x < 1
(h) (y^2 - x^4)/(x^2 + y^2 - 1) > 0

### Uppgift 2
Make a sketch of the set K which consists of those points (x, y) in R^2 such that 1 <= |x| + |y| <= 2. Then determine the maximal and minimal values of f(x, y) = x^2 + y^2 where (x, y) in K.

### Uppgift 3
Find the domain of definition D(f) where f is the function
(a) f(x_1, x_2) = ln(x_1 + 2x_2 - 1)
(b) f(x_1, x_2) = 1/(x_1^2 + x_2^2 + 2x_1x_2 - 1)
(c) f(x_1, x_2) = (1 + x_1x_2)/(x_1^2 + x_2^2 + x_1x_2)
(d) f(x_1, x_2) = 1/(x_1^2 - x_2^2)

### Uppgift 4
(a) Sketch the graph of the function f(x, y) = 1/(x^2 + y^2).
(b) Draw the level curves f(x, y) = C for C = 1, 2, 3, 4.

### Uppgift 5
Sketch a few level curves and describe the graph of
(a) f(x, y) = sqrt(1 - x^2 - 3y^2)
(b) f(x, y) = 1 - x^2 - y^2
(c) f(x, y) = 1 - sqrt(x^2 + y^2)
(d) f(x, y) = 1 - x

### Uppgift 6
(a) Express the function f(x, y) = 2xy/(x^2 + y^2) in polar coordinates. Which values can f assume as (x, y) varies over the punctured disc 0 < x^2 + y^2 < delta^2? Does f become continuous if one defines f(0, 0) = 0?
Answer the above questions for the following functions:
(b) f(x, y) = 2xy/(1 + x^2 + y^2)
(c) f(x, y) = 2xy/sqrt(x^2 + y^2)
(d) f(x, y) = 2xy/(x^2 + y^2)^2

### Uppgift 7
Consider the function

    f(x_1, x_2) = x_1x_2/(x_1^2 + |x_2|)  for (x_1, x_2) != (0, 0),
    f(0, 0) = 0.

Determine whether f is continuous, and find the range f(R^2) = {f(x_1, x_2) : (x_1, x_2) in R^2}.

### Uppgift 8
Determine whether the following limits exist. Calculate them when this is the case.
(a) lim_((x,y)->(1,1)) (x - y)/(x - 1)
(b) lim_((x,y)->(0,0)) sin(sqrt(x^2 + y^2))/sqrt(x^2 + y^2)

### Uppgift 9
Find (if it exists) the following limit, where x = (x_1, x_2, x_3) and ||x|| = sqrt(x_1^2 + x_2^2 + x_3^2):

    lim_(x->0) ( e^(||x||^2) - 1 ) / ( ||x||^2 + x_1^2 x_2 + x_2^2 x_3 ).

### Uppgift 10
Find, if they exist, the following limits:
(a) lim_(x^2+y^2 -> oo) sin(x^2 y^2)/(x^2 + y^2)
(b) lim_(x^2+y^2 -> oo) xy e^(-(x+y)^2)

## Questions on basic set theory

### Uppgift 11
Let A = [-1, 3], B = (-3, 1], C = (2, 4], D = (-2, oo). Which of the following statements are true?
(a) 0 in A
(b) 0 not in B
(c) C subset D
(d) B subset D
(e) [0, 3] subset A
(f) A and B are disjoint
(g) {2, 3} subset D
(h) B and C are disjoint
(i) A not subset B

### Uppgift 12
For the sets A, B, C, D in Exercise 11, describe the following sets:
(a) A ∪ B
(b) D^c
(c) A ∩ C
(d) D \ C
(e) B ∩ C
(f) A ∪ B ∪ C ∪ D

## Answers
2. Largest value: 4. Smallest value: 1/2.
3. (a) x_1 + 2x_2 - 1 > 0. (b) x_1 + x_2 != ±1. (c) (x_1, x_2) != (0, 0). (d) x_2 != ±x_1.
5. (a) Half-ellipsoid. (b) Paraboloid. (c) Cone. (d) Plane.
6. (a) No. (b) Yes. (c) Yes. (d) No.
7. f is continuous and f(R^2) = R.
8. (a) Does not exist. (b) The limit equals 1.
9. The limit is 1.
10. (a) 0. (b) Does not exist.
11. (b), (d) and (f) are false; the remaining statements are true.
12. (a) A ∪ B = (-3, 3]. (b) D^c = (-oo, -2]. (c) A ∩ C = (2, 3]. (d) D \ C = (-2, 2] ∪ (4, oo). (e) B ∩ C = tom mängd. (f) A ∪ B ∪ C ∪ D = (-3, oo).
