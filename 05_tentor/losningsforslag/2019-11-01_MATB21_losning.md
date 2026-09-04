# Lösningsförslag — tentamen MATB21 Flervariabelanalys, fredag 1 november 2019
> Hämtat från Canvas, kurs 42188 (exam_191101solutions-1.pdf).
> Tentan utan lösningar: `../skarpa_tentor/2019-11-01_MATB21.md`

### Lösning 1
**(a)** The factor comes from the determinant of the derivative (Jacobi) matrix

    [ cos(theta)   -r sin(theta) ]
    [ sin(theta)    r cos(theta) ]

The determinant of this matrix at a point (r, theta) controls the ratio of the size of a small set including (r, theta) and its image in the (x, y)-plane. This ratio is clearly unaffected by changes in theta, since this amounts to rotating the given set around the origin.

**(b)** Changing to polar coordinates, the line x/sqrt(3) <= y is equivalent to theta >= arctan(1/sqrt(3)) = pi/6, and likewise y <= sqrt(3) x corresponds to theta <= pi/3. We get, by iterated integration,

    doubleintegral over E arctan(sqrt(x^2 + y^2)) dA
        = integral(pi/6 to pi/3) integral(1 to sqrt(3)) arctan(r) · r dr dtheta
        = (pi/6) integral(1 to sqrt(3)) r arctan(r) dr.

The remaining integral is evaluated by partial integration:

    integral(1 to sqrt(3)) r arctan(r) dr
        = [ (r^2/2) arctan(r) ] from 1 to sqrt(3) - integral(1 to sqrt(3)) (r^2/2)/(1 + r^2) dr
        = (3/2)(pi/3) - (1/2)(pi/6) - (1/2) integral(1 to sqrt(3)) (1 - 1/(1 + r^2)) dr
        = 5pi/12 - (1/2)(sqrt(3) - 1) + (1/2)[arctan(r)] from 1 to sqrt(3)
        = (1/2)(pi + 1 - sqrt(3)).

### Lösning 2
**(a)** If we set x(t) = (t, t^2, (2/3)t^3), the velocity at t_0 is

    dx/dt (t_0) = (1, 2t_0, 2t_0^2).

The speed is ||dx/dt (t_0)|| = sqrt(1^2 + (2t_0)^2 + (2t_0^2)^2).

**(b)** Call the trajectory y(t). Then

    y(t) = x(1) + (dx/dt (1))(t - 1) = (1 + (t-1), 1 + 2(t-1), 2/3 + 2(t-1)),

i.e. y(t) = (t, 2t - 1, 2t - 4/3).

**(c)** The length is given by integrating the speed:

    l = integral(0 to 1) sqrt(1 + 4t^2 + 4t^4) dt = integral(0 to 1) (1 + 2t^2) dt
      = [ t + 2t^3/3 ] from 0 to 1 = 5/3.

### Lösning 3
**(a)** By the chain rule,

    (d/dt) f(x(t)) at t=1 = < grad f(x(1)), dx/dt (1) > = < grad f(1,1,1), (2, -3, 1) > = 5.

**(b)** The tangent plane has the formula

    T(x, y) = g(3, -4) + g_x(3, -4)(x - 3) + g_y(3, -4)(y + 4)
            = 3/5 + (16/125)(x - 3) + (12/125)(y + 4)
            = 3/5 + (16/125)x + (12/125)y.

**(c)** Writing the tangent plane as z - (16/125)x - (12/125)y = -3/5, we immediately see that N = (125, -16, -12) is a normal vector.

### Lösning 4
**(a)** Clearly not, since (x, y) and (x, -y) map to the same point.

**(b)** The codomain is s >= t^3, and the inverse is given by x = t, y = sqrt((s - 2t^3)/3).

**(c)** Let ũ be defined by ũ(s, t) = u(x, y). By the chain rule,

    partial u/partial x = (partial ũ/partial s)(partial s/partial x) + (partial ũ/partial t)(partial t/partial x),

so partial u/partial x = 6x^2 (partial ũ/partial s) + partial ũ/partial t, and similarly partial u/partial y = 6y (partial ũ/partial s). With this, the equation reduces to

    y (partial ũ/partial t) = 0,

which implies partial ũ/partial t = 0 since y > 0. Hence ũ does not depend on t and must have the form ũ(s, t) = phi(s) for some function phi. Since u is supposed to be C^2, phi must be C^2 as well. The general solution is

    u(x, y) = phi(2x^3 + 3y^2),   phi in C^2.

### Lösning 5
The cone is given by z = 3 sqrt(x^2 + y^2) over a disc of radius h/3. The surface-area formula gives

    S = doubleintegral over {x^2+y^2 <= h^2/9} sqrt( 1 + (3x/sqrt(x^2+y^2))^2 + (3y/sqrt(x^2+y^2))^2 ) dA
      = doubleintegral over {x^2+y^2 <= h^2/9} sqrt(10) dA
      = pi sqrt(10) h^2 / 9.

### Lösning 6
**(a)** Clearly there are no singular points. Since

    partial f/partial x = 2x(1 - x^2 - 2y^2) e^(-x^2 + y^2)
    partial f/partial y = 2y(2 + x^2 + 2y^2) e^(-x^2 + y^2)

the critical points are P_1 = (-1, 0), P_2 = (0, 0) and P_3 = (1, 0), with function values e^(-1), 0 and e^(-1) respectively. A maximum/minimum can also occur on the boundary, the unit circle, parametrized by (cos theta, sin theta). This yields

    f(cos theta, sin theta) = (cos^2 theta + 2 sin^2 theta) e^(-cos^2 theta + sin^2 theta)
                            = (1 + sin^2 theta) e^(-1 + 2 sin^2 theta).

Now sin^2 theta takes values in [0, 1] and the function t -> (1 + t)e^(-1 + 2t) is clearly increasing there, hence the maximum value on the circle is attained at sin^2 theta = 1, i.e. (x, y) = (0, ±1). The value there is 2e. We also see that P_1 and P_3 are minima on the circle.

**Svar:** The maximum is 2e and the minimum is 0.

**(b)** The function is a product of two non-negative functions, and hence non-negative. It follows that 0 is the global minimum. The global maximum is infinite, as seen e.g. by considering lim_(t->oo) f(0, t).

### Lösning 7
The limit along either coordinate axis is clearly 0. Considering (x, y) = (t^2, t) we get t^(2+alpha)/t^4, so the limit along this curve differs whenever alpha <= 2. Hence we must have alpha > 2.

Suppose now that alpha = 2 + epsilon where epsilon > 0. Then, by the inequality in the hint,

    | x |y|^alpha | = |x| |y|^2 |y|^epsilon <= (x^2 + y^4) |y|^epsilon.

It follows that x|y|^alpha / (x^2 + y^4) <= |y|^epsilon, whose limit is 0 as (x, y) -> 0.

**Svar:** alpha > 2.
