function [wcp, ganhoPM] = questao4()
% Determinar analiticamente a frequencia de cruzamento wcp e o ganho (aumento) de
% margem de fase (em graus) ganhoPM devido a troca do sensor.

T = 1.5;
alpha = 0.1/1.5;
roots([0.01 0 1 0 -81 0 -36]);
wcp = 7.299581725967109;
t1 = 100/1000;
t2 = 30/1000;

ganhoPM = wcp * (t1-t2) * 180/pi;
end
