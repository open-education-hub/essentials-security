# Stage 1: Builder
FROM alpine AS builder
WORKDIR /app
# COPY commands look for files relative to the build context
COPY src/index.php .
COPY flag .
RUN sed -i "s/__TEMPLATE__/$(cat flag)/g" index.php

# Stage 2: Final Image
FROM php:8.0-apache
COPY --from=builder /app/index.php /var/www/html/
EXPOSE 80
