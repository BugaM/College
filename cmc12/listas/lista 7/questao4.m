function [Kp, Ki] = questao4()
% Projetar um controlador PI para alocar polos complexo-conjugados em
% posicoes tais que wn = 6 rad/s e xi = 0.7.
h = sqrt(6^2 - 4.2^2);
b = 50;
m = 1000;
wn = 6;
z= -(4.2^2 + h^2)/ (8.4 + b/m);
R = sqrt(z*(z+b/m));
l = sqrt(h^2 + (4.2-b/m)^2);
Kp = m*wn*l/R;
Ki = - Kp*z;
end
