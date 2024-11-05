from pydantic import BaseModel, Field

class RouterConfig(BaseModel):
    """
    Configuration for the LMOS Router which delegates requests to the appropriate service.

    `log_request_dump_max_queue_size` and `log_request_dump_queue_timeout` are used to determine when to insert usage logs into the RDB.
    LMOS Router will queue usage logs internally to prevent delays in the request response cycle.

    It is recommended that you set the `log_request_dump_max_queue_size` such that it frequently triggers prior to reaching the the time limit specified by `log_request_dump_queue_timeout`.
    """

    log_request_dump_max_queue_size: int = Field(
        default=1000,
        description="In number of entries: Threshold for worker to insert usage logs into RDB",
    )
    log_request_dump_queue_timeout: int = Field(
        default=1000,
        description="In Seconds: The max time between worker inserting into RDB",
    )
