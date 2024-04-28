import os

from dotenv import load_dotenv

from src.app.usecase.user_usecase import UserUsecase
from src.infra.db.db import DBConnect
from src.infra.repository.user_repo import SQLUserRepository
from src.infra.web.handler.user_handler import UserHandler
from src.infra.web.webserver.webserver import WebServer
import asyncio

load_dotenv()




async def main(conn_str: str, port: int, host: str)-> None:
    # Initialize the database connection
    db_connect = DBConnect(connection_string=conn_str)  # Make sure to provide the actual connection string

    # Create session for the user repository
    async with db_connect.get_session() as session:
        user_repo = SQLUserRepository(session)
        user_usecase = UserUsecase(user_repo)
        user_handler = UserHandler(user_usecase)

        server = WebServer(port=port, host=host)

        # Add your existing routes
        def example_route():
            return {"message": "Wlecome to the server!"}
        server.add_route("/", example_route, ["GET"])

        # Add the create_user route
        server.add_route("/create_user", user_handler.create_user, ["POST"])

        # Run the server
        server.run()
if __name__ == "__main__":
    conn = os.getenv("POSTGRES_URL")
    port = os.getenv("PORT")
    host = os.getenv("HOST")

    async def main_wrapper():
        await main(conn, port, host)

    asyncio.run(main_wrapper())
