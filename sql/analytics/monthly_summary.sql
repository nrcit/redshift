SELECT DATE_TRUNC('month', created_at) AS month, COUNT(*) AS new_users
FROM users
GROUP BY 1
ORDER BY 1;
