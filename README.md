#FastAPI Backend Project with Rust and PostreSQL (Login or Sign up System)
#Structure
#fastapi-rust-backend/
#│
#├── fastapi_app/
#│   ├── main.py
#│   ├── database.py
#│   ├── models.py
#│   ├── schemas.py
#│   ├── auth.py
#│   ├── requirements.txt
#│   └── fastapi.Dockerfile
#│
#├── actix_service/
#│   ├── Cargo.toml
#│   ├── src/main.rs
#│   └── rust.Dockerfile
#│
#├── docker-compose.yml
#└── README.md

## Run Project

docker-compose up --build

FastAPI: http://localhost:8000/docs
Rust: http://localhost:8081/health

## Features

- User registration
- Login system
- Password hashing
- Rust microservice integration