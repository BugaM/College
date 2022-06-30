function [GR, GN, GD] = questao5(L, R, Kp, Ki, a)
% Determine a resposta em funcao de L, R, Kp, Ki e a. Escreva as funcoes de
% transferencia com o s de Laplace definido logo abaixo.

s = tf('s');
C = (Kp*s + Ki)/s;
F = Ki/(Kp*s + Ki);
G = 1/(L*s + R);
Fm = a/(s+a);

GR = C*F*G/(1+C*Fm*G);
GD = G/(1+C*Fm*G);
GN = Fm*C*G/(1+Fm*C*G);
end