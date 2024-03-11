# SOA
HSE SOA course

Анохов Владислав Дмитриевич, 2110, Трекер задач 

docker-compose build 
docker-compose up


удалить том: 

docker volume rm soa_postgres_data

тест ручек:

curl -X POST -H "Content-Type: application/json" -d '{"username":"myusername", "password":"mypassword"}' http://localhost:5000/api/users/register

curl -X POST -H "Content-Type: application/json"      -d '{"username":"myusername", "password":"mypassword"}'      http://localhost:5000/api/users/auth

curl -X PUT      -H "Content-Type: application/json"      -H "Authorization: <token>"      -d '{"name":"New Name", "email":"newemail@example.com"}'      http://localhost:5000/api/users/me