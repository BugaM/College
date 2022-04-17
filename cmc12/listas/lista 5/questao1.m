function [p1, p2] = questao1(tr, Mp)
% Determinar os polos de um sistema de 2a ordem a partir do tempo de 
% subida de 0 a 100% tr e sobressinal Mp. Convencao:
% p1 = -sigma + wd * j,
% p2 = -sigma - wd * j,
% em que sigma > 0 e wd > 0.
wd = (pi - atan(-pi/(log(Mp))))/tr;
sigma = -log(Mp)*wd/pi;
p1 = -sigma + wd * 1j;
p2 = -sigma - wd * 1j;
end
