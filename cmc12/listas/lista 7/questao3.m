function K = questao3()
% Determinar K para se ter Mp = 0.0432.
Mp = 0.0432;
xi = - log(Mp)/sqrt(pi^2 + log(Mp)^2);
theta = atan(sqrt(26) - 5);
a = 10 * sin(theta)/sin(3*pi/4 - theta);
b = 10 * sin(pi/4)/sin(3*pi/4 - theta);
c = sqrt(8^2 + b^2 -16*b*cos(theta));
K = a*b*c/5;
end
