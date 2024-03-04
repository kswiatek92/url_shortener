import uuid
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from url_shortener.database import get_db

from . import models, tasks

router = APIRouter(
    prefix="/shorts",
)


class URLShortsRequest(BaseModel):
    original_url: str


@router.post("/short_url/")
async def shorten_url(url_short: URLShortsRequest, db: Session = Depends(get_db)):
    shortened_url = uuid.uuid4().hex
    db_url = models.URLShorts(
        original_url=url_short.original_url, shortened_url=shortened_url
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


@router.get("/get_all/")
async def get_all_urls(db: Session = Depends(get_db)):
    return db.query(models.URLShorts).all()


@router.get("/retrieve/{url_id}", response_class=RedirectResponse, status_code=302)
async def get_all_urls(url_id: str, db: Session = Depends(get_db)):
    redirect_url = (
        db.query(models.URLShorts)
        .filter(models.URLShorts.shortened_url == url_id)
        .first()
        .original_url
    )
    return RedirectResponse(redirect_url)
