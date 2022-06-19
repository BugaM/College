function questao3()

s = tf('s');
G = 1/((s+1)*(s^2 +4));

% Raio escolhido para desvio
r = 1/32;

figure;
hold on;

% Tracado do mapeamento de C1 e C2
w = (2+r):1e-3:100;
C1mx = zeros(size(w));
C1my = zeros(size(w));
for i=1:length(w)
    sm = evalfr(G, w(i) * 1j);
    C1mx(i) = real(sm);
    C1my(i) = imag(sm);
end
plot(C1mx, C1my, 'b', 'LineWidth', 2);
plot(C1mx, -C1my, 'r', 'LineWidth', 2);

% C3 eh um ponto em 0

scatter([0],[0],'g', '.')

% Tracado do mapeamento de C4 (desvio)
angulos = -pi/2:1e-3:pi/2;
C4mx = zeros(size(angulos));
C4my = zeros(size(angulos));
for i=1:length(angulos)
    sm = evalfr(G, 2j +r * exp(angulos(i) * 1j));
    C4mx(i) = real(sm);
    C4my(i) = imag(sm);
end
plot(C4mx, C4my, 'm', 'LineWidth', 2);

% Tracado do mapeamento de C4 (desvio)
angulos = -pi/2:1e-3:pi/2;
C5mx = zeros(size(angulos));
C5my = zeros(size(angulos));
for i=1:length(angulos)
    sm = evalfr(G, -2j +r * exp(-angulos(i) * 1j));
    C5mx(i) = real(sm);
    C5my(i) = imag(sm);
end
plot(C5mx, C5my, 'k', 'LineWidth', 2);

% Tracado do mapeamento de C6
w = (-2+r):1e-3:(2-r);
C6mx = zeros(size(w));
C6my = zeros(size(w));
for i=1:length(w)
    sm = evalfr(G, w(i) * 1j);
    C6mx(i) = real(sm);
    C6my(i) = imag(sm);
end
plot(C6mx, C6my, 'c', 'LineWidth', 2);

axis equal;
grid on;
xlabel('Re\{G(j \omega)\}');
ylabel('Im\{G(j \omega)\}');
legend('C1', 'C2', 'C3', 'C4', 'C5', 'C6')

end