function [Kp, Kv] = questao2(R, Kt, J, b, wn, xi)
% Use as variaveis R, Kt, J, b, wn e xi para definir a sua resposta.
% Talvez voce nao precise de todas as variaveis para definir sua resposta.
% Definir Kp e Kv, que sao retornados pela funcao.

A = R*b/Kt + Kt;
B = R*J/Kt;


Kv =  2*xi*wn*B - A;
Kp = B*wn^2/Kv;

end
