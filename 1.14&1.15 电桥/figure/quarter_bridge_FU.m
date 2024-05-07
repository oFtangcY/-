x = [0 50 100 150 200 250 300 400 500]
y = [0 0.13 0.22 0.33 0.44 0.53 0.64 0.83 1.02]
scatter(x,y,'*')

p = polyfit(x,y,1)
y1 = polyval(p,x)

xlabel('F/gf')
ylabel('U_{out}/mV')
title('Figure4: quarter bridge F-U_{out}')

hold on
plot(x,y1)
hold off