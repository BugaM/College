function [entropy, maxEntropy, n] = analysehashcount(hashcount)
    
    
    n = sum(hashcount);
    numbuckets = length(hashcount);
       
    hashcount = hashcount ./ n;
    
    entropy = H(hashcount(hashcount>0));% do not count empty buckets
    
    maxEntropy = H(ones(1,numbuckets).*(1/numbuckets));% entropy of uniform distribution
    
       

end