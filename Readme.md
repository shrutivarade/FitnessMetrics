
# Fitness Metrics Dashboard

The Fitness Metrics Dashboard is a web application built with Django, Chart.js, and PostgreSQL, allowing users to visualize and track their fitness metrics. The dashboard consists of four graphs displaying calories burnt, distance covered, step count, and heart rate data.

![Fitness Metrics Dashboard](<https://github.com/shrutivarade/FitnessMetrics/blob/main/gfx/Fitness%20Dashboard.png>)

## Features

- Visualize fitness metrics data in real-time with interactive graphs.
- Store and manage fitness metrics data in a PostgreSQL database.
- Easy deployment and management with Docker using docker-compose.

## Prerequisites

Before running the application, ensure you have the following installed on your system:

- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Installation and Setup

1. Clone the repository to your local machine:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd fitness_metrics_dashboard
```

3. Create a `.env` file in the root directory and specify the required environment variables:

```
# .env file
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```

Replace `your_secret_key`, `your_db_name`, `your_db_user`, `your_db_password` with your desired values. The `DB_HOST` should be set to `db`, which is the service name defined in the `docker-compose.yml`.

4. Build and start the Docker containers:

```bash
docker-compose build
docker-compose up
```

5. Wait for the containers to start. Once the process is complete, the application should be accessible at `http://localhost:8000` in your web browser.

## Usage

1. Open your web browser and navigate to `http://localhost:8000` to access the Fitness Metrics Dashboard.

2. The dashboard displays four interactive graphs representing calories burnt, distance covered, step count, and heart rate data.

3. Interact with the graphs to explore the fitness metrics data over time.

## Data Collection

To populate the dashboard with fitness metrics data, use the Django admin interface. Follow these steps:

1. Access the Django admin interface at `http://localhost:8000/admin`.

2. Log in using the superuser credentials created during setup.

3. Add, edit, or delete fitness metrics data through the provided admin interface.

## Contributing

Contributions to the Fitness Metrics Dashboard project are welcome! If you wish to contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name for your feature or bug fix.

3. Make the necessary changes in your branch.

4. Commit and push your changes to your forked repository.

5. Submit a pull request explaining your changes.

Feel free to customize the README file to suit your project structure and specific requirements. The provided instructions should help users understand how to set up and use the fitness metrics dashboard deployed with Docker and Docker Compose.
