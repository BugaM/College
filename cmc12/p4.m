s = tf('s');
t = 0:0.01:10;
u = t;
C = (5.489*s +10)/(0.2223*s+1);
Gy = 1/(s^2+2*s);

Ga = Gy*C;

Gf = Ga/(1+Ga);
figure(1);
lsim(Gf, u, t)
figure(2);
margin(Ga)
