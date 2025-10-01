-- https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_VIEW.html

CREATE OR REPLACE VIEW active_users AS
SELECT user_id, username
FROM users
WHERE created_at > GETDATE() - INTERVAL '30 days';
