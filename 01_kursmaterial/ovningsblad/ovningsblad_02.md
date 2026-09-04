# Övningsblad 2 — MATB21 Flervariabelanalys
> Hämtat från Canvas (Ex_sheet2.pdf), kurs 42188. Originalet är daterat "Spring 2016".
> Används i kursplanen vid F6 (uppgift 3), F7 (uppgift 1–2) och F8 (uppgift 6–8).

### Uppgift 1
Solve the differential equation

    partial f/partial x - 3 partial f/partial y = 0

by introducing the new variables u = ax + y, v = x, and choosing the constant a appropriately.

### Uppgift 2
Solve for x > 0 and y > 0 the differential equation

    x partial f/partial x + y partial f/partial y = y

by introducing new variables u, v by x = u and y = u/v.

### Uppgift 3
(a) Prove that the function f(x, y) = e^(x + 2y) is differentiable at the point (1, 0) (i) using the definition of differentiability, (ii) using an appropriate theorem.
(b) The same question for g(x, y) = sin(xy) at the point (0, 0).
(c) Prove that the function

    u(x, y) = xy/(x^2 + y^2) for (x, y) != (0, 0),   u(0, 0) = 0

is not differentiable at (0, 0) (i) using the definition of differentiability, (ii) using an appropriate theorem.

### Uppgift 4
Consider a function f(x, y) of two variables. Why do we write "partial f/partial x" for the partial derivative and not "df/dx", like in the 1-variable case?

### Uppgift 5
Let f(u, v) be a differentiable function and put h(x, y, z) = f(x/y, y/z), y > 0, z > 0. Prove that h is homogeneous of degree 0, i.e. h(tx) = t^0 h(x) for t > 0 and x in R^3. Then compute the expression

    x partial h/partial x + y partial h/partial y + z partial h/partial z.

### Uppgift 6
Suppose that f(x, y) only depends on r = sqrt(x^2 + y^2), i.e. f(x, y) = g(r) where g is a function of one variable. (f is then called a radial function.) Prove that

    Laplace f(x, y) = g''(r) + (1/r) g'(r),

where Laplace = partial^2/partial x^2 + partial^2/partial y^2 is the Laplacian. Use the result to determine the general solution to the differential equation Laplace f(x, y) = x^2 + y^2.

Remark. In Example 10, Section 12.5 (Adams 9:e uppl.; motsvarar 13.5 i 10:e), the general expression for the Laplacian in polar coordinates is given:
Laplace = partial^2/partial r^2 + (1/r) partial/partial r + (1/r^2) partial^2/partial theta^2.
It is a good exercise to read the derivation of this formula.

### Uppgift 7
Determine the general solution to the wave equation u_tt = c^2 u_xx by introducing the new variables xi = x + ct, eta = x - ct.

### Uppgift 8
Let u(x, t) be a (C^2-smooth) function which solves the following so-called Cauchy problem for the wave equation

    u_tt = c^2 u_xx,   x in R, t > 0,
    u(x, 0) = f(x),    x in R,
    u_t(x, 0) = g(x),  x in R,

where f and g are given (sufficiently smooth) functions. Use the result in Exercise 7 to show that

    u(x, t) = (1/2)( f(x + ct) + f(x - ct) ) + (1/(2c)) integral(x-ct to x+ct) g(s) ds.

This is the famous D'Alembert formula for the solution to Cauchy's problem. It tells how a wave propagates, if the form and velocity of the wave is known at the initial time t = 0.
Calculate u(x, t) if f(x) = sin x and g(x) = cos x.

## Answers
1. a = 3 and f(x, y) = phi(3x + y) where phi is an arbitrary differentiable function.
2. f(x, y) = y + phi(x/y) where phi is an arbitrary differentiable one-variable function.
5. 0.
6. g(r) = (1/16) r^4 + A ln r + B.
7. u(x, t) = Phi(x + ct) + Psi(x - ct) where Phi and Psi are arbitrary (twice differentiable) functions.
8. u(x, t) = (1/2)(1 - 1/c) sin(x + ct) + (1/2)(1 + 1/c) sin(x - ct).
