x = 0:0.1:10;


m = 1;
b = 1.4;
k = 1;
f = 1;

r1 = (-b + sqrt(b^2 -4*k*m))/(2*m);
r2 = (-b - sqrt(b^2 -4*k*m))/(2*m);

alfa = -b/(2*m);
beta = sqrt(4*m*k - b^2)/ (2*m);


C2 = -f/k;
C1 = -C2 * alfa/beta;

y = exp(alfa.*x).*(C1*sin(beta.*x) + C2*cos(beta.*x)) + f/k;
plot(x,y)
hold on;
grid on;
xlabel ('Tempo (s)')
ylabel ('Posição (m)')
% print -dpng -r400 questao2.png
