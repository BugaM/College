function deltaPM = questao4()
% Calcule a perda de margem de fase provocada pelos atrasos na malha.
% Retorne um valor positivo em graus.

% 3.81
a = 0.05^2 -1.35^2;
roots([1 0 a 0 -1]);
wcp = 1.504018777563671;
tau = 50/1000;
T = 1/10;
deltaPM = wcp*(tau + T/2) * 180/pi;

end