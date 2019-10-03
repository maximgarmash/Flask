from flask import Flask

# Создаем объекта класса Flask, используя конструктор класса
app = Flask(__name__)  # __name__ - ссылка на файл, в котором этот конструктор вызывается (main.py)


# Декоратор route используется, чтобы связать URL адрес с функцией
@app.route('/')
# Этот код назначает функцию index() обработчиком корневого URL в приложении.
# Другими словами, каждый раз, когда приложение будет получать запрос, где путь — /,
# вызывается функция index(), и на этом запрос завершается.
def index():
    # print(i) # Для просомтра возможности debugger
    return 'Hello World'


# Для запуска сервера разработки нужно использовать метод run() объекта Flask.
if __name__ == "__main__":
    app.run(debug=True) # Параметр debug - включение отладчика

# Условие __name__ == "__main__" гарантирует, что метод run() будет вызван только в том случае,
# если main.py будет запущен как основная программа. Если попытаться использовать метод run()
# при импорте main.py в другой модуль Python, он не вызовется.
