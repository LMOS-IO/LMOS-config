from typing import List, Optional, Literal
from ..generic.service import InternalService
from pydantic import BaseModel, ConfigDict

class SglangArgs(BaseModel):
    # mostly generated by chatGPT
    # reference: https://github.com/sgl-project/sglang/blob/218ab3611ddf46ce6acf8a465611a01faa275eb7/python/sglang/srt/server_args.py#L208
    # model_path: str
    tokenizer_path: Optional[str] = None
    host: str = "127.0.0.1"
    port: int = 8000
    tokenizer_mode: str = "auto"
    skip_tokenizer_init: bool = False
    load_format: str = "auto"
    trust_remote_code: bool = False
    dtype: str = "auto"
    kv_cache_dtype: str = "auto"
    quantization: Optional[str] = None
    context_length: Optional[int] = None
    device: str = "cuda"
    # served_model_name: Optional[str] = None
    chat_template: Optional[str] = None
    is_embedding: bool = False
    mem_fraction_static: Optional[float] = None
    max_running_requests: Optional[int] = None
    max_total_tokens: Optional[int] = None
    chunked_prefill_size: Optional[int] = None
    max_prefill_tokens: Optional[int] = None
    schedule_policy: str = "lpm"
    schedule_conservativeness: float = 1.0
    tp_size: int = 1
    stream_interval: int = 1
    random_seed: Optional[int] = None
    watchdog_timeout: Optional[float] = None
    log_level: str = "info"
    log_level_http: Optional[str] = None
    log_requests: bool = False
    show_time_cost: bool = False
    enable_metrics: bool = False
    decode_log_interval: Optional[int] = None
    api_key: Optional[str] = None
    file_storage_pth: Optional[str] = None
    enable_cache_report: bool = False
    dp_size: int = 1
    load_balance_method: str = "round_robin"
    dist_init_addr: Optional[str] = None
    nnodes: int = 1
    node_rank: int = 0
    json_model_override_args: Optional[str] = None
    enable_double_sparsity: bool = False
    ds_channel_config_path: Optional[str] = None
    ds_heavy_channel_num: Optional[int] = None
    ds_heavy_token_num: Optional[int] = None
    ds_heavy_channel_type: Optional[str] = None
    ds_sparse_decode_threshold: Optional[int] = None
    lora_paths: Optional[List[str]] = None
    max_loras_per_batch: int = 8
    attention_backend: Optional[str] = None
    sampling_backend: Optional[str] = None
    grammar_backend: Optional[str] = None
    disable_flashinfer: bool = False
    disable_flashinfer_sampling: bool = False
    disable_radix_cache: bool = False
    disable_jump_forward: bool = False
    disable_cuda_graph: bool = False
    disable_cuda_graph_padding: bool = False
    disable_disk_cache: bool = False
    disable_custom_all_reduce: bool = False
    disable_mla: bool = False
    disable_penalizer: bool = False
    disable_nan_detection: bool = False
    enable_overlap_schedule: bool = False
    enable_mixed_chunk: bool = False
    enable_torch_compile: bool = False
    torch_compile_max_bs: Optional[int] = None
    cuda_graph_max_bs: Optional[int] = None
    torchao_config: Optional[str] = None
    enable_p2p_check: bool = False
    triton_attention_reduce_in_fp32: bool = False
    num_continuous_decode_steps: int = 1
    delete_ckpt_after_loading: bool = False

    model_config  = ConfigDict(protected_namespaces=())

class SglangRunner(InternalService, SglangArgs):
    """sglang runner config"""

    type: Literal["sglang"]
    _port: int = 8000
