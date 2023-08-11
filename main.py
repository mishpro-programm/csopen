from pyrogram import Client, errors
from time import sleep

api_id = 24851427
api_hash = 'b73fb7bae6362ba5d37825d8334ec903'
app = Client("open", api_id=api_id, api_hash=api_hash, app_version="CaseOpen 1.0", device_model="@mishpro Scripts", lang_code="ru")
print("\033[33mВведите номер телефона, затем английскую 'y', и код который придет из телеги. Если не напишет 'Готово', то нужно ввести пароль от тг\033[0m")
try:
    app.start()
except:
    print("\033[31mНеудалось запустить скрипт\033[0m")
    exit(1)
print("\033[33mГотово!")
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
print("Завершено!\033[0m")
