function ts = questao2(sys)
% Determinar numericamente o tempo de acomodacao de 2% ts do sistema
% dinamico sys
[~, t] = step(sys);
tinf = 10*t(length(t));
t = 0:0.001:tinf;
[y, ~] = step(sys, t);
yinf = y(length(y));
i = 1;
ts = 0;
for time = t
    j = 0;
    for timelim = time:0.001:tinf
        if abs(y(i + j) - yinf) > 0.02*yinf
            ts = 0;
            break
        end
        ts = time;
        j = j + 1;
    end
    if ts ~= 0
        break
    end
    i = i + 1;
end
end

