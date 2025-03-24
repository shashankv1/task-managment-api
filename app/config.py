import os

# Best practice: Use environment variables for sensitive information
SECRET_KEY = "YOUR_SECRET_KEY" # Fallback if env variable not set (for development only!)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database configuration (example using environment variables)
DATABASE_URL = "postgresql://postgres:shashank@localhost:5432/superset_db"