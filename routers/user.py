from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from routers.login import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.get("/{id}", status_code=200)
def show_user(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="User not found")
    return schemas.ShowUser.from_orm(user)

@router.get("/", tags=["users"])
def all_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    users = db.query(models.User).all()
    return [schemas.ShowUser.from_orm(user) for user in users]

@router.delete("/{id}")
def destroy_user(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
