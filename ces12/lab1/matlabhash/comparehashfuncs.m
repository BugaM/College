% inputs:
% hashfuncs : cell array of function pointers - each function should be a hash
%             function: input is string, return value is bucket index 
% filenames : cell array of strings containing filenames.
%
% comparehashfuncs is a ploting function. the actual work is performed by 
% hashtextfile and analysehashcount functions. 
%
function hfig = comparehashfuncs(hashfuncs,filenames)

for ihf = 1:length(hashfuncs)
    for ifn = 1:length(filenames)
        
        hashcount = hashtextfile(filenames{ifn},hashfuncs{ihf});
        [H(ihf,ifn),maxH(ihf,ifn)]= analysehashcount(hashcount);
        %max percentage of elements in a single bucket above the uniform distribution.
        maxhashcount(ihf,ifn) = 100*((max(hashcount)/sum(hashcount)) - (1/length(hashcount)));
        
    end 
end

% some datasets may not fill all buckets.
% so we get the maximum among all datasets for each hash function
maxH = max(maxH,[],2);% get the max of each line

listlegends = {};
for ihf = 1:length(hashfuncs)
    listlegends{end+1} = func2str(hashfuncs{ihf});
end
listfilenames = [];
for ifn = 1:length(filenames)
    [filepath,name,ext] = fileparts(filenames{ifn}) ;
    listfilenames = [listfilenames '  ' name ]; 
end


y = [H maxH]';

hfig = figure; hold on; grid on; fs = 16;
bar(y);
legend(listlegends,'FontSize',fs);
xlabel([listfilenames '  MaxEntropy'],'FontSize',fs-1);
ylabel('Entropy (bits)','FontSize',fs);
title('Compare: hash function entropies','FontSize',fs);
hold off;

ydiff = [repmat(maxH,1,size(H,2)) - H]';

hfigdiff = figure; hold on; grid on; fs = 16;
bar(ydiff);
legend(listlegends,'FontSize',fs);
xlabel(listfilenames,'FontSize',fs-1);
ylabel('MaxEntropy - Entropy (bits)','FontSize',fs);
title('Compare: hash function LOST entropy','FontSize',fs);
hold off;

hfigmaxbuck = figure; hold on; grid on; fs = 16;
bar(maxhashcount');
legend(listlegends,'FontSize',fs);
xlabel(listfilenames,'FontSize',fs-1);
ylabel('max % in a bucket - (100/n)','FontSize',fs);
title('Compare: max % in a bucket minus the uniform distribution','FontSize',fs);
hold off;


end %comparefilenames