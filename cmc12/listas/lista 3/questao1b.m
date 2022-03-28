function Kp = questao1b(R, Kt, J, b, tau)
% Use as variaveis R, Kt, J, b e tau para definir a sua resposta.
% Talvez voce nao precise de todas as variaveis para definir sua resposta.
% Definir Kp, que eh retornado pela funcao.

Kff = R*b/Kt + Kt;
Kp = R*J/(tau*Kt) - Kff;

end
