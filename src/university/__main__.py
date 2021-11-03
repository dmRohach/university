import uvicorn

from .config import settings

uvicorn.run(
    'university.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
