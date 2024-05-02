from src.app.model.blog_post import BlogPostRequestCreate, BlogPostResponse
from src.app.usecase.blog_post_usecase import BlogPostUseCase
from fastapi import HTTPException


class BlogPostHandler:
    def __init__(self, blog_post_usecase: BlogPostUseCase) -> None:
        self.blog_post_usecase = blog_post_usecase

    async def create_blog_post(self, payload: BlogPostRequestCreate) -> BlogPostResponse:

        try:
            blog_post = await self.blog_post_usecase.create_blog_post(
                payload.title, payload.content, payload.user_id
            )

            return BlogPostResponse(
                id=str(blog_post.id),
                title=blog_post.title,
                content=blog_post.content,
                user_id=str(blog_post.user_id),
                created_at=str(blog_post.created_at),
                updated_at=str(blog_post.updated_at),
            )

        except ValueError as e:
            if str(e) == "User not found":
                raise HTTPException(status_code=400, detail="User not found")
            else:
                raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
