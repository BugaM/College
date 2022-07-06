planta = obterPlantaLongitudinal;
% step(planta, 5000)
% grid on;

A = planta.A;
B = planta.B;
C = planta.C;
D = planta.D;
[Num, Den] = ss2tf(A,B,C,D);
numTfq = Num(1,:);
numTftheta = Num(2,:);
numTfh = Num(3,:);
denTf = Den;
Gq = -tf(numTfq,denTf);
Gh = -tf(numTfh,denTf);
Gtheta = tf(numTftheta,denTf);

s = tf('s');
Ktheta = 7.0286;
Kq = Ktheta*0.28;

Gat = Ktheta*Gtheta/ (Ktheta*Gtheta + Kq*s*Gtheta - 1);
figure(1)
step(-Gtheta)
grid on
figure(2)
step(Gat)
stepinfo(Gat)
grid on