# Use the base image you want
FROM kukatlavenkat/django:v1

# Set the working directory
WORKDIR /app

# Copy the start.sh script into the container
COPY ./startup.sh /app/

# Give execute permissions to the script
RUN chmod 700 /app/startup.sh

# Expose the necessary port
EXPOSE 8000

# Start the application using the script as the default command
CMD ["/bin/bash", "-c", "/app/startup.sh"]
