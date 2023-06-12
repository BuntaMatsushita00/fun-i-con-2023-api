from fastapi import APIRouter, HTTPException, Depends
import api.schemas.calc as calc_schema

import api.calc.logic as logic

router = APIRouter()

@router.post("/calc")
async def calc(item: calc_schema.Answers):
    result = logic.main(item)
    return result

