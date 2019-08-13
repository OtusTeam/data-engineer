# 1. Разверните и подготовьте окружение

Вам потребуется компьютер или виртуальная машина минимум с двумя ядрами и 8 гигабайтами памяти (оптимально - 4 ядра, 16 гигабайт памяти и 100 гигабайт на диске для данных). Вы можете использовать Mac или Linux.
Вам потребуются такие пакеты:
- docker, docker-compose
- git
- jq
- OpenJDK8 (от него нужен keytool)
- curl

Если вы используете виртуальную машину с Linux рекомендую поднять значение vm.max_map_count (sudo sysctl -w vm.max_map_count=262144 для изменения на живой машине, и/или добавить строчку vm.max_map_count=262144 в /etc/sysctl.conf).
Если вы используете Mac - поднимите объем оперативной памяти для Docker Desktop до 8 гигабайт.

Скопируйте себе репозиторий с окружением:
`git clone https://github.com/confluentinc/cp-demo && cd cp-demo`

В эту же директорию скопируйте скрипты set_elasticsearch_mapping_lang.sh и submit_elastic_sink_lang_config.sh которые приложены к заданию (не забудьте сделать их исполняемыми командой `chmod u+x`).

Запустите скрипт `./scripts/start.sh` (вы можете остановить окружение и удалить все собранные данные если запустите `./scripts/stop.sh`)

В зависимости от мощности вашей машины и ширины канала в интернет скрипт может занимать от нескольких минут до получаса (повторые запуски будут проходить быстрее, так как все образы уже будут скачаны).

Если все прошло успешно, то скрипт поприветствует вас сообщением:
```
******************************************************************
DONE! Connect to Confluent Control Center at http://localhost:9021
******************************************************************
```

Если у вас появились проблемы - обратитесь к преподавателю, либо воспользуйтесь подсказками [на сайте Confluent](https://docs.confluent.io/current/tutorials/cp-demo/docs/index.html#troubleshooting-the-demo).

Для работы, помимо текстового редактора, вам понадобятся 4 окна:
1. Браузер (лучше Chrome) с Confluent Control Center http://localhost:9021 (если вы запускаетесь где-то на виртуалке - используйте ее адрес)
2. Браузер c Kibana UI http://localhost:5601
3. Терминал с открытым KSQL CLI, для этого в директории ./cp-demo выполните команду `docker-compose exec ksql-cli ksql http://ksql-server:8088`
4. Терминал с shell в директории ./cp-demo для запуска скриптов и отладки



# 2. Создайте KSQL Stream WIKILANG

Посмотрите какие топики есть сейчас в системе, и на основе того, в котором вы видите максимальный объем данных создайте stream по имени WIKILANG который фильтрует правки только в разделах национальных языков, кроме английского (поле channel вида #ru.wikipedia), который сделали не боты.

Stream должен содержать следующие поля: createdat, channel, username, wikipage, diffurl

# 3. Мониторинг WIKILANG

После 1-2 минут работы откройте Confluent Control Center и сравните пропускную способность топиков WIKILANG и WIKIPEDIANOBOT, какие числа вы видите?

- В KSQL CLI получите текущую статистику вашего стрима: describe extended wikilang;  

Приложите полный ответ на предыдущий запрос к ответу на задание.

- В KSQL CLI получите текущую статистику WIKIPEDIANOBOT: descrbie extended wikipedianobot;  

Приложите раздел Local runtime statistics к ответу на задание.  
Почему для wikipedianobot интерфейс показывает также consumer-* метрики?

# 4. Добавьте данные из стрима WIKILANG в ElasticSearch
- Добавьте mapping - запустите скрипт set_elasticsearch_mapping_lang.sh
- Добавьте Kafka Connect - запустите submit_elastic_sink_lang_config.sh
- Добавьте index-pattern - Kibana UI -> Management -> Index patterns -> Create Index Pattern -> Index name or pattern: wikilang -> кнопка Create

Используя полученные знания и документацию ответьте на вопросы:  
a) Опишите что делает каждая из этих операций?  
б) Зачем Elasticsearch нужен mapping чтобы принять данные?  
в) Что дает index-pattern?

# 5. Создайте отчет "Топ10 национальных разделов" на базе индекса wikilang
- Kibana UI -> Visualize -> + -> Data Table -> выберите индекс wikilang
- Select bucket type -> Split Rows, Aggregation -> Terms, Field -> CHANNEL.keyword, Size -> 10, нажмите кнопку Apply changes (выглядит как кнопка Play)
- Сохраните визуализацию под удобным для вас именем

Что вы увидели в отчете?

- Нажав маленьку круглую кнопку со стрелкой вверх под отчетом, вы сможете запросить не только таблицу, но и запрос на Query DSL которым он получен.

Приложите тело запроса к заданию.