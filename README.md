# Quote of the Day API

This is a simple microservice that serves a random famous quote. It is built with Python/Flask and is designed to be deployed on Kubernetes as part of a DevOps demonstration.

---

## API Endpoints

- `GET /`: Returns a random quote in JSON format.
  - **Example Response:** `{"author": "Steve Jobs", "quote": "The only way to do great work is to love what you do."}`
- `GET /health`: Health check endpoint used by Kubernetes.
  - **Example Response:** `{"status": "ok"}`

---

## How to Run the Project

### Prerequisites

- Git
- Docker
- A Kubernetes cluster (e.g., Minikube, k3s, or a cloud provider)
- `kubectl` configured to connect to your cluster

### Steps

1.  **Clone the Repository**
    ```sh
    git clone <your-repository-url>
    cd quote-api
    ```

2.  **Push to Docker Hub**
    This project includes a GitHub Actions workflow (`.github/workflows/ci-cd.yml`) that automatically builds and pushes the Docker image to Docker Hub whenever you push to the `main` branch.

    **Manual Push (Optional):**
    ```sh
    # Replace 'your-dockerhub-username' with your actual username
    docker build -t your-dockerhub-username/quote-api:latest .
    docker push your-dockerhub-username/quote-api:latest
    ```

3.  **Deploy to Kubernetes**
    Before applying, make sure to update the `image` field in `deployment.yaml` to point to your Docker Hub repository.

    ```sh
    # Apply the deployment and service configurations
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

4.  **Verify the Deployment**
    ```sh
    # Check that the pods are running (should see 2 pods)
    kubectl get pods

    # Check that the service is created
    kubectl get service quote-api-service
    ```

5.  **Access the Service**
    If you are using Minikube, you can easily get the URL to access your service:
    ```sh
    minikube service quote-api-service
    ```
    This will open the service URL in your browser or print it to the console. You can then access the endpoint to get a quote.