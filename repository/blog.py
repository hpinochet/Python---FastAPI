from fastapi import  Depends, status, HTTPException
from schemas import Blog
from models import Blog as BlogModel
from sqlalchemy.orm import Session
from database import get_db

def get_all_blogs(db: Session):
    blogs = db.query(BlogModel).all()
    return blogs

def get_blog_id(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    return blog

def post_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def put_blog(id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return "updated"

def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"     