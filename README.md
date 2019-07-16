# Взламываем электронный дневник
Скрипт исправляет успеваемость, удаляет замечания и вписывает похвалу.

### Как установить
Скачайте [код сайта](https://github.com/devmanorg/e-diary) электронного дневника.

Скрипт school_hack.py и файл с БД положите в корень проекта.

Создайте .env файл в корне проекта.
Укажите секретный ключ, он должен быть случайным и сложным для подбора,
т.к. используется для криптографической подписи.

В DATABASE_NAME укажите имя БД файла электронного дневника.

Дополнительно вы можете включить отладочный режим добавив переменную DEBUG с параметром True.

Пример файла .env:
```
SECRET_KEY=55*v5Aq)xz6A&q(b
DATABASE_NAME=schoolbase.sqlite3
DEBUG=True
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Возможности скрипта
В командной строке запустите интерактивную консоль:
```
python manage.py shell
```
Импортируйте класс **SchoolHack** и создайте экземпляр класса с аргументом ФИО ученика.

Для исправления плохих оценок на 5 используйте метод: **fix_marks()**.

Для удаления всех замечаний используйте метод: **remove_chastisements()**.

Для добавления похвалы от учителя используйте метод: **set_commendation()**.
В параметрах укажите название предмета и дату в формате "ДД.ММ.ГГГГ".
Похвала выбирается случайным образом из взятого списка с сайта [pedsovet.org](https://pedsovet.org/beta/article/30-sposobov-pohvalit-ucenika).

Пример использования скрипта:
```python
from school_hack import SchoolHack

student = SchoolHack('Рябова София Ильинична') # Создание экземпляр класса

student.fix_marks() # Исправления плохих оценок на 5

student.remove_chastisements() # Удаления всех замечаний

student.set_commendation('История', '15.07.2019') # Добавления похвалы
```

### Проверка изменений
Запустите сайт электронного дневника командой:
```
python manage.py runserver
```
Сайт будет доступен по адресу http://localhost:8000/.

Выберите класс и найдите ученика.

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
