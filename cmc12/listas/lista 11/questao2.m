function [alpha, T] = questao2()
% Projete a compensacao lag para reduzir o erro em regime pela metade.
% Considere a compensacao lag na seguinte forma:
% Clag = alpha * (T * s + 1) / (alpha * T * s + 1).
roots([1 0 13 0 -2880]);
wcp = 6.896219;
T = 10/wcp;
alpha = 81/5;

end