import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from api.routers import all_routers


origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://0.0.0.0:8000",
    "*"
]


def create_app() -> FastAPI:
    app = FastAPI(title="ToDoCalendar",
                  debug=False
                  )
    # for local start
    # app.mount("/static", StaticFiles(directory="front/static"), name="static")

    # for docker start
    app.mount("/static", StaticFiles(directory="src/front/static"), name="static")

    # Register all routers
    for router in all_routers:
        app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
        allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                       "Authorization"],
    )

    return app


app = create_app()


if __name__ == "__main__":
    # for docker start
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

    # for local start
    # uvicorn.run("app:app", reload=True)
