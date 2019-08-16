save:
	git add .
	git commit -a -m "Save"
	git push

migrate:
	docker-compose run api python manage.py migrate

start:
	make migrate
	docker-compose up

stop:
	docker-compose stop

makemigrations:
	docker-compose run api python manage.py makemigrations

clean:
	make stop
	rm -f api/db.sqlite3
	make start
