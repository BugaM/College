function omegaInf = questao2b()
% Retorne a velocidade do motor em regime, considerando os parametros
% do motor Maxon RE-max 17 214897. Use SI.
V = 14.8;
R = 8.3;
Kt =10.7;
J = 0.868 *10^-3*10^-4;
b = 8.87*10^-8;

omegaInf = V*Kt/(R*b+Kt^2);

end