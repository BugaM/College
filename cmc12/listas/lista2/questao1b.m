function q = questao1b()
% Retorne o valor da carga do capacitor no tempo t = 0.02 s. Use SI.
C = 10^(-6);
V = 5;
R = 10^3;
t = 0.02;

q = C*V*(1 - exp(-t/(R*C)));


end