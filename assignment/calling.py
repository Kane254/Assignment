from functions import calculator, oddoreven, get_first_element, greet_user
calculator()
oddoreven()
get_first_element([10, 20, 30, 40])
greet_user()

from classes import workers, cars, randomnumbers

wrk1 = workers('Kane', 'Nyamai', 20, 90000)

wrk2 = workers('James', 'Mailu', 2, 80000)

car1 = cars('Toyota', 'crown')

car2 = cars('Toyota', 'Land cruiser')

rand = randomnumbers(1, 1000)


print(wrk1.salary)
wrk1.salary_decreament()
print(wrk1.salary)

print(car1.make)
print(car2.model)

