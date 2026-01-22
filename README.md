# 🚀 Comment Toxicity Classifier API

[![Docker Hub]
https://hub.docker.com/r/ashfaqgg3/commenttoxicityfastapi


## 📝 Project Overview
This project takes a "Legacy" Deep Learning model (trained on the Jigsaw Toxicity Dataset) and transforms it into a modern, production-ready microservice. I wrapped the original `.h5` model with **FastAPI** and fully **Dockerized** the environment to ensure portability and ease of use.

### Key Features:
- **FastAPI Wrapper:** High-performance asynchronous API for real-time toxicity scoring.
- **Legacy Compatibility:** Solved versioning conflicts between Keras 2 and Keras 3 to support older `.h5` model formats.
- **Dockerized Deployment:** Fully containerized with a non-root user for enhanced security.
- **Automated Preprocessing:** Integrates `TextVectorization` and custom vocab loading within the API lifecycle.

---

## 🛠️ Technical Challenges & Solutions

### 1. The Keras 2 vs. Keras 3 Conflict
The original model was trained in a Keras 2 environment. Modern TensorFlow (2.16+) defaults to Keras 3, which causes `unrecognized keyword` errors when loading older LSTM layers.
* **Solution:** I pinned the environment to **TensorFlow-CPU 2.15.0** and **Keras 2.15.0**, ensuring the model architecture loads correctly without losing weights or functionality.

### 2. Windows-Specific Dependency Hurdles
During Dockerization, I encountered issues with `tensorflow-io-gcs-filesystem` lacking Windows wheels.
* **Solution:** Switched to a `python:3.11-slim` Debian-based Docker image and optimized the `pip` installation to bypass unnecessary GCS dependencies, reducing image size and improving stability.

### 3. Production Security
* **Solution:** Implemented a **non-root user** (`appuser`) in the Dockerfile. Even if the application is compromised, the attacker has limited access to the container system.

---

## 🚀 Quick Start (Docker)

You don't need Python or TensorFlow installed to try this. Just run the following command:

docker run -p 8000:8000 ashfaqgg3/commenttoxicityfastapi
