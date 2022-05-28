function controlador = projetarControladorVerticalAnalitico(requisitos, planta)
% controlador = projetarControladorVerticalAnalitico(requisitos, planta) 
% projeta o controlador vertical de forma analitica. As entradas da 
% funcao sao as structs requisitos e planta, que contem os requisitos e os 
% parametros da planta, respectivamente. Os requisitos sao:
% requisitos.tr: tempo de subidade de 0 a 100%.
% requisitos.Mp: sobressinal.
% A planta eh dada por:
% planta.m: massa.
% planta.J: inercia.
% planta.l: distancia entre os rotores.
% planta.g: aceleracao da gravidade.
% A saida da funcao eh a struct controlador com:
% controlador.Kp: ganho proporcional.
% controlador.Ki: ganho integrativo.
% controlador.Kd: ganho derivativo.

xi = -log(requisitos.Mp)/sqrt(pi^2 + log(requisitos.Mp)^2);
wn = (pi - acos(xi))/(requisitos.tr*sqrt(1-xi^2));
m = planta.m;

controlador.Kd = m*7*xi*wn;
controlador.Kp = m*wn^2*(1+10*xi^2);
controlador.Ki = m*5*xi*wn^3;

end
