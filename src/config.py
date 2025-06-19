from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Directory for the databases
DATABASE_DIR = Path.cwd().joinpath("databases")
DATABASE_DIR.mkdir(exist_ok=True)

# Paths to the embedded databases
RELATIONAL_DB_PATH = DATABASE_DIR.joinpath("heurist.duckdb")
GRAPH_DB_PATH = DATABASE_DIR.joinpath("kuzu_db")

# Directory for static files
STATIC_FILES = Path.cwd().joinpath("static")
STATIC_FILES.mkdir(exist_ok=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=False,
        extra="ignore",
    )

    # environment variables
    DB_NAME: str = "jbcamps_gestes"
    HEURIST_LOGIN: str  # loaded from .env file with the model_config
    HEURIST_PASSWORD: str  # loaded from .env file with model_config

    # Dynamic paths
    DUCKDB_PATH: Path = RELATIONAL_DB_PATH
    KUZU_PATH: Path = GRAPH_DB_PATH
    STATIC_FILES: Path = STATIC_FILES


settings = Settings()
