SELECT COUNT(*) AS new_users_today
FROM users
WHERE created_at::date = CURRENT_DATE;
