function plothash(filename, hashfunc)

hashcount = hashtextfile(filename,hashfunc);

[H,maxH]= analysehashcount(hashcount);

plothashcount(hashcount,filename,hashfunc,H,maxH);

end