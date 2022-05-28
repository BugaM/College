function dinamica = obterMalhaVertical(controlador, planta)
% dinamica = obterMalhaVertical(controlador, planta) obtem a dinamica da
% malha vertical. A struct controlador possui os seguintes parametros:
% controlador.Kp: ganho proporcional.
% controlador.Ki: ganho integrativo.
% controlador.Kd: ganho derivativo.
% A struct planta tem os seguintes parametros:
% planta.m: massa.
% planta.J: inercia.
% planta.l: distancia entre os rotores.
% planta.g: aceleracao da gravidade.
% A saida dinamica eh a dinamica da malha vertical na forma de funcao de
% transferencia.

m = planta.m;
Kp = controlador.Kp;
Ki = controlador.Ki;
Kd = controlador.Kd;
s = tf('s');

dinamica = Ki/(m*s^3 + Kd*s^2 + Kp*s + Ki);

end