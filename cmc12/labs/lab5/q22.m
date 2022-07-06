A = [-0.00643, 0.0263, 0, -32.2, 0;
     -0.0941, -0.624, 820, 0, 0;
     -0.000222, -0.00153, -0.668, 0, 0;
     0, 0, 1, 0, 0;
     0, -1, 0, 830, 0];
B = [0; -32.7; -2.08; 0; 0];
Z = [0;0;0;0;0];
Ktheta = 7.0286;
Kq = Ktheta*0.28;


B1 = B*Ktheta;
B2 = B*Kq;
Atheta = A + [Z Z Z B1 Z] + [Z Z B2 Z Z];
Btheta = -B1;

C = [0 0 0 0 1];
D = [0];

[Num, Den] = ss2tf(Atheta, Btheta, C, D);
Gh = tf(Num,Den)
% rltool(Gh)