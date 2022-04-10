data = readmatrix('build/oak_search.csv');
x = linspace(0, 10^6);
fun = @(B,x) B(1).*log(x) + B(2);

figure (1)

hold on
grid on

beta = nlinfit(data(:,2), data(:,3), fun, [0,1]);
y = fun(beta, x);
plot (x,y, 'b')
beta = nlinfit(data(:,2), data(:,4), fun, [0,1]);
y = fun(beta, x);
plot (x,y, 'r')
scatter(data(:,2), data(:,3), 'b');
title('Busca')
scatter(data(:,2), data(:,4), 'r');
legend('Tempo busca STL', 'Tempo busca aluno')
xlabel('Número de elementos')
ylabel('Tempo')
print -dpng -r400 busca.png

figure (2)

beta = nlinfit(data(:,2), data(:,5), fun, [0,1]);
y = fun(beta, x);
plot (x,y, 'b')
hold on
grid on

beta = nlinfit(data(:,2), data(:,6), fun, [0,1]);
y = fun(beta, x);
plot (x,y, 'r')
scatter(data(:,2), data(:,5), 'b');


title('Inserção')
scatter(data(:,2), data(:,6), 'r');
legend('Tempo inserção STL', 'Tempo inserção aluno')
xlabel('Número de elementos')
ylabel('Tempo')
print -dpng -r400 insercao.png

