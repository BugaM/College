planta = obterPlantaLongitudinal;
% step(planta, 5000)
% grid on;

A = planta.A;
B = planta.B;
C = planta.C;
D = planta.D;
[Num, Den] = ss2tf(A,B,C,D)
numTfq = -Num(1,:)
numTftheta = -Num(2,:)
numTfh = -Num(3,:)
denTf = Den
Gq = tf(numTfq,denTf)
Gh = tf(numTfh,denTf)
Gtheta = tf(numTftheta,denTf)