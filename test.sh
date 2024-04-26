#!/bin/bash

# set -x

username1="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1)"
password1="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1)"
username2="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1)"
password2="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 15 | head -n 1)"

### create users

curl -s -X POST -H "Content-Type: application/json" \
    -d "{\"username\":\"$username1\", \"password\":\"$password1\"}" \
    http://localhost:5000/api/users/register

response=$(curl -s -X POST -H "Content-Type: application/json" \
    -d "{\"username\":\"$username1\", \"password\":\"$password1\"}" \
    http://localhost:5000/api/users/auth)

USER1_TOKEN=$(echo $response | jq -r '.token')


curl -s -X POST -H "Content-Type: application/json" \
    -d "{\"username\":\"$username2\", \"password\":\"$password2\"}" \
    http://localhost:5000/api/users/register

response=$(curl -s -X POST -H "Content-Type: application/json" \
    -d "{\"username\":\"$username2\", \"password\":\"$password2\"}" \
    http://localhost:5000/api/users/auth)

USER2_TOKEN=$(echo $response | jq -r '.token')

# создать задачу
response=$(curl -X POST http://localhost:5000/tasks \
    -H "Content-Type: application/json" \
    -H "Authorization: $USER1_TOKEN" \
    -d '{"title": "Новая задача", "description": "Описание задачи", "deadline": "2022-12-31 23:59:59"}'
)

echo ""
echo "Create task"
TASK_ID=$(echo $response | jq -r '.id')
echo $TASK_ID

# изменить задачу
response=$(curl -X PUT http://localhost:5000/tasks/$TASK_ID \
    -H "Content-Type: application/json" \
    -H "Authorization: $USER1_TOKEN" \
    -d '{"title": "Измененная задача", "description": "Описание задачи", "deadline": "2023-01-01 00:00:00", "is_completed":false}'
)

echo ""
echo "Change task"

# удалить задачу другому юзеру
response=$(curl -X DELETE http://localhost:5000/tasks/$TASK_ID -H "Authorization: $USER2_TOKEN")
echo $response
echo ""
echo "Delete task"

# удалить задачу
curl -X DELETE http://localhost:5000/tasks/$TASK_ID -H "Authorization: $USER1_TOKEN"

echo ""
echo "Delete task"

# создать задачу
response=$(curl -X POST http://localhost:5000/tasks \
    -H "Content-Type: application/json" \
    -H "Authorization: $USER1_TOKEN" \
    -d '{"title": "Новая задача 2", "description": "Описание задачи", "deadline": "2022-12-31 23:59:59"}'
)

echo ""
echo "Create task"
TASK_ID=$(echo $response | jq -r '.id')
echo $TASK_ID

# просмотреть задачу
curl -X GET http://localhost:5000/tasks/$TASK_ID -H "Authorization: $USER1_TOKEN"
echo ""
echo "Get task"

# просмотреть задачи с пагинацией
curl -X GET "http://localhost:5000/tasks?page=2&page_size=3" -H "Authorization: $USER1_TOKEN"
echo ""
echo "Get tasks"

