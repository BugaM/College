inicializarFrontal

out = sim('frontal.slx');
plot(out.x.time, out.x.signals.values);
hold on
grid on
ylim([0 1.2])

print -depsc2 2_1.eps