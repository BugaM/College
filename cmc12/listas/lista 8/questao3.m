function [magnitude, phase] = questao3(sys, w)
% Calcula valores de magnitude e fase de uma aproximacao para tracado
% manual do diagrama de Bode da funcao de transferencia sys nas frequencias
% das por w. Os valores de magnitude e fase sao dados em dB e graus,
% respectivamente. Note que
% magnitude(i) = |sys(j * w(i)|,
% fase(i) = fase(sys(j * w(i)).

magnitude = 1:1:length(w);
phase = 1:1:length(w);

zs = sort(abs(zero(sys)));
poles = sort(abs(pole(sys)));
zm= 1; 
pm = 1;

zpida = 1;
zpvolta = 1;
zpv = 1;
ppida = 1;
ppvolta = 1;
ppv = 1;

% Magnitude:
phase(1) = angle(evalfr(sys, 0));
magnitude(1) = dcgain(sys);
for i=2:length(w) 
    
    while (zm <= length(zs) && w(i) > zs(zm))
        zm = zm + 1;
    end
    while (pm <= length(poles) && w(i) > poles(pm))
        pm = pm + 1;
    end

    while (zpida <= length(zs) && w(i) > 0.1*zs(zpida))
        zpida = zpida + 1;
        zpv = zpv + 1;
    end
    while (zpvolta ~= zpida && w(i)>10*zs(zpvolta))
        zpvolta = zpvolta + 1;
        zpv = zpv -1 ;
    end
    
    while (ppida <= length(poles) && w(i) > 0.1*poles(ppida))
        ppida = ppida + 1;
        ppv = ppv + 1;
    end
    while (ppvolta ~= ppida && w(i)>10*poles(ppvolta))
        ppvolta = ppvolta + 1;
        ppv = ppv -1 ;
    end
    
    
    thetam = (zm-pm)*20;
    thetap = (zpv-ppv)*45;
    if (w(i-1) > 0)
        magnitude(i) = magnitude(i-1) + thetam*(log10(w(i)/w(i-1)));
        phase(i) = phase(i-1) + thetap*(log10(w(i)/w(i-1)));
    else
        magnitude(i) = magnitude(i-1);
        phase(i) = phase(i-1);
    end
end

end
