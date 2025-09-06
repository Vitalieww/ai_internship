# Docker Flask and Ollama Setup

This project sets up a multi-container Docker application with a Flask web application and an Ollama service. Below are the instructions on how to build and run the containers.

## Project Structure

```
docker-flask-ollama
├── flask-app
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── ollama
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Docker installed on your machine
- Docker Compose installed

## Building the Containers

To build the containers, navigate to the project directory and run:

```bash
docker-compose build
```

## Running the Containers

To start the containers, use the following command:

```bash
docker-compose up
```

This will start both the Flask application and the Ollama service. The Flask app will be accessible at `http://localhost:5000`.

## Stopping the Containers

To stop the containers, you can use:

```bash
docker-compose down
```

## Additional Information

- The Flask application is defined in the `flask-app` directory.
- The Ollama service is defined in the `ollama` directory.
- Make sure to check the individual Dockerfiles and the `docker-compose.yml` for any specific configurations or environment variables that may be required.

Feel free to modify the application as needed!