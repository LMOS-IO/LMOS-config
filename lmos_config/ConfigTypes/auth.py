from pydantic import BaseModel, Field

class AuthConfig(BaseModel):
    key_prefix: str = Field("lmos") 