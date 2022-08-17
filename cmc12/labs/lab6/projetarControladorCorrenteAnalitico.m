function controlador = projetarControladorCorrenteAnalitico(requisitos, planta)
% controlador = projetarControladorCorrenteAnalitico(requisitos, planta)
% projeta o controlador de corrente atraves de um metodo analitico. A
% struct requisitos eh:
% requisitos.wb: requisito de banda passante.
% requisitos.GM: requisito de margem de ganho.
% requisitos.PM: requisito de margem de fase.
% requisitos.fs: requisito de taxa de amostragem.
% A struct planta contem os parametros da planta e pode ser obtida atraves
% de planta = obterPlantaServoPosicao().
% A saida da funcao eh a struct controlador:
% controlador.K: ganho proporcional do controlador de corrente.
% controlador.alpha: parametro alpha da compensacao lead.
% controlador.Tl: parametro Tl da compensacao lead.
% controlador.T: periodo de amostragem do controlador de corrente.

wbReq = requisitos.wb;
PMReq = requisitos.PM;

L = planta.L;
R = planta.R;

% Utilizando wbReq
controlador.K = -L * wbReq^2 + sqrt(2 * L^2 * wbReq^4 + R^2 * wbReq^2);

s = tf('s');
G = controlador.K/(s* (L*s + R));
[~,Pm,~,Wcp] = margin(G);
% Utilizando PMReq
phiMax = (PMReq - Pm)*pi/180;
controlador.alpha = (1-sin(phiMax))/(1+sin(phiMax));
controlador.Tl = 1/(Wcp*sqrt(controlador.alpha));

controlador.T = 1.0 / requisitos.fs;


end