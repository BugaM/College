function dinamica = obterMalhaHorizontal(controladorX, controladorTheta, planta)
% dinamica = obterMalhaHorizontal(controladorX, controladorTheta, planta)
% obtem a dinamica da malha horizontal. As structs controladorX e 
% controladorTheta possuem a seguinte estrutura:
% controlador.Kp: ganho proporcional.
% controlador.Ki: ganho integrativo.
% controlador.Kd: ganho derivativo.
% A struct planta tem os seguintes parametros:
% planta.m: massa.
% planta.J: inercia.
% planta.l: distancia entre os rotores.
% planta.g: aceleracao da gravidade.
% A saida dinamica eh a dinamica da malha horizontal na forma de funcao de
% transferencia.

Kp = controladorX.Kp;
Ki = controladorX.Ki;
Kd = controladorX.Kd;
g = planta.g;

Gtheta = obterMalhaArfagem(controladorTheta, planta);
s= tf('s');
dinamica = Ki*Gtheta*g/(s^3 + Gtheta*g*(Kd*s^2 + Kp*s + Ki));

end