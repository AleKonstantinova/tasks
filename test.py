per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = []
money = int(input("Введите сумму: "))
tcb = money/100*per_cent['ТКБ']+money
deposit.append(tcb)
skb = money/100*per_cent['СКБ']+money
deposit.append(skb)
vtb = money/100*per_cent['ВТБ']+money
deposit.append(vtb)
sber = money/100*per_cent['СБЕР']+money
deposit.append(sber)
deposit_max = str(max(deposit))

print("Максимальная сумма, которую вы можете заработать - "+ deposit_max)

