summ = input("Введите сумму перевода")
summ = summ.replace(" ", "")
summ = summ.replace("*", "")
summ = summ.replace(",", "")
summ = summ.replace(".", "")
summ = summ.replace("/", "")
summ = summ.replace("-", "")
summ = int(summ)
summ = summ * 0.0095
print("Комиссия за перевод:", round(summ, 2), "руб.")
