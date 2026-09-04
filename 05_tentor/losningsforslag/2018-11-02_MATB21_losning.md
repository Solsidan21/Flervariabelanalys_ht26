# Lösningsförslag — tentamen MATB21 Flervariabelanalys, fredag 2 november 2018
> Hämtat från Canvas, kurs 42188 (Suggested solutions exam 02112018.pdf), daterat 9 november 2018.
> Tentan utan lösningar: `../skarpa_tentor/2018-11-02_MATB21.md`

### Lösning 1
**(5p) Compute the volume of the solid between the cone z = 4 - sqrt(x^2 + y^2) and the paraboloid z = x^2 + y^2 + 2.**

Let R be the region below the cone z = 4 - sqrt(x^2 + y^2) and above the paraboloid z = x^2 + y^2 + 2. In cylindrical coordinates x = r cos(theta), y = r sin(theta), z = z, R can be expressed as

    R = {(r, theta, z) in R^3 : r^2 + 2 <= z <= 4 - r,  0 < r <= 1,  0 <= theta <= 2pi}.

The inequalities for r and theta are obtained by considering the intersection of the surfaces z = 4 - r and z = r^2 + 2:

    4 - r = r^2 + 2  <=>  r = 1 or r = -2.

Since r cannot be negative, the circle of intersection has radius 1. The volume of R is now

    tripleintegral over R dV = integral(0 to 2pi) dtheta integral(0 to 1) r dr integral(r^2+2 to 4-r) dz
        = 2pi integral(0 to 1) r [z] from z=r^2+2 to z=4-r dr
        = 2pi integral(0 to 1) (2r - r^2 - r^3) dr
        = 5pi/6 v.e.

**Svar:** 5pi/6 volymenheter.

### Lösning 2
**Consider the equation cos(z) + x^3 + (1/4)y^4 - y = 1.**

**(a)** Let F(x, y, z) := cos(z) + x^3 + (1/4)y^4 - y. The normal to the tangent plane of the level surface F = 1 at the point (1, 0, pi/2) is grad F(1, 0, pi/2):

    grad F(x, y, z) = (3x^2, y^3 - 1, -sin(z)),
    grad F(1, 0, pi/2) = (3, -1, -1).

So the normal equation of the plane is 3x - y - z = D. Since (1, 0, pi/2) lies on the plane,

    3·1 - 0 - pi/2 = D.

Hence the tangent plane has the equation 3x - y - z = 3 - pi/2.

**(b)** F is C^1 on R^3, so it is C^1 in the neighborhood of any point (x_0, y_0, z_0) with F(x_0, y_0, z_0) = 1. If

    F_2(x_0, y_0, z_0) != 0  <=>  y_0^3 - 1 != 0  <=>  y_0 != 1,

then the Implicit Function Theorem guarantees that in a neighborhood of this point the solutions (x, y, z) can be expressed as (x, y(x, z), z). Similarly, around points with F_1(x_0, y_0, z_0) != 0 we can express the solutions as (x(y, z), y, z); this happens for x_0 != 0.

**Svar:** (a) 3x - y - z = 3 - pi/2. (b) Around (x_0, y_0, z_0) with y_0 != 1 for (x, y(x,z), z), and x_0 != 0 for (x(y,z), y, z).

### Lösning 3
**(a) (4p) Find the extreme values of f(x, y) = x^2 + y^2 + sin(x^2) + cos(y^2) over the region x^2 + y^2 <= pi.**

Candidates for extreme points are singular points, boundary points and critical points. There are no singular points because f is C^1 on R^2, hence C^1 over the given disk. The boundary points lie on x^2 + y^2 = pi. The critical points satisfy grad f(x, y) = 0, i.e.

    2x + 2x cos(x^2) = 0        2x(1 + cos(x^2)) = 0
                          <=>
    2y - 2y sin(y^2) = 0        2y(1 - sin(y^2)) = 0

The first equation is met if x = 0 or 1 + cos(x^2) = 0. Since x^2 + y^2 <= pi we have x in [-sqrt(pi), sqrt(pi)], so 1 + cos(x^2) vanishes only for x^2 = pi, i.e. x = ±sqrt(pi). Similarly the second equation is met when y = 0 or y = ±sqrt(pi/2). The points with grad f(x, y) = 0 are thus

    (0, 0), (±sqrt(pi), 0), (0, ±sqrt(pi/2)), (±sqrt(pi), ±sqrt(pi/2)) and (±sqrt(pi), ∓sqrt(pi/2)).

However, the points (±sqrt(pi), ±sqrt(pi/2)) and (±sqrt(pi), ∓sqrt(pi/2)) do not lie in the disk because pi + pi/2 > pi. The values of f are f(0, 0) = 1, f(±sqrt(pi), 0) = pi + 1, and f(0, ±sqrt(pi/2)) = pi/2 + 1.

On the boundary x^2 + y^2 = pi we have y^2 = pi - x^2, and

    f(x, y) = x^2 + y^2 + sin(x^2) + cos(y^2)
            = pi + sin(x^2) + cos(pi - x^2)
            = pi + sin(x^2) - cos(x^2).

Define g(x) := pi + sin(x^2) - cos(x^2) and optimize g over [-sqrt(pi), sqrt(pi)]. Again there are no singular points because g is C^1. The boundary points are x = ±sqrt(pi), which gives y = 0. The critical points satisfy

    g'(x) = 0  <=>  2x cos(x^2) + 2x sin(x^2) = 0,

true for x = 0 or cos(x^2) = -sin(x^2). Since x in [-sqrt(pi), sqrt(pi)], the only solution of the second equation is x = ±sqrt(3pi/4). The value of f at these points is pi + sqrt(2).

**Svar:** Max is pi + sqrt(2) and min is 1.

**(b) (1p)** f attains its minimum and maximum if it is continuous and D is bounded and closed.

### Lösning 4
**(a) (4p) Transform the partial differential equation y (partial u/partial x) - x (partial u/partial y) = x + y using x = r cos(theta), y = r sin(theta) for theta in [0, 2pi], r > 0.**

We want to rewrite the equation in terms of r, theta, partial u/partial r and partial u/partial theta. Note that

    x^2 + y^2 = r^2,   y/x = tan(theta).

Differentiating the first equation with respect to x gives 2x = 2r (partial r/partial x), i.e. partial r/partial x = x/r. Doing the same for the others,

    partial r/partial x = x/r,        partial r/partial y = y/r,
    partial theta/partial x = -y/r^2, partial theta/partial y = x/r^2.

Thinking of u as u(r, theta) = u(r(x,y), theta(x,y)), the chain rule gives

    partial u/partial x = (partial u/partial r)(x/r) - (partial u/partial theta)(y/r^2),
    partial u/partial y = (partial u/partial r)(y/r) + (partial u/partial theta)(x/r^2).

In summary,

    y (partial u/partial x) - x (partial u/partial y) = -((x^2 + y^2)/r^2)(partial u/partial theta) = -(partial u/partial theta),

and the transformed differential equation is

    -(partial u/partial theta) = r(cos(theta) + sin(theta)).

**(b) (1p)** Integrating both sides with respect to theta gives

    u(r, theta) = -r(sin(theta) - cos(theta)) + C(r),

for some differentiable function C : R -> R. Backwards substitution with theta = arctan(y/x) and r = sqrt(x^2 + y^2) gives u = x - y + C(sqrt(x^2 + y^2)).

**Svar:** (a) -(partial u/partial theta) = r(cos(theta) + sin(theta)). (b) x - y + C(sqrt(x^2 + y^2)) for some differentiable C : R -> R.

### Lösning 5
**(a) (1p)** All terms in the integrand except (1 - x^2 - y^2)^(-1/2) are continuous over the closed and bounded disk x^2 + y^2 <= 1, so the integrals of these terms are finite. With x = r cos(theta), y = r sin(theta),

    doubleintegral over D dA/sqrt(1 - x^2 - y^2)
        = integral(0 to 2pi) dtheta integral(0 to 1) r/sqrt(1 - r^2) dr
        = pi [ sqrt(1 - r^2) ] from r=1 to r=0 = pi.

Since lim(A_n + B_n) = lim A_n + lim B_n holds when both limits exist and are finite, the splitting of the integral is justified.

**(b) (4p)** The integral doubleintegral over D x^10 y^9 dA = 0 because the integrand is odd in y while D is symmetric in both x and y. The integral doubleintegral over D y sin(x y^9) dA = 0 because the integrand is odd in x. We compute doubleintegral over D x^2 dA with x = r cos(theta), y = r sin(theta):

    doubleintegral over D x^2 dA = integral(0 to 2pi) dtheta integral(0 to 1) r^2 cos^2(theta) r dr
        = integral(0 to 2pi) cos^2(theta) dtheta · integral(0 to 1) r^3 dr
        = [ (1/2)(theta + sin(theta) cos(theta)) ] from 0 to 2pi · [ r^4/4 ] from 0 to 1
        = pi/4.

Adding doubleintegral over D (1 - x^2 - y^2)^(-1/2) dA = pi, we get I = 5pi/4.

**Svar:** (b) 5pi/4.

### Lösning 6
**(a) (3p) Compute F'(x) if F(x) = integral(0 to x) (x - y) f(y) dy.**

Let u(x) = x and v(x) = x. Then

    F(x) = F(u(x), v(x)) = integral(0 to u(x)) (v(x) - y) f(y) dy.

By the chain rule,

    F'(x) = (partial F/partial u)(partial u/partial x) + (partial F/partial v)(partial v/partial x)
          = partial F/partial u + partial F/partial v,

where

    partial F/partial u = (v - u) f(u) = (x - x) f(x) = 0,

and

    partial F/partial v = integral(0 to u) partial/partial v (v - y) f(y) dy
                        = integral(0 to u) f(y) dy = integral(0 to x) f(y) dy.

In summary, F'(x) = integral(0 to x) f(y) dy.

**(b) (1p)** For example, f continuous on R. Then for every x in R the integral integral(0 to x) (x - y) f(y) dy exists, because the integrand is continuous over the bounded interval [0, x]. Also integral(0 to x) partial/partial x [(x - y) f(y)] dy = integral(0 to x) f(y) dy exists for the same reason. Finally integral(0 to x) |partial^2/partial x^2 [(x - y) f(y)]| dy is bounded, since that second derivative is 0. By the theorem in Section 13.6 of the course literature (9:e uppl.; motsvarar 14.6 i 10:e), differentiation through the integral sign as performed in (a) is permitted.

**(c) (1p)** Doing the same as in part (a) we arrive at

    F'(x) = integral(0 to x) ((x - y)^(n-2)/(n-2)!) f(y) dy.

Differentiating k times, for 1 <= k <= n - 1,

    F^(k)(x) = integral(0 to x) ((x - y)^(n-k-1)/(n-k-1)!) f(y) dy.

In particular, for k = n - 1,

    F^(n-1)(x) = integral(0 to x) ((x - y)^0/0!) f(y) dy = integral(0 to x) f(y) dy.

So

    F^(n)(x) = (d/dx) integral(0 to x) f(y) dy = f(x).

This holds for any n = 1, 2, ....

**Svar:** (a) integral(0 to x) f(y) dy. (b) e.g. f continuous. (c) f(x).
