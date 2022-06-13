function [Kmin, Kmax] = questao4()
% Calcule os valores minimo e maximo de K para que o sistema atenda aos
% requisitos.
b = 50;
m = 1000;
w = 10;
rts = roots([99 -2*b (-m^2*w^2 - b^2)]);
Kmax = max(rts);
Kmin = 9*b;

end
