from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 8000

    db_host = 'postgres'
    db_name = 'university'
    database_url: str = f'postgresql://postgres:123456@{db_host}/{db_name}'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
