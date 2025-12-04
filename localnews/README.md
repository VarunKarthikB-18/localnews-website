# LocalNews

A full-stack location-aware news application.

## Tech Stack
- **Backend**: Flask, SQLAlchemy, Flask-Migrate, Flask-JWT-Extended, Flask-Caching
- **Frontend**: Vue 3, Vite, Axios, Pinia, Vue Router
- **Database**: SQLite (dev)

## Prerequisites
- Python 3.8+
- Node.js 16+

## Setup & Running

### Backend

1. Navigate to backend directory:
   ```bash
   cd localnews/backend
   ```

2. Create virtual environment and activate:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize database:
   ```bash
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed data (optional):
   ```bash
   python seeds.py
   ```

6. Run server:
   ```bash
   flask run
   ```
   Server runs at `http://127.0.0.1:5000`

### Frontend

1. Navigate to frontend directory:
   ```bash
   cd localnews/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run dev server:
   ```bash
   npm run dev
   ```
   App runs at `http://localhost:5173`

## API Endpoints (Curl Examples)

### Register
```bash
curl -X POST http://127.0.0.1:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

### Get News (City)
```bash
curl "http://127.0.0.1:5000/news?city=New%20York"
```

### Get News (Coordinates)
```bash
curl "http://127.0.0.1:5000/news?lat=40.7128&lon=-74.0060"
```

## Environment Variables
See `backend/.env.example` for backend configuration.
Create a `.env` file in `backend/` with your keys (e.g. `NEWS_API_KEY`).
# localnews-website
