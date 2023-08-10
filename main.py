from pyrogram import Client, errors
from time import sleep

api_id = 24851427
api_hash = 'b73fb7bae6362ba5d37825d8334ec903'
app = Client("open", api_id=api_id, api_hash=api_hash)
print("Введите номер телефона, затем английскую 'y', и код который придет из телеги. Если не напишет 'Готово', то нужно ввести пароль от тг")
try:
    app.start()
except:
    print("Неудалось запустить скрипт")
    exit(1)
print("Готово!")
casse = input("Введите номер кейса: ")
count = int(input("Введите кол-во кейсов: "))
print(f"Начинаю открытие {count} {casse} кейсов...")
for i in range(count):
    try:
        app.send_message(chat_id="bforgame_bot", text=f"Открыть кейс {casse}")
    except errors.FloodWait as e:
        print(f"Задержка в {e.value} секунд...")
        sleep(e.value)
print("Завершено!")
