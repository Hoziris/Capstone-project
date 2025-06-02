from fastapi import FastAPI, Request
from typing import Optional, Union
from pydantic import BaseModel, confloat, validator
from enum import Enum
import uvicorn
from processing import treatement
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
    "https://www.inondact.com",
    "https://inondact.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for user's answer

class DbEnum(str, Enum):
    centralized = "centralized"
    distributed = "distributed"

class SbEnum(str, Enum):
    stone = "stone"
    concrete = "concrete"
    brick = "brick"

class QcEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class SjEnum(str, Enum):
    adjoined = "adjoined"
    separated = "separated"

class SpEnum(str, Enum):
    wood = "wood"
    porcelain_stoneware = "porcelain_stoneware"
    natural = "natural"

class EbEnum(str, Enum):
    yes = "yes"
    no = "no"

class ShEnum(str, Enum):
    individual = "individual"
    collective = "collective"

class EeEnum(str, Enum):
    yes = "yes"
    no = "no"

class ErEnum(str, Enum):
    yes = "yes"
    no = "no"

class QmEnum(str, Enum):
    low = "low"
    high = "high"

class ApEnum(str, Enum):
    none = "None"
    basic = "Basic"
    medium = "Medium"
    advanced = "Advanced"
    pro = "Pro"

class FsEnum(str, Enum):
    flood_test = "FloodTest"
    runoff = "Runoff"
    quick_overflowing = "Quick Overflowing"
    slow_overflowing = "Slow Overflowing"
    rising_groundwater = "Rising Groundwater"

class User_answer(BaseModel):

    Ai: confloat(gt=0)  # m²
    Nf: confloat(gt=0)
    Eb: EbEnum # yes or no basement
    Sh: ShEnum #individual or collective housing
    Db: DbEnum  # centralized or distributed
    Yc: confloat(gt=0)
    Sj: SjEnum #adjoined or separated building

    Hf: Optional[confloat(gt=0)] = None
    Sb: Optional[SbEnum] = None  # stone, brick, concrete
    Qc: Optional[QcEnum] = None  # low, medium, high
    Ad: Optional[confloat(gt=0)] = None
    Hb: Optional[float] = None
    Hg: Optional[float] = None
    Sp: Optional[SpEnum] = None
    Yr: Optional[float] = None
    Tw: Optional[float] = None
    Ee: Optional[EeEnum] = None
    Er: Optional[ErEnum] = None
    Hcs: Optional[float] = None
    Qm: Optional[QmEnum] = None

    Adapt_Package : Optional[ApEnum] = None
    Flood_Scenario : Optional[FsEnum] = None

@app.post("/analyser")
def analysis(answers: User_answer):
    result = treatement(answers.dict())
    return {"result": result}


@validator("Ai")
def ai_must_be_positive(cls, v):
    if v <= 0:
        raise ValueError("Internal Area must be strictly positive")
    return v

@validator("Nf")
def nf_must_be_positive(cls, v):
    if v <= 0:
        raise ValueError("Number of floors must be strictly positive")
    return v

@validator("Hf")
def hf_must_be_positive(cls, v):
    if v <= 0:
        raise ValueError("Height of floor must be strictly positive")
    return v

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)