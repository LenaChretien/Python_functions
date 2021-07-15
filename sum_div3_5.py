# Sum up the numbers divisible by 3 or 5 from 1 to 999
Lst = range(1,999);
sum([element for element in Lst if element%3 == 0 or element%5 == 0])
