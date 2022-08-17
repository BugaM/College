function controlador = projetarControladorPosicaoOtimizacao(requisitos, controladorCorrente, planta)
% controlador = projetarControladorPosicaoAnalitico(requisitos, planta)
% projeta o controlador de posicao atraves de otimizacao. A
% struct requisitos eh:
% requisitos.wb: requisito de banda passante.
% requisitos.GM: requisito de margem de ganho.
% requisitos.PM: requisito de margem de fase.
% requisitos.fs: requisito de taxa de amostragem.
% A struct controladorCorrente eh dada por:
% controlador.K: ganho proporcional do controlador de corrente.
% controlador.alpha: parametro alpha da compensacao lead.
% controlador.Tl: parametro Tl da compensacao lead.
% controlador.T: periodo de amostragem do controlador de corrente.
% A struct planta contem os parametros da planta e pode ser obtida atraves
% de planta = obterPlantaServoPosicao().
% A saida da funcao eh a struct controlador:
% controlador.Kp: ganho proporcional do controlador de posicao.
% controlador.Kd: ganho derivativo do controlador de posicao.
% controlador.a: frequencia de corte do filtro do termo derivativo.
% controlador.T: periodo de amostragem do controlador de posicao.

controlador0 = projetarControladorPosicaoAnalitico(requisitos, planta);
parametros0 = [controlador0.Kp; controlador0.Kd];
par = fminsearch(@(parametros) custoControladorPosicao(requisitos, controladorCorrente, planta, parametros), parametros0);

wbreq = requisitos.wb;


controlador.Kp = par(1);
controlador.Kd = par(2);
controlador.a = wbreq * 10.0;
controlador.T = 1.0 / requisitos.fs;

end

function J = custoControladorPosicao(requisitos, controladorCorrente, planta, parametros)

wbreq = requisitos.wb;
PMreq = requisitos.PM;


controladorPosicao.Kp = parametros(1);
controladorPosicao.Kd = parametros(2);
controladorPosicao.a = wbreq * 10.0;
controladorPosicao.T = 1.0 / requisitos.fs;


[Ga, Gf] = obterMalhaPosicao(controladorPosicao, controladorCorrente, planta);



wb = bandwidth(Gf);
[~, PM, ~, ~] = margin(Ga);

J = (wbreq - wb)^2 + (PMreq - PM)^2;

end