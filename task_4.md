## Структура БД

1. Переопределяем Юзера, в будущем в местах где нужно достать его инстанс используем get_user_model(), если мы говорим про django(1 час)
2. Создаем таблицу Ролей с n нужных вариантов названий для ролей, и кидаем FK на юзера (0.2 часа)

## Запросы
1. Выбрать все роли (названия ролей) с количеством пользователей для каждой роли: 
SELECT r.role, COUNT(u.id) AS user_count
FROM roles AS r
LEFT JOIN user AS u ON r.user_id = u.id
GROUP BY r.role;

2. Выбрать всех пользователей (логины пользователей), которые имеют от 3 до 5 ролей, перечислив их роли через запятую в отдельном поле:
SELECT u.username, GROUP_CONCAT(r.role) AS roles
FROM user AS u
INNER JOIN role AS r ON u.id = r.user_id
GROUP BY u.username
HAVING COUNT(r.id) BETWEEN 3 AND 5;
