from fastapi import FastAPI, APIRouter
from Models.modelreq import userReq
from Services.modelprediction import commentpredict

router = APIRouter()

@router.post("/predict")
def prediccomment(req:userReq):
    result = commentpredict(req.usercomment)
    return {"response":result}

