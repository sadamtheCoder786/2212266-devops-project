# 2212266 — DevOps Final Project

  Student: Sadam Hussain
  Reg No: 2212266


## Architecture

FastAPI app + PostgreSQL database running in Docker containers,
automatically deployed to AWS EC2 via GitHub Actions CD pipeline.

GitHub Push -> CI (lint+test) -> CD (SSH to EC2) -> docker compose up

## Local Setup

cp .env.example .env
docker compose up --build

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check with reg number |
| POST | /students | Create student record |
| GET | /students | List all students |
| GET | /students/{reg_no} | Get student by reg no |
