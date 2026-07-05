\set ON_ERROR_STOP on

SELECT 'CREATE ROLE agent_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE'
WHERE NOT EXISTS (
    SELECT 1
    FROM pg_roles
    WHERE rolname = 'agent_app'
)
\gexec

ALTER ROLE agent_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE;
\password agent_app

SELECT 'CREATE DATABASE agent_platform OWNER agent_app'
WHERE NOT EXISTS (
    SELECT 1
    FROM pg_database
    WHERE datname = 'agent_platform'
)
\gexec

SELECT 'CREATE DATABASE agent_platform_test OWNER agent_app'
WHERE NOT EXISTS (
    SELECT 1
    FROM pg_database
    WHERE datname = 'agent_platform_test'
)
\gexec

REVOKE ALL ON DATABASE agent_platform FROM PUBLIC;
REVOKE ALL ON DATABASE agent_platform_test FROM PUBLIC;
GRANT CONNECT, TEMPORARY ON DATABASE agent_platform TO agent_app;
GRANT CONNECT, TEMPORARY ON DATABASE agent_platform_test TO agent_app;

\echo PostgreSQL project databases are ready.
