FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app


# 4. Install dependencies first (Better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .
# 3. Switch to the non-root user
USER appuser
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]