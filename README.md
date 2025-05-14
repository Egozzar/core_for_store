# core_for_store
## Описание проекта
Создание ядра для интернет-магазина.<br/>
Это учебный проект студента курса [Python - разработчик](https://sky.pro/courses/programming/python-web-course#giftpopup)
на обучающей платформе [Skypro](https://sky.pro/).
## Структура проекта
* [main.py](main.py) - модуль с функцией main, которая формирует основную логику проекта и связывает<br/>
функциональности между собой
* src
  + [product.py](src/product.py) - модуль с классом Product для создания экземпляров товара<br/>
  + [category.py](src/category.py) - модуль с классом Category для создания экземпляров категорий товара<br/>
  + [cat_iterator.py](src/cat_iterator.py) - модуль с классом-итератором CatIterator, позволяющим перебирать<br/>
список продуктов в экземпляре класса Category 
* tests
  + test_product.py - модуль с тестами для модуля product.py
  + test_category.py - модуль с тестами для модуля category.py
  + test_cat_iterator.py - модуль с тестами для модуля cat_iterator.py

## Установка
```commandline
poetry install
```
## Тестирование
Для разработчика:
```commandline
pytest
```
## Пример использования
Для того, чтобы запустить проект, необходимо сначала установить зависимости.<br/>
Затем нужно запустить файл `main.py`:
```commandline
python main.py
```
## Команда проекта
* Клименко Леонид - студент
