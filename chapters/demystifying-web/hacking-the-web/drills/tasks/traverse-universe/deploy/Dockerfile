# Build Stage 1: Builder
FROM php:7.2-apache AS builder

ARG FLAG="CTF{Placeholder_Fallback_Flag}"

WORKDIR /build

# Copy template from src
COPY src/index.php.template ./index.php.template

# Inject flag
RUN sed "s/__TEMPLATE__/${FLAG}/g" index.php.template > index.php


# Build Stage 2: Runtime 
FROM php:7.2-apache

# Copy entire src directory into Apache root
COPY src /var/www/html/

# Overwrite index.php with generated one
COPY --from=builder /build/index.php /var/www/html/index.php

# Healthcheck (uses your src/health.php)
HEALTHCHECK CMD curl -f http://localhost/health.php || exit 1

EXPOSE 80

