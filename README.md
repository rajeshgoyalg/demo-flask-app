# Demo Flask App

A sample Python Flask application designed for learning and demonstrating DevOps, CI/CD, and cloud-native deployment practices. This project is containerized with Docker and includes a GitHub Actions workflow for CI/CD automation. It is ideal for beginners and developers interested in modern software delivery pipelines.

---

## Features / API Endpoints

The application exposes the following endpoints:

| Endpoint            | Method | Description                                               |
|---------------------|--------|-----------------------------------------------------------|
| `/`                 | GET    | Returns a welcome message for ECS CI/CD test.             |
| `/flask`            | GET    | Returns a message for EKS deployment demonstration.       |
| `/health-check`     | GET    | Health check endpoint for service monitoring.             |
| `/argocd`           | GET    | Indicates ArgoCD sync status message.                     |

### Example `curl` Commands

```sh
curl http://localhost:3000/
curl http://localhost:3000/flask
curl http://localhost:3000/health-check
curl http://localhost:3000/argocd
```

---

## Installation Instructions

### Local Python Environment

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/demo-flask-app.git
   cd demo-flask-app
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip3 install -r requirements.txt
   ```
4. **Run the app:**
   ```sh
   python3 app.py
   ```
5. **Access the app:**
   - The app will be running at `http://localhost:3000`

### Using Docker

1. **Build the Docker image:**
   ```sh
   docker build -t demo-flask-app .
   ```
2. **Run the Docker container:**
   ```sh
   docker run -d -p 3000:3000 demo-flask-app
   ```
3. **Access the app:**
   - The app will be running at `http://localhost:3000`

---

## Building and Running the Docker Container

The app is containerized using a `Dockerfile` based on Python 3.11. Key steps:
- Copies all files into `/app` in the container
- Installs dependencies from `requirements.txt`
- Exposes port 3000
- Runs `python app.py`

### Example: Build & Run
```sh
docker build -t demo-flask-app .
docker run -d -p 3000:3000 demo-flask-app
```

---

## Environment Variables

- **None required by default.**
- You may add environment variables as needed for your use case.

---

## CI/CD

This project uses **GitHub Actions** for CI/CD automation:
- On every push to the `main` branch, the pipeline:
  - Builds the Docker image
  - Tags it with the commit SHA and date
  - Pushes the image to Docker Hub
  - Optionally updates a Helm chart repository for Kubernetes deployments

Workflow defined in `.github/workflows/ci.yml`.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## License

This project is licensed under the [MIT License](LICENSE).
 demo-flask-app
demo-flask-app
