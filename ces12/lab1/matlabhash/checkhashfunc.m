defhashfuncs

%hashfunc = modsumchar29;
hashfunc = modsumchar30;
%hashfunc = modsumchar1k;
%hashfunc = modprodchar1k;
%hashfunc = mult_m29;
%hashfunc = mult_m1k;
%hashfunc = mult_m1k_prod;
%filename = 'data/random.txt';
%filename = 'data/length8.txt';
filename = 'data/mod30.txt';
%filename = 'data/startend.txt';
%filename = 'data/huckfinn.txt';


plothash(filename,hashfunc);

%hashcount = hashtextfile(filename,hashfunc);
%[H,maxH]= analysehashcount(hashcount);
%plothashcount(hashcount,filename,hashfunc,H,maxH);