# 2212266 — DevOps Final Project

**Student: Sadam Hussain** 
**Reg No: 2212266** 


## Architecture

FastAPI app + PostgreSQL database running in Docker containers, automatically deployed to AWS EC2 via GitHub Actions CD pipeline.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check with reg number |
| POST | /students | Create student record |
| GET | /students | List all students |
| GET | /students/{reg_no} | Get student by reg no |

## Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/sadamtheCoder786/2212266-devops-project.git
cd 2212266-devops-project

# 2. Create .env file
cp .env.example .env

# 3. Run with Docker Compose
docker compose up --build

# 4. Access the app
# http://localhost:8000/health
```

### Production (EC2)

Automatically deployed via GitHub Actions CD pipeline when code is pushed to the `main` branch.

<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/09f8a848-1f64-4f19-95e0-cf93f9ae0caf" />
<img width="960" height="1140" alt="image" src="https://github.com/user-attachments/assets/56c839a8-ed5e-4aeb-afe0-a541d1ab8ea7" />
