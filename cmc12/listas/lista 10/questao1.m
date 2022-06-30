function [GM, PM, wcg, wcp] = questao1(mag, fase, w)
% [GM, PM, wcg, wcp] = questao1(mag, fase, w) determina as margens de ganho
% e de fase a partir da resposta em frequencia de um sistema. mag (dB) e
% fase (graus) representam as magnitudes e fase da resposta em frequencia
% considerando as frequencias dadas por w (rad/s). GM e PM sao as margens
% de ganho e de fase, respectivamente, que sao medidas em wcg e wcp,
% respectivamente.

wcg = interp1(fase,w,-180);
aux = abs(10^(interp1(w, mag, wcg)/20));
GM = 20*log10(1/aux);


wcp = interp1(mag, w, 0);
PM = 180 + interp1(w, fase, wcp);



end