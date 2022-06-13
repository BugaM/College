function [phi, im, K] = questao1()
% Determinar:
% - O angulo de saida phi (em graus) do ramo do lugar geometrico das raizes
% (LGR) que comeca no polo -1 + j.
% - O ponto de cruzamento im do mesmo ramo com o eixo imaginario (i.e. o
% numero complexo no cruzamento eh im * j).
% - O ganho K assocado a esse ponto de cruzamento.

phi = 90 - atan(1/9) * 180 / pi;
im = sqrt(22);
K = 24.4;

end
