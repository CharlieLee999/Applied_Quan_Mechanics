L_x = 1e-9;
L_y = 2e-9;
x = linspace(0,L_x,1000);
y = linspace(0,L_y,1000);
num_level_1 = 1;
num_level_2 = 2;

[X, Y]  = meshgrid(x, y);
[X_axis, Y_axis]  = meshgrid(x * 1e9, y * 1e9);
phi_1_1 = phi_fun(num_level_1, num_level_1, L_x, L_y, X, Y);
% phi_1_1 = 1/2 * sqrt(L_x * L_y) * sin(num_level_1 * pi * X /L_x).* sin(num_level_1 * pi * Y/L_y);
mesh(X_axis, Y_axis, phi_1_1);
xlabel('X/(nm)')
ylabel('Y/(nm)')
zlabel('WaveFunction')
title('The lowest state \Psi_1_,_1')
saveas(gcf,'The lowest state','jpg')

figure()
phi_1_2 = phi_fun(num_level_1, num_level_2, L_x, L_y, X, Y);
mesh(X_axis, Y_axis, phi_1_2)
xlabel('X/(nm)')
ylabel('Y/(nm)')
zlabel('WaveFunction')
title('The second lowest state \Psi_1_,_2')
saveas(gcf,'The second lowest state 1','jpg')

figure()
phi_2_1 = phi_fun(num_level_2, num_level_1, L_x, L_y, X, Y);
mesh(X_axis, Y_axis, phi_2_1)
xlabel('X/(nm)')
ylabel('Y/(nm)')
zlabel('WaveFunction')
title('The second lowest state \Psi_2_,_1')
saveas(gcf,'The second lowest state 2','jpg')


function [phi] = phi_fun(num_level_x, num_level_y, width_x, width_y, x_list, y_list)
    phi = 0.5 / sqrt(width_x * width_y) * sin(num_level_x * pi * x_list/width_x).* sin(num_level_y * pi * y_list/width_y);
end 