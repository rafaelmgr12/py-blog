import os
import asyncio
import uvicorn
from dotenv import load_dotenv

from src.app.usecase.user_usecase import UserUsecase
from src.infra.db.db import DBConnect
from src.infra.repository.blog_post_repo import SQLBlogPostRepository
from src.infra.repository.user_repo import SQLUserRepository
from src.infra.web.handler.blog_post_handler import BlogPostHandler
from src.infra.web.handler.user_handler import UserHandler
from src.infra.web.webserver.webserver import WebServer
from src.app.usecase.blog_post_usecase import BlogPostUseCase

load_dotenv()

create_user_response_dict = {400: "Email already exists"}

create_blog_response_dict = {400: "User not found"}


async def create_app(conn_str, port, host):
    # Initialize the database connection
    db_connect = DBConnect(connection_string=conn_str)

    # Async context manager for the session
    async with db_connect.get_session() as session:

        blog_repository = SQLBlogPostRepository(session)
        user_repo = SQLUserRepository(session)
        user_usecase = UserUsecase(user_repo)
        blog_usecase = BlogPostUseCase(blog_repository, user_repo)
        user_handler = UserHandler(user_usecase)
        blog_handler = BlogPostHandler(blog_usecase)
        server = WebServer(port=port, host=host)

        # Add routes
        server.add_route(
            "/",
            lambda: {
                "message": "Welcome to the server! Access /docs to see the documentation"
            },
            ["GET"],
        )
        server.add_route(
            "/user",
            user_handler.create_user,
            ["POST"],
            create_user_response_dict,
            ["User"],
            201,
        )

        server.add_route(
            path="/blogs",
            endpoint=blog_handler.create_blog_post,
            methods=["POST"],
            response_dict=create_blog_response_dict,
            tags=["Blog"],
            status_code=201,
        )

        return server.app


def main():
    conn_str = os.getenv("POSTGRES_URL")
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "localhost")

    app = asyncio.run(create_app(conn_str, port, host))

    # Directly run Uvicorn with the FastAPI app
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
