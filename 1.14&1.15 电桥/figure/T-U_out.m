x = [0.54 21.4 40.75 50.18 60.4 70.4 80 90.45 99.95]
y = [0.04 13.87 27.68 34.42 41.67 48.69 55.37 62.73 69.29]
scatter(x,y,'*')

p = polyfit(x,y,1)
y1 = polyval(p,x)

xlabel('T(^{\circ} C)')
ylabel('U_{out}(mV)')
title('figure3: unbalanced bridge T-U_{out}')

hold on
plot(x,y1)
hold off