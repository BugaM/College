function ftd = discretizarControladorCorrente(controlador)
% ftd = discretizarControladorPosicao(controlador) discretiza o controlador
% de corrente. A struct controlador eh dada por:
% controlador.K: ganho proporcional do controlador de corrente.
% controlador.alpha: parametro alpha da compensacao lead.
% controlador.Tl: parametro Tl da compensacao lead.
% controlador.T: periodo de amostragem do controlador de corrente.
% A saida ftd eh a funcao de transferencia discreta (no dominio z) do
% controlador de corrente.

K = controlador.K;
alpha = controlador.alpha;
Tl = controlador.Tl;
T = controlador.T;

s = tf('s');
C = K* (Tl*s + 1)/(alpha*Tl*s + 1) * 1/s;

ftd = c2d(C, T, 'Tustin');


end