from fastapi import APIRouter, Depends, status, Response
from schemas import Blog, ShowBlogTitle
from sqlalchemy.orm import Session
from database import get_db
from repository.blog import get_all_blogs, get_blog_id, post_blog, put_blog, delete_blog 

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.get("", response_model=list[ShowBlogTitle])
def get_blog(db: Session = Depends(get_db)):
    return get_all_blogs(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlogTitle)
def get_blog_by_id(id, db: Session = Depends(get_db)):
    return get_blog_id(id, db)   

@router.post("", status_code=status.HTTP_201_CREATED)
def create_blog(request: Blog, db: Session = Depends(get_db)):
    return post_blog(request, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: Blog, db: Session = Depends(get_db)):
    return put_blog(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    return delete_blog(id, db)