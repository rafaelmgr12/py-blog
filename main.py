from src.infra.web.webserver import WebServer

if __name__ == "__main__":
    server = WebServer(port=8080)
    def example_route():
        return {"message": "Dynamic route response"}

    server.add_route("/dynamic", example_route, ["GET", "POST"])
    server.run()