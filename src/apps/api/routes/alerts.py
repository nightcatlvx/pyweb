from fastapi import APIRouter

router = APIRouter()

@router.post("/trigger")
async def trigger_alert(
):
    return {"status": "alert triggered"}
