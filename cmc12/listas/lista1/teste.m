vtheta0 = [0, 5];
m = 1;
g = 10;
l = 1;
b = 1;
t = 0:0.01:20;
f = @(t,theta) [theta(2);(-b*theta(2)-m*g*sin(theta(1)))/(m*l)];
[~, theta] = ode45(f, t, vtheta0);
theta(:,1)
plot(t, theta(:,1), 'r');
hold on;
grid on;
