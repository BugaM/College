function [Kp, Kpsi] = questao5()
% Calcule os valores de Kp e Kpsi para que o sistema atenda aos requisitos
% no dominio da frequencia.
wb = 6;
v = 1;
Mr = 10^(0.3546/20);
% roots([1 0 -1 0 1/(4*Mr^2)]);
xi = 0.6;
wn = wb/(sqrt(1-2*xi^2+ sqrt(4*xi^4 - 4*xi^2 +2)));
Kpsi = 2*xi*wn;
Kp = wn^2/(Kpsi * v);
end
