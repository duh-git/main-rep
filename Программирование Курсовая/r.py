from random import randint
l_in = ['Frontend', 'Backend', 'Fullstack', 'Тестировщик', 'Менеджер проекта',
        'Designer', 'Системный администратор', 'Teamlead']
# l_in = ['Junior', 'Middle', 'Senior']
l_out = []
for i in range(50):
    x = randint(0, len(l_in)-1)
    l_out.append(l_in[x])

for i in l_out:
    print(i)

