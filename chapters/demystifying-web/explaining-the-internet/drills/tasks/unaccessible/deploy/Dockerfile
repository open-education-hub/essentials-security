# Stage 1: Generate the source file with the flag
FROM alpine:latest AS builder

ARG FLAG
# Copy the template flag file from the host
COPY src/flag.txt /tmp/flag.txt

# Substitute the placeholder with the actual flag
RUN sed -i "s/__TEMPLATE__/${FLAG}/g" /tmp/flag.txt

# Stage 2: Final SSH image
FROM alpine:latest

# Install OpenSSH server and generate host keys
RUN apk add --no-cache openssh \
    && ssh-keygen -A

# Create the user 'ctf' and set the weak password to 'stupid'
RUN adduser -D -s /bin/sh ctf \
    && echo "ctf:stupid" | chpasswd

# Copy the generated flag file from the builder stage
COPY --from=builder /tmp/flag.txt /home/ctf/flag

# Set strict permissions so only the 'ctf' user can read the flag
RUN chown ctf:ctf /home/ctf/flag && chmod 400 /home/ctf/flag

# Expose the standard SSH port
EXPOSE 22

# Start the SSH daemon in the foreground
CMD ["/usr/sbin/sshd", "-D"]
