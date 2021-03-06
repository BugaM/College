function theta = pendulo(m, l, b, g, theta0, dtheta0, t)
% Realiza a simulacao de um pendulo simples amortecido que possui a
% seguinte EDO: m l theta'' + b theta' + m g sin theta = 0. theta0 e
% dtheta0 representam angulo e velocidade angular iniciais do pendulo.
% t representa o vetor de tempos [t0, t1, t2, ..., tf] em que se deseja
% fazer as simulacoes. A saida theta contem angulo e velocidade angular
% para cada instante de tempo conforme no seguinte formato:
% theta = [theta(t0), dtheta(t0);
%          theta(t1), dtheta(t1);
%          theta(t2), dtheta(t2);
%          ...      , ...       ;
%          theta(tf), dtheta(tf)];

% resolver EDO numericamente
vtheta0 = [theta0, dtheta0];

f = @(t,theta) [theta(2);(-b*theta(2)-m*g*sin(theta(1)))/(m*l)];
[~, theta] = ode45(f, t, vtheta0);
plot(t,theta(:,1))
end