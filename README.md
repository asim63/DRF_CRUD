# DRF_CRUD

Render-ready full-stack setup for:

- Django REST API (`/api/grocery/`)
- React + Vite frontend (`frontend/grocery-bud`)

## Deploy on Render

1. In Render, create a **Blueprint** and point it to this repo.
2. Render will read `render.yaml` and create:
   - `drf-crud-api` (Python web service)
   - `grocery-bud-frontend` (static site)
   - `drf-crud-db` (PostgreSQL)
3. After services are created, set these environment variables:
   - On `grocery-bud-frontend`: `VITE_API_BASE_URL=https://<your-api-service>.onrender.com`
   - On `drf-crud-api`:
     - `CORS_ALLOWED_ORIGINS=https://<your-frontend-service>.onrender.com`
     - `CSRF_TRUSTED_ORIGINS=https://<your-frontend-service>.onrender.com`
4. Trigger a redeploy for both services.

## Local development

Backend:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Frontend:

```bash
cd frontend/grocery-bud
npm install
npm run dev
```

Optional frontend env file:

```bash
# frontend/grocery-bud/.env
VITE_API_BASE_URL=http://127.0.0.1:8000
```
