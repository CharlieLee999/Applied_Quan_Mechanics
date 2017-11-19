L = 1e-9;
x = linspace(0,L,1000);
num_level_1 = 1;
num_level_2 = 2;
phi_1 = phi_fun(num_level_1, L, x);
P_1 = plot(x * 1e9,phi_1,'--k');
P_1.LineWidth = 2;
hold on


phi_2 = phi_fun(num_level_2, L, x);
P_2 = plot(x * 1e9, phi_2,'k');
P_2.LineWidth = 2;
xlabel('X/(nm)')
ylabel('WaveFunction')
legend('Lowest state', 'Second lowest state')
title('Lowest two state')
saveas(gcf,'Lowest_Two_State','jpg')
function [phi] = phi_fun(num_level, width, x_list)
    phi = sqrt(2/width) * sin(num_level * pi * x_list/width);
end 

