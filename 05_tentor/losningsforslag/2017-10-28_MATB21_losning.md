# Lösningsförslag — tentamen MATB21 Flervariabelanalys, lördag 28 oktober 2017
> Hämtat från Canvas, kurs 42188 (exam_171028_solutions.pdf). Skrivtid 08:00–13:00.
> Filen innehåller tentans uppgifter tillsammans med lösningsförslagen.
> Tentan utan lösningar: `../skarpa_tentor/2017-10-28_MATB21.md`

### Lösning 1
Consider f(x, y) = |(x, y)| - x = sqrt(x^2 + y^2) - x. Find its extreme points in the region |(x, y)| <= 2. Also classify other points of interest.

**Lösning.** We compute the gradient

    grad f = ( x/sqrt(x^2 + y^2) - 1,  y/sqrt(x^2 + y^2) ),   (x, y) != (0, 0)

which is non-existing at (0, 0). Hence this is a singular point. The critical points are all points on the line (0, 2) × {0} (i.e. the segment of the positive x-axis which lies within the circle). These points give value 0, which is also the value at the singular point. The boundary is parametrized by (2 cos theta, 2 sin theta) which gives

    f(2 cos theta, 2 sin theta) = 2 - 2 cos theta.

This clearly has a maximum at cos theta = -1, i.e. the point (-2, 0).

**Svar.** The extreme points are (-2, 0) (maximum) and [0, 2] × {0} (minimum). There is one singular point (0, 0) and critical points (x, 0) for 0 < x < 2.

### Lösning 2
A mountain has the shape of the graph of f(x, y) = (x + sin y) cos(pi x^2 + y). You are standing at the point (2, 0).
(a) In which direction is the steepest slope (upwards)?
(b) What is the slope in this direction (i.e. how many vertical meters do you gain for each horizontal meter)?
(c) You are out of shape so the maximum inclination you can handle is 45 degrees. In which direction should you move to have this inclination?

**Lösning.** (a) The gradient is

    grad f = ( cos(pi x^2 + y) - (x + sin y) 2 pi x sin(pi x^2 + y),
               cos y cos(pi x^2 + y) - (x + sin y) sin(pi x^2 + y) )

which evaluated at (2, 0) gives grad f(2, 0) = (1, 1). This is the direction of steepest ascent.

(b) The directional derivative at (2, 0) in direction (1, 1) is

    < grad f(2, 0), (1, 1)/|(1, 1)| > = sqrt(2).

You gain sqrt(2) ≈ 1.4 vertical meters per horizontal meter.

(c) You want the directional derivative to be 1. If v is a unit vector we get

    1 = < grad f(2, 0), v > = cos(phi) |(1, 1)|

where phi is the angle to (1, 1). This gives cos(phi) = 1/sqrt(2), solved by phi = ±pi/4. phi = +pi/4 gives v = (0, 1) and phi = -pi/4 gives v = (1, 0). Hence you can move either straight north or straight east.

(Alternatively, parametrize v by (cos theta, sin theta), giving 1 = cos theta + sin theta. Since sin(theta + pi/4) = (1/sqrt(2))(cos theta + sin theta), this gives sin(theta + pi/4) = 1/sqrt(2) with solutions theta = 0 and theta = pi/2.)

### Lösning 3
We reuse the function f from Problem 2.
(a) Write a formula for the tangent plane at the point (2, 0).
(b) Write a formula for the second order Taylor approximation at the point (2, 0).
(c) Consider an integral doubleintegral g(u, v) du dv and the change of variables u = f(x, y), v = xy. What is the Jacobian of this change of variables at the point (x, y) = (2, 0)?

**Lösning.** (a) The tangent plane is

    f(2, 0) + f_x(2, 0)(x - 2) + f_y(2, 0)(y - 0) = 2 + (x - 2) + y = x + y.

(b) Some messy computations yield

    f_xx(2, 0) = -32 pi^2,  f_xy(2, 0) = -8 pi,  f_yy(2, 0) = -2.

The Taylor expansion is thus

    2 + (x - 2) + y + (1/2)( -32 pi^2 (x-2)^2 + 2(-8 pi)(x-2)y + (-2)y^2 )
      = x + y - 16 pi^2 (x-2)^2 - 8 pi (x-2) y - y^2.

(c) We have u_x(2,0) = 1, u_y(2,0) = 1, v_x(2,0) = 0 and v_y(2,0) = 2, so the Jacobian matrix is

    partial(u,v)/partial(x,y) = [ 1  1 ]
                                [ 0  2 ]

which gives the Jacobian 2. However, we are interested in the Jacobian of partial(x,y)/partial(u,v), which by the chain rule is 1/2.

### Lösning 4
Compute, as far as possible, the derivative of the function

    f(r) = integral(0 to r) e^(-r x^2) dx.

Justify your computations. (Hint: you cannot compute the integral, so the final answer will also contain an integral.)

**Lösning.** Introducing F(u, v) = integral(0 to u) e^(-v x^2) dx we have

    f'(r) = F_u(r, r) + F_v(r, r).

By the fundamental theorem of calculus, F_u(u, v) = e^(-v u^2), and

    F_v(u, v) = integral(0 to u) partial/partial v e^(-v x^2) dx = integral(0 to u) -x^2 e^(-v x^2) dx

(e.g. since e^(-v x^2) and its v-derivative are continuous). Summing up,

    f'(r) = e^(-r^3) - integral(0 to r) x^2 e^(-r x^2) dx.

### Lösning 5
A body B is defined by 0 <= x <= cos y where -pi/2 <= y <= pi/2, and |z| <= x^2. Compute

    tripleintegral over B sin y dx dy dz.

**Lösning.** Iterated integration in the order dz dx dy gives

    tripleintegral over B sin y dx dy dz
      = integral(-pi/2 to pi/2) integral(0 to cos y) integral(-x^2 to x^2) sin y dz dx dy
      = integral(-pi/2 to pi/2) integral(0 to cos y) 2x^2 sin y dx dy
      = integral(-pi/2 to pi/2) (2/3)(cos y)^3 sin y dy
      = [ -2(cos y)^4 / 12 ] from -pi/2 to pi/2 = 0.

(This could also have been seen from the symmetry of the domain in y together with sin y being odd.)

### Lösning 6
Compute doubleintegral over R^2 e^(-x^2 - y^2) by using polar coordinates. Then write an expression for it using iterated integration, and in this way find the value of integral over R e^(-x^2) dx.

**Lösning.** The function is positive so iterated integration and coordinate changes are allowed (although the domain is unbounded). Thus

    doubleintegral over R^2 e^(-x^2-y^2) dx dy
      = integral(-oo to oo) e^(-x^2) dx · integral(-oo to oo) e^(-y^2) dy
      = ( integral(-oo to oo) e^(-x^2) dx )^2.

On the other hand,

    doubleintegral over R^2 e^(-x^2-y^2) dx dy
      = integral(0 to 2pi) integral(0 to oo) e^(-r^2) r dr dtheta
      = 2pi [ e^(-r^2)/(-2) ] from 0 to oo = pi.

Hence integral(-oo to oo) e^(-x^2) dx = sqrt(pi).
