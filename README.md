#fibo-rest-test
# Fibonacci REST API

This project is a REST API for calculating Fibonacci numbers, implemented using Flask and containerized using Docker.

## Installation and launch

### Requirements

- Docker
- Docker Compose (optional)

### Containerization

1. **Building a Docker image**:

 In the project root, run the following command:

 ```bash
 docker build -t my-flask-app .

2. **Running a Docker container**:

 After building the image, run the container:
 docker run -d -p 5000:5000 my-flask-app
 The application will be available at http://localhost:5000/.


### Launch and test API

 Functionality check:

 Open your browser and go to http://localhost:5000/. You should see a "Hello, World!" message.

 API testing:

 To get the nth Fibonacci number, send a GET request with the n parameter. For example:

 For n=2:

GET http://localhost:5000/calc?n=2
Expected answer: 55 (since F(10) = 55).

3. **Using cURL**:
You can also use cURL to test the API from the command line. Example command:

curl "http://localhost:5000/calc?n=2"
This should return 1.

**CI/CD**

Using GitHub Actions, you can set up automatic build and deployment of your application:

 Workflow: For every change in the main branch, a workflow is triggered, which:
 Checks code from the repository.
 Installs dependencies.
 Builds a Docker image.
 Conducts tests (if available).
 Authenticates to Docker Hub using an access token.
 Publishes the image to Docker Hub.

**Monitoring and registration**

The following strategies can be used for monitoring and logging:

 Logs: Application logs can be written to standard output, which Docker will save.
 Monitoring: Prometheus and Grafana can be used to monitor container health and performance. They can be deployed as separate containers and integrated with your application to collect metrics.
 Health Checks: Set up health checks in Docker to ensure your container is running correctly.

**Scaling**

To scale your application to handle a large number of requests, you can:

 Run multiple container instances: Use Docker Compose or Kubernetes to run multiple instances of your application, allowing you to handle more incoming requests simultaneously.

 Example using Docker Compose:
version: '3'
services:
 web:
 image: my-flask-app
 ports:
 - "5000:5000"
 deploy:
 replicas: 3

 Load Balancing: Use a reverse proxy such as Nginx or Traefik to distribute the load across your application instances.

 Caching: Implement application-level caching or use Redis to temporarily store Fibonacci calculation results to reduce the load.

 This project demonstrates a simple Flask application that can be easily deployed and scaled using modern containerization and CI/CD techniques. For more information, see the Flask, Docker, and GitHub Actions documentation.