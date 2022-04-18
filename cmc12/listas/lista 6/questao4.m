function [eInf, tr, ts] = questao4()
% Para o sistema
% Gf = 600 / ((s + 10) * (s + 20) * (s^2 + s + 4)),
% determine:
% eInf: erro em regime para entrada de degrau.
% tr: tempo de subida de 10% a 90%.
% ts: tempo de acomodacao de 2%.

xi = 1/2;
wn = 2;

eInf = 1/4;
tr = (2.16*xi + 0.60)/wn;
ts = 3.9/(xi*wn);

end
