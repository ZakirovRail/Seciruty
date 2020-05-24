import logic
import queries
import generators

logic.iteration_by_logins_then_by_limited_passwords(
    generators.generate_simple_login,
    generators.generate_popular_password,
    queries.request_local_server
)
