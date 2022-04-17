inicializarFrontal

out = sim('frontal.slx');
plot(out.x.signals.values, out.x.time);
ylabel('t(s)')
xlabel('x(m)')
hold on
grid on

print -depsc2 2_1.eps