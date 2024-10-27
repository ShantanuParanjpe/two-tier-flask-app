# Start with the official MySQL image as a base
FROM mysql:8.0

# Set environment variables for MySQL configuration
ENV MYSQL_DATABASE=myDb \
    MYSQL_USER=admin \
    MYSQL_PASSWORD=admin \
    MYSQL_ROOT_PASSWORD=admin

# Expose the default MySQL port
EXPOSE 3306

# Run a command to check the MySQL service
HEALTHCHECK --interval=10s --retries=5 \
    CMD mysqladmin ping -h localhost || exit 1

