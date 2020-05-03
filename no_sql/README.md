# Задание по NoSQL СУБД

- Мы разрабатываем сервис который показывает другим сервисам внутри нашей компании Lifetime Value клиента (по его идентификатору). Мы решили использовать Aerospike в самой простой редакции.
- Сейчас у нас простая in-memory реализация: [test.py](scripts/test.py)

1. Запустите aerospike локально в докере: `docker-compose up -d`
2. Проверьте что Aerospike работает: `docker-compose exec client python /root/test.py`
3. Используя документацию https://www.aerospike.com/docs/client/python/index.html реализуйте три функции (add_customer, get_ltv_by_id, get_ltv_by_phone) в файле scripts/solution.py
4. Решение должно содержать пример использовать и исполняться командой `docker-compose exec client python /root/solution.py`; для соединения с базой данных используйте имя хоста `db` и порт `3000` (как сделано в примере test.py)

