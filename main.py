from fastapi import FastAPI
import uvicorn
from database import engine
import models
from routers import blog, user, login

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

# Original code commented out for reference
"""
@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return schemas.ShowBlog.from_orm(new_blog)

@app.get("/blog/{id}", status_code=200, tags=["blogs"])
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="Blog not found")
    return schemas.ShowBlog.from_orm(blog)

@app.get("/blogs", tags=["blogs"])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return [schemas.ShowBlog.from_orm(blog) for blog in blogs]

@app.delete("/blog/{id}", tags=["blogs"])
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

@app.put("/blog/{id}", status_code=200, tags=["blogs"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.title = request.title
    blog.body = request.body
    blog.user_id = request.user_id
    db.commit()
    db.refresh(blog)
    return schemas.ShowBlog.from_orm(blog)

# User endpoints
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@app.post("/user", status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return schemas.ShowUser.from_orm(new_user)

@app.get("/user/{id}", status_code=200, tags=["users"])
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="User not found")
    return schemas.ShowUser.from_orm(user)

@app.get("/users", tags=["users"])
def all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return [schemas.ShowUser.from_orm(user) for user in users]

@app.delete("/user/{id}", tags=["users"])
def destroy_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)