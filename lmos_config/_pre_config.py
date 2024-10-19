"""This document exports a variable called `PreConfigOptions` that will expose locations to load a config file pulled from environment variables"""

from typing import Optional
from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema
from pydantic_settings import BaseSettings

__all__ = [
    "PreConfigOptions",
]


class S3BucketConfiguration(BaseModel):
    name: str = Field(..., description="Name of the S3 bucket")
    access_key: Optional[str] = Field(None, description="Access key for S3 bucket")
    secret_key: Optional[str] = Field(None, description="Secret key for S3 bucket")
    region: Optional[str] = Field(None, description="AWS region for the S3 bucket")


class PreConfigConfigurationOptions(BaseSettings):
    PRELOAD_CONFIG: SkipJsonSchema[bool] = Field(False, description="**internal** attribute to skip the loading of a json schema")

    http_url: Optional[str] = Field(
        None, description="HTTP(s) URL to load the configuration from"
    )
    s3_bucket: Optional[S3BucketConfiguration] = Field(
        None, description="S3 bucket configuration"
    )
    yaml_path: Optional[str] = Field(
        '/usr/src/app/config.yaml',
        description="Path to the YAML configuration file"
    )

    class Config:
        env_prefix = "LMOS_CONFIG_"


PreConfigOptions = PreConfigConfigurationOptions()
