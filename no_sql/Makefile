start:
	docker-compose up -d

remove:
	docker-compose rm -s -f

reset: remove start

test:
	docker-compose exec client python /root/test.py

console:
	docker-compose exec client bash
