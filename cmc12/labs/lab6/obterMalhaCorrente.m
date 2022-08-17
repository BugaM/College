function [Ga, Gf] = obterMalhaCorrente(controlador, planta)
% [Ga, Gf] = obterMalhaCorrente(controlador, planta) obtem as funcoes de 
% transferencia de malha aberta Ga e fechada Gf da malha de corrente.
% A struct controlador eh dada por:
% controlador.K: ganho proporcional do controlador de corrente.
% controlador.alpha: parametro alpha da compensacao lead.
% controlador.Tl: parametro Tl da compensacao lead.
% controlador.T: periodo de amostragem do controlador de corrente.
% A struct planta contem os parametros da planta e pode ser obtida atraves
% de planta = obterPlantaServoPosicao().

s = tf('s');
K = controlador.K;
alpha = controlador.alpha;
Tl = controlador.Tl;
T = controlador.T;

Cc = (1/s) * K * (Tl*s + 1)/(Tl*alpha*s + 1);
[NumP, DenP] = pade(T,2);
Ac = tf(NumP,DenP);
Gc = 1/(planta.L * s + planta.R);

Ga = minreal(Cc*Ac*Gc);
Gf = minreal(feedback(Ga,1));


% Implementar

end
