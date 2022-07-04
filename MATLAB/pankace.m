% take input coffee convert to code 
% and store in a variable
coffee = input('Enter the coffee you want to order: ','s');
if strcmp(coffee,'Cappuccino')
    coffee = 'Cappuccino';
    fprintf('JavaScript: %s\n', coffee);
elseif strcmp(coffee,'Latte')
    coffee = 'Latte';
    fprintf('Typescript: %s\n', coffee);
elseif strcmp(coffee,'Espresso')
    coffee = 'Espresso';
    fprintf('Java: %s\n', coffee);
elseif strcmp(coffee,'Coffee')
    coffee = 'Coffee';
    fprintf('Code!: %s\n', coffee);
else
    fprintf('Invalid coffee selection\n');
end