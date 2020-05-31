## Модуль 2. Фреймворк для распределенных вычислений Apache Spark

Описание:

По результатам модуля:

- делаем вычисления, преобразования, агрегации данных (ETL)

- формируем конечные витрины (для ML / BI)

- обучаем простенькую модель


### Занятие 5. Введение в Scala.

scala для дата инженеров.

Введение в Spark, RDD API


#### Цель занятия



*   Изучить основы языка Scala
*   Научиться собирать простейшее Scala-приложение


#### Краткое содержание



*   Синтаксис и простые выражения в Scala
*   Управляющие конструкции: if, for, pattern matching
*   ООП: Class, Object, Trait
*   Implicits
*   Инструменты для разработки: sbt, IntelliJ IDEA


#### Результат

Приложение на языке Scala


### Занятие 6. Apache Spark - 1 часть.

- Spark - что это и зачем он нужен

- API - RDD, Dataset, Dataframe, операции над распределенными коллекциями

- Процесс вычисления в Spark - task, stage, оптимизатор запросов

	


### Занятие 7. Apache Spark - 2 часть.

- Spark - что это и зачем он нужен

- API - RDD, Dataset, Dataframe, операции над распределенными коллекциями

- Процесс вычисления в Spark - task, stage, оптимизатор запросов


#### Домашнeе заданиe № 3. Введение в Spark + Гид по безопасному Бостону

[https://docs.google.com/document/d/1HPhwYCQ1AYklBeQ75RVsYV4MMGBEw_UBeTWp0c0Q678/edit?usp=sharing](https://docs.google.com/document/d/1HPhwYCQ1AYklBeQ75RVsYV4MMGBEw_UBeTWp0c0Q678/edit?usp=sharing)

[https://docs.google.com/document/d/1elWInbWsLrIDqB4FMMgFTUMNEmiYev9HJUfg9LXxydE/edit?usp=sharing](https://docs.google.com/document/d/1elWInbWsLrIDqB4FMMgFTUMNEmiYev9HJUfg9LXxydE/edit?usp=sharing)


### Занятие 8. Spark Streaming.

- Micro-batch обработка данных

- Классический Spark Streaming

- Structured Streaming

- Continuous processing


### Занятие 9. Доступ к данным, ноутбуки. Explore and visualize.

- Инструменты интерактивной аналитики

- Google Cloud Datalab

- Jupyter - интеграция с Apache Spark


### Занятие 10. Обучение моделей. ML.

Пример построения модели


#### Домашнeе заданиe № 4. Задание: обучаем собственную модель..

Внимание!

Из необходимого для успешной работы всей инфраструктурной обвязки:

- docker

- Makefile  (в противном случае команды можно запускать руками, копируя их из Makefile).

Для решения данного задания необходимо:

1. Сделать форк от master из репозитория https://github.com/OtusTeam/data-engineer

2. Перейти в папку spark_ml (командой в консоли: cd spark_ml)

3. Запустить докер-контейнер с jupyter notebook

4. Последовательно выполнить все ноутбуки в Readme.md (построить модель на Python + scikit-learn, построить модель на Apache Spark)

5. При построении модели на Apache Spark необходимо в качестве классификатора необходимо использовать вместо  LogisticRegression на RandomForest. 

Документация по API представлена здесь -  https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-classifier. Обратите внимание что необходимо использовать новое API (spark.ml). 

6. После построения модели и ее сохранения на диск, необходимо запустить стриминг из ноутбука (tweet_feeder). 

7. Далее необходимо применить модель в streaming mode. Заготовка для имплементации находится в ноутбуке (apply_model). В базовом подходе достаточно просто выводить результат применения модели. Обратите внимание что в качестве результата мы хотим видеть в отдельной колонке вероятность негативного твита (внутри поля probability представлен вектор из двух значений, нам нужна отдельная колонка с последним значением). Напишите udf который будет доставать эту колонку отдельно. 

8. Предоставьте корректно работающий форк на проверку. 

 Advanced:

- Попробуйте выводить статистику по количеству "негативных" и "позитивных" твитов за последние 10 секунд скользящим окном. 

_____________________________