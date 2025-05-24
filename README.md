# core_for_store
## Описание проекта
Создание ядра для интернет-магазина.<br/>
Это учебный проект студента курса [Python - разработчик](https://sky.pro/courses/programming/python-web-course#giftpopup)
на обучающей платформе [Skypro](https://sky.pro/).
## Структура проекта
* [main.py](main.py) - модуль с функцией main, которая формирует основную логику проекта и связывает<br/>
функциональности между собой
* src
  + [product.py](src/product.py) - модуль с классом Product для создания экземпляров товара
  + [lawn_grass.py](src/lawn_grass.py) - модуль с классом LawnGrass для создания экземпляров газонной травы
  + [smartphone.py](src/smartphone.py) - модуль с классом Smartphone для создания экземпляров смартфонов
  + [category.py](src/category.py) - модуль с классом Category для создания экземпляров категорий товара
  + [cat_iterator.py](src/cat_iterator.py) - модуль с классом-итератором CatIterator, позволяющим перебирать<br/>
список продуктов в экземпляре класса Category 
  + [base_product.py](src/base_product.py) - модуль с абстрактным классом-шаблоном BaseProduct для создания<br/>
необходимой структуры класса Product и его наследников
  + [print_mixin.py](src/print_mixin.py) - модуль с классом-примесью PrintMixin, добавляющим его наследникам<br/>
функционал вывода в консоль информации о своих экземплярах
* tests
  + test_product.py - модуль с тестами для модуля product.py
  + test_lawn_grass.py - модуль с тестами для модуля lawn_grass.py
  + test_smartphone.py - модуль с тестами для модуля smartphone.py
  + test_category.py - модуль с тестами для модуля category.py
  + test_cat_iterator.py - модуль с тестами для модуля cat_iterator.py
  + test_print_mixin.py - модуль с тестами для модуля print_mixin.py

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
