function [Ga, Gf] = obterMalhaPosicao(controladorPosicao, controladorCorrente, planta)
% [Ga, Gf] = obterMalhaPosicao(controladorPosicao, controladorCorrente,
% planta) obtem as malhas aberta Ga e fechada Gf do servomotor de posicao.
% A struct controladorPosicao eh dada por:
% controladorPosicao.Kp: ganho proporcional do controlador de posicao.
% controladorPosicao.Kd: ganho derivativo do controlador de posicao.
% controladorPosicao.a: frequencia de corte do filtro do termo derivativo.
% controladorPosicao.T: periodo de amostragem do controlador de posicao.
% A struct controladorCorrente eh dada por:
% controlador.K: ganho proporcional do controlador de corrente.
% controlador.alpha: parametro alpha da compensacao lead.
% controlador.Tl: parametro Tl da compensacao lead.
% controlador.T: tempo de amostragem do controlador de corrente.
% A struct planta contem os parametros da planta e pode ser obtida atraves
% de planta = obterPlantaServoPosicao().

s = tf('s');

Kp = controladorPosicao.Kp;
Kd = controladorPosicao.Kd;
a = controladorPosicao.a;
Tp = controladorPosicao.T;

K = controladorCorrente.K;
alpha = controladorCorrente.alpha;
Tl = controladorCorrente.Tl;
Tc = controladorCorrente.T;

Kt = planta.Kt;
Jeq = planta.Jeq;
Beq = planta.Beq;
L = planta.L;
R = planta.R;
N = planta.N;
eta = planta.eta;

Cp = Kp + Kd*s*a/(s+a);
[NumPp, DenPp] = pade(Tp,2);
Ap = tf(NumPp,DenPp);

Cc = (1/s) * K * (Tl*s + 1)/(Tl*alpha*s + 1);
[NumPc, DenPc] = pade(Tc,2);
NAc = tf(NumPc,1);
DenAc= tf(DenPc,1);


P = 1/(L * s + R) * N*eta*Kt * 1/(Jeq*s + Beq) * 1/s;


Ga = minreal((Cp*Ap*Cc*NAc*P)/(DenAc*(1+N*Kt*P*s + Cc*NAc*P*(Jeq*s^2 + Beq*s)/(DenAc*N*eta*Kt))));
Gf = minreal(feedback(Ga,1));
end