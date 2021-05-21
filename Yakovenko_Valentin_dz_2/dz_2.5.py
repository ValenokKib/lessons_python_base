prices = [11.24, 25.56, 78.54, 20, 34, 69, 54.12, 62.52, 12.33,
          41.21, 45, 52, 24, 22, 26.55, 2.33, 56.52, 12.09, 58.23,
          96.66, 81.22, 55.77, 75.15, 81, 33.61, 91.11]

#print(len(prices))
#print(type(prices[11]))

for i in prices:
    r = int(i // 1)
    kk = i % 1
    kk = '{:.2f}'.format(kk)
    print('{} руб {} коп,  '.format(r, kk[2:]), end='')


print('\n\n Id основного спика: ', id(prices))
print(prices)
prices.sort()
print('\n Id отсортированного списка по возрастанию: ', id(prices))
print(prices)


new_list_prices = sorted(prices, reverse=True)
print('\n Новый список, с ценами по убыванию \n', new_list_prices)

print('\n Топ 5 цен списка \n', new_list_prices[0:5])
print('\n Топ 5 цен списка по возрастанию \n', sorted(prices[-5:]))