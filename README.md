# yamdb_final
![yamdb workflow status](https://github.com/Sovushka-sever/yamdb_final/workflows/YamdbWorkflow/badge.svg)

API для блога с авторизацией пользователей, комментариями и подписками

## Начало
Эти инструкции позволят вам запустить копию проекта на локальном компьютере в целях разработки и тестирования. 
См. В разделе «Установка» примечания о том, как развернуть проект в действующей системе.
### Предварительные требования
Должны быть установлены Docker и Docker-Compose

Инструкция по установке: 
- [Docker](https://docs.docker.com/get-docker/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

### Установка
Для начала вам нужно склонировать репозиторий и находится в директории yamdb_final:
- Собрать образ
```
docker-compose build
```
- Запустить docker-compose
```
docker-compose up
```
- Для остановки docker-compose
```
docker-compose down

```
## Дополнительные команды
для выполнения этих команд вы должны находится в yamdb_final 
и у вас должен быть запущен docker-compose
- Для выполнения миграций:
```
docker-compose run web python manage.py migrate
```
- Для заполнения базы начальными данными:
```
docker-compose run web python manage.py loaddata fixtures.json
```
- Для создания суперюзера:
```
docker-compose run web python manage.py createsuperuser
```
## Авторы
* **Sovushka-sever** 
* **Sommary**
* **AVStorchak**
## Лицензия
Этот проект находится под лицензией Apache License 2.0. Подробности в файле  [LICENSE](https://github.com/Sovushka-sever/infra_sp2/blob/master/LICENSE)
