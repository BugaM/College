function [Kp, Kv] = questao2()
% Projetar Kp e Kv para que o carro autonomo tenha banda passante de 1 Hz e
% margem de fase de 60 graus. Usar formulas exatas, i.e. sem aproximacoes.

wb = 2*pi;
PM = pi/3;
m = 1000;
b = 50;

t = tan(PM);
xi = t/(2*(1+t^2)^(1/4));

wn = wb/(sqrt(1-2*xi^2 + sqrt(4*xi^4 - 4 * xi^2 + 2)));


Kv = 2*m*xi*wn - b;
Kp = m*wn^2/Kv;


end