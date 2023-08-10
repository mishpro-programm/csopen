from pyrogram import Client, errors
from time import sleep

api_id = 24851427
api_hash = 'b73fb7bae6362ba5d37825d8334ec903'
app = Client("open", api_id=api_id, api_hash=api_hash)
print("\e[0;33mВведите номер телефона, затем английскую 'y', и код который придет из телеги. Если не напишет 'Готово', то нужно ввести пароль от тг")
try:
    app.start()
except:
    print("\e[0;31mНеудалось запустить скрипт\e[0;0m")
    exit(1)
print("\e[0;33mГотово!")
casse = input("Введите номер кейса: ")
count = int(input("Введите кол-во кейсов: "))
print(f"Начинаю открытие {count} {casse} кейсов...")
for i in range(count):
    print(i+1, "кейс")
    try:
        app.send_message(chat_id="bforgame_bot", text=f"Открыть кейс {casse}")
    except errors.FloodWait as e:
        print(f"Задержка в {e.value} секунд...")
        sleep(e.value)
print("Завершено!\e[0;0m")
