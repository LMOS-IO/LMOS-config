from pydantic import BaseModel, Field, AnyUrl

# Define the model for the internal configuration assets
class RedisConfig(BaseModel):
    """
    Redis Configuration. This tells LMOS how to connect to your redis instance.
    """

    url: AnyUrl = Field(
        ..., description="Redis Connection URL. This Should start with `redis://`"
    )
