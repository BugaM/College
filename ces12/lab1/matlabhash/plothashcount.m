function plothashcount(hashcount, filename, hashfunc, entropy, maxEntropy)

funcname = func2str(hashfunc);

n = sum(hashcount);
m = length(hashcount);
hfig = figure; hold on; grid on; fs = 16;
bar(hashcount.*(100/n));
line([1 m],(100/m).*[1 1],'LineWidth',3);
xlabel(sprintf('bucket index ( %d buckets)', m),'FontSize',fs);
ylabel('%','FontSize',fs);
legend({'% of elements in bucket','uniform distribution'},'FontSize',fs);

title(sprintf('%s H %.3f  MaxH %.3f #keys %d load factor %.3f \n function %s',filename,entropy,maxEntropy,n,n/m,funcname),'FontSize',fs);
hold off;

end