from typing import List, Optional, Literal
from ..generic.service import InternalService
from pydantic import BaseModel, ConfigDict

class vLLMArgs(BaseModel):
    # chatGPT built this from the official docs
    # https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#command-line-arguments-for-the-server
    tokenizer: Optional[str] = None
    skip_tokenizer_init: Optional[bool] = None
    revision: Optional[str] = None
    code_revision: Optional[str] = None
    tokenizer_revision: Optional[str] = None
    tokenizer_mode: Optional[Literal["auto", "slow", "mistral"]] = None
    trust_remote_code: Optional[bool] = None
    download_dir: Optional[str] = None
    load_format: Optional[Literal[
        "auto", "pt", "safetensors", "npcache", "dummy", "tensorizer",
        "sharded_state", "gguf", "bitsandbytes", "mistral"
    ]] = None
    config_format: Optional[Literal["auto", "hf", "mistral"]] = None
    dtype: Optional[Literal[
        "auto", "half", "float16", "bfloat16", "float", "float32"
    ]] = None
    kv_cache_dtype: Optional[Literal["auto", "fp8", "fp8_e5m2", "fp8_e4m3"]] = None
    quantization_param_path: Optional[str] = None
    max_model_len: Optional[int] = None
    guided_decoding_backend: Optional[Literal["outlines", "lm-format-enforcer"]] = None
    distributed_executor_backend: Optional[Literal["ray", "mp"]] = None
    worker_use_ray: Optional[bool] = None
    pipeline_parallel_size: Optional[int] = None
    tensor_parallel_size: Optional[int] = None
    max_parallel_loading_workers: Optional[int] = None
    ray_workers_use_nsight: Optional[bool] = None
    block_size: Optional[Literal[8, 16, 32]] = None
    enable_prefix_caching: Optional[bool] = None
    disable_sliding_window: Optional[bool] = None
    use_v2_block_manager: Optional[bool] = None
    num_lookahead_slots: Optional[int] = None
    seed: Optional[int] = None
    swap_space: Optional[int] = None
    cpu_offload_gb: Optional[int] = None
    gpu_memory_utilization: Optional[float] = None
    num_gpu_blocks_override: Optional[int] = None
    max_num_batched_tokens: Optional[int] = None
    max_num_seqs: Optional[int] = None
    max_logprobs: Optional[int] = None
    disable_log_stats: Optional[bool] = None
    quantization: Optional[Literal[
        "aqlm", "awq", "deepspeedfp", "tpu_int8", "fp8", "fbgemm_fp8",
        "modelopt", "marlin", "gguf", "gptq_marlin_24", "gptq_marlin",
        "awq_marlin", "gptq", "compressed-tensors", "bitsandbytes", "qqq",
        "experts_int8", "neuron_quant", "ipex", None
    ]] = None
    rope_scaling: Optional[str] = None
    rope_theta: Optional[float] = None
    enforce_eager: Optional[bool] = None
    max_context_len_to_capture: Optional[int] = None
    max_seq_len_to_capture: Optional[int] = None
    disable_custom_all_reduce: Optional[bool] = None
    tokenizer_pool_size: Optional[int] = None
    tokenizer_pool_type: Optional[str] = None
    tokenizer_pool_extra_config: Optional[str] = None
    limit_mm_per_prompt: Optional[int] = None
    mm_processor_kwargs: Optional[str] = None
    enable_lora: Optional[bool] = None
    max_loras: Optional[int] = None
    max_lora_rank: Optional[int] = None
    lora_extra_vocab_size: Optional[int] = None
    lora_dtype: Optional[Literal["auto", "float16", "bfloat16", "float32"]] = None
    long_lora_scaling_factors: Optional[str] = None
    max_cpu_loras: Optional[int] = None
    fully_sharded_loras: Optional[bool] = None
    enable_prompt_adapter: Optional[bool] = None
    max_prompt_adapters: Optional[int] = None
    max_prompt_adapter_token: Optional[int] = None
    device: Optional[Literal[
        "auto", "cuda", "neuron", "cpu", "openvino", "tpu", "xpu"
    ]] = None
    num_scheduler_steps: Optional[int] = None
    multi_step_stream_outputs: Optional[bool] = None
    scheduler_delay_factor: Optional[float] = None
    enable_chunked_prefill: Optional[bool] = None
    speculative_model: Optional[str] = None
    speculative_model_quantization: Optional[Literal[
        "aqlm", "awq", "deepspeedfp", "tpu_int8", "fp8", "fbgemm_fp8",
        "modelopt", "marlin", "gguf", "gptq_marlin_24", "gptq_marlin",
        "awq_marlin", "gptq", "compressed-tensors", "bitsandbytes", "qqq",
        "experts_int8", "neuron_quant", "ipex", None
    ]] = None
    num_speculative_tokens: Optional[int] = None
    speculative_disable_mqa_scorer: Optional[bool] = None
    speculative_draft_tensor_parallel_size: Optional[int] = None
    speculative_max_model_len: Optional[int] = None
    speculative_disable_by_batch_size: Optional[bool] = None
    ngram_prompt_lookup_max: Optional[int] = None
    ngram_prompt_lookup_min: Optional[int] = None
    spec_decoding_acceptance_method: Optional[Literal[
        "rejection_sampler", "typical_acceptance_sampler"
    ]] = None
    typical_acceptance_sampler_posterior_threshold: Optional[float] = None
    typical_acceptance_sampler_posterior_alpha: Optional[float] = None
    disable_logprobs_during_spec_decoding: Optional[bool] = None
    model_loader_extra_config: Optional[str] = None
    ignore_patterns: Optional[str] = None
    preemption_mode: Optional[str] = None
    served_model_name: Optional[List[str]] = None
    qlora_adapter_name_or_path: Optional[str] = None
    otlp_traces_endpoint: Optional[str] = None
    collect_detailed_traces: Optional[bool] = None
    disable_async_output_proc: Optional[bool] = None
    override_neuron_config: Optional[str] = None
    scheduling_policy: Optional[Literal["fcfs", "priority"]] = None

    model_config  = ConfigDict(protected_namespaces=())

class vLLMRunner(InternalService, vLLMArgs):
    """vLLM runner config"""

    type: Literal["vllm"]
    _port: int = 8000

