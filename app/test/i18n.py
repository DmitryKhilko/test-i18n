import os


def search_i18n():
    """
    1.  Отбираем в проекте все файлы.
    2.  В отобранных файлах находим html-файл.
    3.  В html-файле находим строки, начинающиеся с '<p', '<button', '<h2',
        '<h'.
    4.  Если найденная строка содержит значение 'i18n', разработчик добавил
        метку i18n.
    5.  Если найденная строка не содержит значение 'i18n', разработчик не
        добавил
        метку i18n. В этом случае выводим сообщение об ошибке, содержащее:
        Имя файла + номер строки, где выявлена ошибка + саму строку
    """
    os.getcwd()  # выясняем текущую директорию (откуда запускается функция)
    os.chdir('..')  # переходим в директорию на уровень выше '.\app'

    for root, dirs, files in os.walk("."):  # отбор всех файлов проекта
        for file in files:  # перебор всех отобранных файлов проекта
            if file.endswith(".html"):  # если файл оканчивается на html

                # Прохождение в файле по строкам и анализ тегов
                # encoding='utf-8' для вывода строк файла на русском языке
                with open(os.path.join(os.getcwd(), root.lstrip(".\\"), file),
                          'r', encoding='utf-8') as f:
                    line_of_file = 0
                    error_exist = False
                    for line in f:
                        line_of_file += 1

                        if '<p' in line:
                            if 'i18n' not in line:
                                # \033[31m - текст красного цвета
                                print('\033[31m Ошибка. Отсутствует метка i18n'
                                      ' в html-теге <p>: имя файла: {}; номер '
                                      'строки: {}; строка: {}'.format(f.name,
                                                                      line_of_file,
                                                                      line))
                                error_exist = True

                        if '<button' in line:
                            if 'i18n' not in line:
                                print('\033[31m Ошибка. Отсутствует метка i18n'
                                      ' в html-теге <button>: имя файла: {}; '
                                      'номер строки: {}; строка: {}'.format(f.name,
                                                                            line_of_file,
                                                                            line))
                                error_exist = True

                        if '<h ' in line or '<h>' in line:
                            if 'i18n' not in line:
                                print("\033[31m Ошибка. Отсутствует метка i18n"
                                      " в html-теге <h>: имя файла: {}; номер "
                                      "строки: {}; строка: {}".format(f.name,
                                                                      line_of_file,
                                                                      line))
                                error_exist = True

                        if '<h2' in line:
                            if 'i18n' not in line:
                                print("\033[31m Ошибка. Отсутствует метка i18n"
                                      " в html-теге <h2>: имя файла: {}; номер"
                                      " строки: {}; строка: {}".format(f.name,
                                                                       line_of_file,
                                                                       line))
                                error_exist = True

    if not error_exist:
        print('\033[32m{}'.format('Разработчики молодцы, метку i18n вставили '
                                  'во все html-теги: p, button, h, h2'))


search_i18n()
