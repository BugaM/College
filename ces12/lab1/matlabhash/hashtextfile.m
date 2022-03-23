function [hashcount, n] = hashtextfile(filename,hashfunc)
n = 0;
hashcount(1) = 0;

% create map
keymap = containers.Map();

% we do not want to use dlmread or textscan, to avoid loading the whole
% file on memory. we want to read line by line
fid = fopen(filename);
tline = fgetl(fid);
while ischar(tline)
    if (~isKey(keymap,tline)) % do not count repeated lines
        keymap(tline) = 1;
        hashindex = hashfunc(tline);
        if (hashindex <= length(hashcount))
            hashcount(hashindex) = hashcount(hashindex)  + 1;
        else
            hashcount(hashindex) = 1;
        end
    end
    n = n + 1; % just count the number of lines
    tline = fgetl(fid);
end
fclose(fid);

end

% check: to count the number of different lines in a text file
% > sort huckfinn.txt -u | wc 
% > 5543    5543   40251