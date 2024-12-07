# Base image for Java
FROM eclipse-temurin:17-jdk AS build

# Set working directory
WORKDIR /app

# Copy application files
COPY ./target/*.jar /app/pizza_shop_backend.jar

# Build the Java application
COPY database /app/database
COPY run.sh /app/run.sh


# Expose ports
EXPOSE 5432 9000

# Command to start PostgreSQL and the Java app
CMD ["java", "-jar","/app/pizza_shop_backend.jar"]
