function y = questao1(w, Au, phiu, Kp, Kd, m, b)
% Determinar a saida em regime permanente senoidal assumindo referencia
% nula e perturbacao senoidal na forma d(t) = Ad * sin(w * t + phid).

Ay = Au * abs(1/(-m*w^2 + (b + Kd)* w * 1j + Kp));
phiy = phiu + angle(1/(-m*w^2 + (b + Kd)* w * 1j + Kp));
y = @(t) Ay * sin(w*t + phiy);

end
