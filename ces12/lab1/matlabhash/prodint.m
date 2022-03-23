
% prod(v) may loose integer precision if result > 1e16 (due to double
% precison limits) Therefore, we use mod to keep the result below m^2
% it just multiplies all elements of v using mod(result, m^2) at each step
function res = prodint(v,m)
    res = 1;
    for i=1:length(v)
        res = mod(res * v(i),m^2);
    end
end