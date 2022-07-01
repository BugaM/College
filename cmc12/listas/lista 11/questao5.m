function u = questao5(wn, xi, T, ua, uaa, e, ea, eaa)
% Escreva a expressao da lei de controle discreta para implementacao em
% computador de um filtro com funcao de transferencia de sistema de segunda
% ordem padrao.
% wn: frequencia natural.
% xi: fator de amortecimento.
% T: periodo de amostragem.
% ua: u[k-1].
% uaa: u[k-2].
% e: e[k].
% ea: e[k-1].
% eaa: e[k-2].
% u: u[k].

a = 4 + 4*xi*wn*T + T^2*wn^2;
b = 2*T^2*wn^2 - 8;
c = 4 - 4*xi*wn*T + T^2*wn^2;

u = -b/a*ua -c/a* uaa + T^2*wn^2/a*(e + 2*ea + eaa);
end
