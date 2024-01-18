FROM postgres:latest

# Copy the custom entrypoint script
#COPY entrypoint.sh /usr/local/bin/custom_entrypoint.sh
#RUN chmod +x /usr/local/bin/custom_entrypoint.sh

COPY init /docker-entrypoint-initdb.d

# Set the custom entrypoint script
#ENTRYPOINT ["custom_entrypoint.sh"]

# Default command, should be the same as in the official image
CMD ["postgres"]