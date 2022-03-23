
defhashfuncs

% compare as funcoes que consideram apenas o 1o caractere X funcoes que
% somam o valor ASCII de todos os caracteres.
% (1.1) (pergunta mais simples e mais geral) porque necessitamos escolher uma boa funcao de hashing, e quais as consequencias de escolher uma funcao ruim?
% (1.2) porque ha uma diferenca significativa entre considerar apenas o 1o caractere ou a soma de todos?
% (1.3) porque um dataset apresentou resultados muito piores do que os outros, quando consideramos apenas o 1o caractere?
hashfunctions1 = {mod1stChar29, modsumchar29};

% (2.1) com uma tabela de hash maior, o hash deveria ser mais facil. afinal temos mais
% posicoes na tabela para espalhar as strings. No entanto, uma regra comum
% eh usar um tamanho primo (e.g. 29) e nao um tamanho com varios divisores,
% como 30. Que tipo de problema isto evita, e porque nao eh tao relevante
% no nosso exemplo?
% (2.2) note que o arquivo mod30 foi feito para atacar um hash por divisao de tabela de tamanho 30. 
% como este ataque funciona?
% (dica: plote a tabela de hash para a funcao correta e arquivo correto, exemplo em checkhashfunc)
hashfunctions2 = {mod1stChar29, modsumchar29,mod1stChar30, modsumchar30};

% (3) com tamanho 997 para a tabela de hash ao inves de 29, nao deveria ser mais facil?
% afinal, temos 997 posicoes para espalhar numeros ao inves de 29. 
% porque os resultados estranhos para modsumchar1k, e porque a versao com
% produtorio eh melhor? porque este problema nao apareceu com tamanho 29?
% dica: novamente plote a tabela de hash para as funcoes e arquivos
% relevantes para entender o que acontece.
hashfunctions3 = {modprodchar1k,modsumchar29,modsumchar1k};

% (4) hash por divisao eh o mais comum, mas outra alternativa eh hash de multiplicacao
% eh uma alternativa viavel? porque hashing por divisao eh mais comum?
hashfunctions4 = {modsumchar29,mult_m29,modsumchar1k};

filenames = { 'data/random.txt', 'data/startend.txt' , 'data/length8.txt' 'data/mod30.txt' };
filenames{end+1} = 'data/huckfinn.txt';

% change hashfunction1 to hashfunctionX to run other exercises.
comparehashfuncs(hashfunctions5, filenames);
