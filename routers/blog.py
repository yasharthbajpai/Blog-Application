from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
import schemas
import models
from routers.login import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return schemas.ShowBlog.from_orm(new_blog)

@router.get("/{id}", status_code=200)
def show(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).options(joinedload(models.Blog.creator)).filter(models.Blog.id == id).first()
    if not blog:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="Blog not found")
    return schemas.ShowBlog.from_orm(blog)

@router.get("/", tags=["blogs"])
def all(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).options(joinedload(models.Blog.creator)).all()
    return [schemas.ShowBlog.from_orm(blog) for blog in blogs]

@router.delete("/{id}")
def destroy(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this blog")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

@router.put("/{id}", status_code=200)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this blog")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return schemas.ShowBlog.from_orm(blog)
