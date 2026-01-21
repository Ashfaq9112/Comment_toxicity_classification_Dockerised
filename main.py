from fastapi import FastAPI
from Routes.commentpredict import router
app = FastAPI()

app.include_router(router)