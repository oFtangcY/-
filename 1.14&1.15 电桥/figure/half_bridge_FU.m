x = [0 50 100 150 200 250 300 400 500]
y = [28.75 29.35 29.93 30.53 31.11 31.72 32.31 33.50 34.69]
scatter(x,y,'*')

p = polyfit(x,y,1)
y1 = polyval(p,x)

xlabel('F/gf')
ylabel('U_{out}/mV')
title('Figure9: full bridge F-U_{out}')

hold on
plot(x,y1)
hold off