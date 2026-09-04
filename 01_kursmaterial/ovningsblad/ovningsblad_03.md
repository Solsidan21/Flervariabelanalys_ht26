# Övningsblad 3 — MATB21 Flervariabelanalys
> Hämtat från Canvas (Ex_sheet3.pdf), kurs 42188. Originalet är daterat "Spring 2016".
> Används i kursplanen vid F10 (uppgift 1, 2, 6), F12 (uppgift 7), F13 (uppgift 3, 4) och F14 (uppgift 8–12).

## Mixed problems

### Uppgift 1
Find all tangent planes to the surface z = 3x^3 + 2y^2 which are parallel to the plane 9x + 8y - z = 0. Also give the points of tangency.

### Uppgift 2
Prove, using the definition, that the mapping u = u(x) defined by

    u_1 = tan(x_1) + x_2,
    u_2 = x_2^3

is a bijection from the strip D : -pi/2 < x_1 < pi/2 in the x_1x_2-plane onto the entire u_1u_2-plane. Also find the inverse mapping x = x(u).

### Uppgift 3
Find the smallest and largest values of the function

    f(x, y) = sqrt(1 + x^2 + y^2) - 3x

in the set K : x >= 0, x^2 + y^2 <= 1.

### Uppgift 4
Determine all local extreme points for f(x, y) = x^2 - x^2 y + y^2.

### Uppgift 5
Prove that there is a unique C^2-function y(x) defined in a neighbourhood of 0 such that y(0) = 0 and sin(y(x)) + x^2 e^(y(x)) = 0. Find y'(0) and y''(0).

### Uppgift 6
Define the function u : R^3 -> R^3 by u(x, y, z) = (x^2 + y, y + z, z - x). Determine all points p in R^3 of the form p = (2, y, z) such that u has a C^1-smooth inverse defined near the point u(p).

### Uppgift 7
(a) Find the expansion of the binomial (2a - sqrt(b))^5.
(b) Find the constant term in the expansion of (x^2 - 1/x)^6.

## Differentiation under the integral sign

### Uppgift 8
Evaluate for alpha > -1 the integral integral(0 to 1) x^alpha (ln x)^k dx, k = 1, 2, ..., by differentiating integral(0 to 1) x^alpha dx with respect to alpha.

### Uppgift 9
Prove that the function

    y(x) = integral(0 to oo) e^(-t^2) cos(2xt) dt

satisfies the differential equation y' + 2xy = 0. Use this to determine y(x).

### Uppgift 10
Consider the function

    f(x) = integral(-1 to 2x) ln(3 + x + t^2)/(1 + t^2) dt,   x > -3.

Compute f'(0).

### Uppgift 11
Prove that the function

    y(x) = integral(0 to x) sin(x - t) ln(1 + t^2) dt

is a solution to the differential equation y'' + y = ln(1 + x^2).

### Uppgift 12
Determine the range of the function

    f(x) = integral(x to 2x) e^(-t^2 x) dt/t,   x > 0.

## Answers
1. There are two such tangent planes having equations 9(x - x_0) + 8(y - y_0) - (z - z_0) = 0, where (x_0, y_0, z_0) is a point of tangency. These points are (-1, 2, 5) and (1, 2, 11).
2. The inverse map is x_1 = arctan(u_2^(1/3) - u_1), x_2 = u_2, for (u_1, u_2) in R^2.
3. Maximum sqrt(2) is achieved at (0, ±1). The minimum sqrt(2) - 3 is attained at (1, 0).
4. (0, 0) is a local minimum. (There are saddle points at (±sqrt(2), 1), but these do not count as extreme points.)
5. y'(0) = 0 and y''(0) = -2.
6. This is satisfied for all p in {(2, y, z) : y, z in R}.
7. (a) 2^5 a^5 - 5·2^4 a^4 b^(1/2) + 10·2^3 a^3 b - 10·2^2 a^2 b^(3/2) + 5·2 a b^2 - b^(5/2). (b) C(6, 4) = 15.
8. (-1)^k k! / (1 + alpha)^(k+1).
9. sqrt(pi) e^(-x^2)/2.
10. f'(0) = pi/8 - pi sqrt(3)/36 + 2 ln 3.
12. (0, ln 2).
