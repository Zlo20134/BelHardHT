rubles = int(input('Введите рубли: '))
cent = int(input('Введите копейки: '))

if cent >= 100:
    add_rubles = cent // 100
    rubles += add_rubles
    cent %= 100
if 11 <= rubles % 100 <= 14:
    rubles_text = f'{rubles} рублей'
elif rubles % 10 == 1:
    rubles_text = f'{rubles} рубль'
elif rubles % 10 in (2, 3, 4):
    rubles_text = f'{rubles} рубля'
elif 5 <= rubles % 100 <= 20:
    rubles_text = f'{rubles} рублей'
else:
    rubles_text = f'{rubles} рублей'

if cent % 10 == 1:
    cent_text = f'{cent} копейка'
elif cent % 10 in (2, 3, 4):
    cent_text = f'{cent} копейки'
elif 5 <= cent % 100 <= 20:
    cent_text = f'{cent} копеек'
else:
    cent_text = f'{cent} копеек'

print(rubles_text, cent_text)