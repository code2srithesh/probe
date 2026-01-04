from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # We must explicitly list every variable in the .env file
    database_url: str
    gemini_api_key: str 

    class Config:
        env_file = ".env"
        # This tells Pydantic: "If there are other variables in .env, ignore them, don't crash."
        extra = "ignore" 

settings = Settings()