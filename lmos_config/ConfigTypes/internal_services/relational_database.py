from pydantic import BaseModel, Field, AnyUrl

class RelationalDatabaseConfig(BaseModel):
    """
    Database Configuration. This tells LMOS how to connect to your relational database.
    [Engine Configuration](https://docs.sqlalchemy.org/en/20/core/engines.html)
    """

    url: AnyUrl = Field(
        ...,
        description="Database Connection URL. This should be any SQLAlchemy support url or similar",
    )