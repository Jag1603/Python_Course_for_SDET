SELECT u.name, o.order_id
FROM users u
JOIN orders o ON o.user_id = u.id;