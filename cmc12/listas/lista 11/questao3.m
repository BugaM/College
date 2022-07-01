function [K, z, p] = questao3()
% Projetar controlador com funcao de transferencia
% C(s) = K * (s - z) / (s * (s - p)).
L = 0.1;
R= 1;
Kprime = 20;
roots([L^2 0 R^2 0 -400]);
wcp = 12.4962106768;
PM = 180 - 90 - atan(L*wcp/R) * 180/pi;

phiMax = (50 - PM + 10)*pi/180;

alpha =(1-sin(phiMax))/(1+sin(phiMax));
T = 1/(wcp*sqrt(alpha));

z = -1/T;
p = -1/(alpha*T);
K = Kprime/alpha;

end