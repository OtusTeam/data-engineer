# Задание по NoSQL СУБД

- Мы разрабатываем сервис который показывает другим сервисам внутри нашей компании Lifetime Value клиента (по его идентификатору). Мы решили использовать Aerospike в самой простой редакции.
- Сейчас у нас простая in-memory реализация: [test.py](test.py)

1. Запустите aerospike локально в докере: `docker-compose up -d` Чтобы проверить что он работает зайдите в AQL: `docker exec -it aerospike aql`
2. Поставьте в свое окружение клиент aerospike для python, например: pip3 install -r requirements.txt
3. Используя документацию https://www.aerospike.com/docs/client/python/index.html реализуйте три функции (add_customer, get_ltv_by_id, get_ltv_by_phone)

Решение должно быть в виде одного файла скрипта, использовать 127.0.0.1:3000 в качестве соединения с Aerospike