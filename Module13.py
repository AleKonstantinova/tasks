ticketsCount = int(input('Введите количество желаемых билетов: '))
ageList = []

for i in range(ticketsCount):
    ageList.append(int(input('Введите возраст для билета: ')))

ticketsSum = 0
for i in ageList:
    if 18 <= i <= 25:
        ticketsSum = ticketsSum + 990
    elif i > 25:
        ticketsSum = ticketsSum + 1390

if ticketsCount > 3:
    ticketsSum = ticketsSum - (ticketsSum // 10)
    print('Сумма со скидкой: ', ticketsSum, 'рублей')

else:
    print(ticketsSum, 'рублей')

