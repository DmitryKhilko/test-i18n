# Тестирование добавления метки i18n к html-тегам 

Установка проекта на локальный компьютер:
1. git clone https://github.com/DmitryKhilko/test-i18n.git - клонирование проекта
2. pip3 install -r requirements.txt - установка пакетов

Описание функционала тестовой функции search_i18n, расположенной в файле /test/i18n.py:

1. Производится отбор всех файлов проекта.
2. В отобранных файлах производится поиск html-файлов. Для каждого html-файла:
   1. Производится поиск строк, начинающихся с '<p', '<button', '<h2',
        '<h'.
   2. Если найденная строка содержит значение 'i18n', разработчик добавил метку i18n.
   3. Если найденная строка не содержит значение 'i18n', разработчик не добавил
        метку i18n. В этом случае в консоль выводится сообщение об ошибке, содержащее:
        имя файла + номер строки, где выявлена ошибка + саму строку

Запуск тестовой функции:
1. Выбрать файл /test/i18n.py
2. Произвести запуск функции (Shift + F10). 
