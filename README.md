# Team Data Web Application

## Overview

This project aims to create a simple web application that displays team data using Docker for containerization. It utilizes Flask with SQLAlchemy to connect to a MySQL database. The project is designed to be easily deployable with Docker Compose or runnable locally by installing the required packages.

## Project Structure

The project consists of the following components:

- **Web Application**: A Flask-based web application with routes to display team data.
- **Database**: MySQL database to store team member information.
- **Docker Configuration**: Dockerfile and docker-compose.yml to containerize and orchestrate the application.

## Requirements

To run this project, ensure you have Docker installed on your system. If you prefer to run it locally, you'll need Python and pip to install the required packages specified in `requirements.txt`.

## Usage

### Running with Docker Compose

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure Docker is installed and running on your system.
4. Open a terminal window and run the following command:
   ```bash
   docker-compose up
   ```
   This command will build and start the Docker containers defined in the `docker-compose.yml` file.
5. Once the containers are up and running, access the web application at `http://localhost:5000` in your browser.

### Running Locally

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your MySQL database. Ensure your database settings match the configuration in `config.py`.
5. Run the Flask application by executing:
   ```bash
   flask run
   ```
6. Access the web application at `http://localhost:5000` in your browser.

## Database Schema

The database schema includes fields for:

- Name
- ID
- Age
- CGPA

Ensure your MySQL database is configured accordingly to accommodate this schema.

## GitHub Repository

The project repository is hosted on GitHub. You can access it [here]([https://github.com/your-username/your-repository](https://github.com/mohamed682004/The-cloud.git)).

## Contributors

- **Team Leader**: [Khalil Elemam]

## Acknowledgements

Special thanks to [Eng/Sara Eldesouky] for providing the project guidelines and support throughout the development process.
