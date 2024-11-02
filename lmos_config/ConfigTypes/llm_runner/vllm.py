from typing import List, Optional, Literal
from ..generic.service import InternalService


class vLLMRunner(InternalService):
    """ExllamaV2 runner config"""

    type: Literal["vllm"]

    # chatGPT built this from the official docs
    # https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#command-line-arguments-for-the-server
    #  model: Optional[str]
    tokenizer: Optional[str]
    skip_tokenizer_init: Optional[bool] = False
    revision: Optional[str]
    code_revision: Optional[str]
    tokenizer_revision: Optional[str]
    tokenizer_mode: Optional[Literal["auto", "slow", "mistral"]]
    trust_remote_code: Optional[bool] = False
    download_dir: Optional[str]
    load_format: Optional[Literal[
        "auto", "pt", "safetensors", "npcache", "dummy", "tensorizer",
        "sharded_state", "gguf", "bitsandbytes", "mistral"
    ]]
    config_format: Optional[Literal["auto", "hf", "mistral"]]
    dtype: Optional[Literal[
        "auto", "half", "float16", "bfloat16", "float", "float32"
    ]]
    kv_cache_dtype: Optional[Literal["auto", "fp8", "fp8_e5m2", "fp8_e4m3"]]
    quantization_param_path: Optional[str]
    max_model_len: Optional[int]
    guided_decoding_backend: Optional[Literal["outlines", "lm-format-enforcer"]]
    distributed_executor_backend: Optional[Literal["ray", "mp"]]
    worker_use_ray: Optional[bool] = False
    pipeline_parallel_size: Optional[int]
    tensor_parallel_size: Optional[int]
    max_parallel_loading_workers: Optional[int]
    ray_workers_use_nsight: Optional[bool] = False
    block_size: Optional[Literal[8, 16, 32]]
    enable_prefix_caching: Optional[bool] = False
    disable_sliding_window: Optional[bool] = False
    use_v2_block_manager: Optional[bool] = False
    num_lookahead_slots: Optional[int]
    seed: Optional[int]
    swap_space: Optional[int]
    cpu_offload_gb: Optional[int]
    gpu_memory_utilization: Optional[float]
    num_gpu_blocks_override: Optional[int]
    max_num_batched_tokens: Optional[int]
    max_num_seqs: Optional[int]
    max_logprobs: Optional[int]
    disable_log_stats: Optional[bool] = False
    quantization: Optional[Literal[
        "aqlm", "awq", "deepspeedfp", "tpu_int8", "fp8", "fbgemm_fp8",
        "modelopt", "marlin", "gguf", "gptq_marlin_24", "gptq_marlin",
        "awq_marlin", "gptq", "compressed-tensors", "bitsandbytes", "qqq",
        "experts_int8", "neuron_quant", "ipex", None
    ]]
    rope_scaling: Optional[str]
    rope_theta: Optional[float]
    enforce_eager: Optional[bool] = False
    max_context_len_to_capture: Optional[int]
    max_seq_len_to_capture: Optional[int]
    disable_custom_all_reduce: Optional[bool] = False
    tokenizer_pool_size: Optional[int]
    tokenizer_pool_type: Optional[str]
    tokenizer_pool_extra_config: Optional[str]
    limit_mm_per_prompt: Optional[int]
    mm_processor_kwargs: Optional[str]
    enable_lora: Optional[bool] = False
    max_loras: Optional[int]
    max_lora_rank: Optional[int]
    lora_extra_vocab_size: Optional[int]
    lora_dtype: Optional[Literal["auto", "float16", "bfloat16", "float32"]]
    long_lora_scaling_factors: Optional[str]
    max_cpu_loras: Optional[int]
    fully_sharded_loras: Optional[bool] = False
    enable_prompt_adapter: Optional[bool] = False
    max_prompt_adapters: Optional[int]
    max_prompt_adapter_token: Optional[int]
    device: Optional[Literal[
        "auto", "cuda", "neuron", "cpu", "openvino", "tpu", "xpu"
    ]]
    num_scheduler_steps: Optional[int]
    multi_step_stream_outputs: Optional[bool] = False
    scheduler_delay_factor: Optional[float]
    enable_chunked_prefill: Optional[bool] = False
    speculative_model: Optional[str]
    speculative_model_quantization: Optional[Literal[
        "aqlm", "awq", "deepspeedfp", "tpu_int8", "fp8", "fbgemm_fp8",
        "modelopt", "marlin", "gguf", "gptq_marlin_24", "gptq_marlin",
        "awq_marlin", "gptq", "compressed-tensors", "bitsandbytes", "qqq",
        "experts_int8", "neuron_quant", "ipex", None
    ]]
    num_speculative_tokens: Optional[int]
    speculative_disable_mqa_scorer: Optional[bool] = False
    speculative_draft_tensor_parallel_size: Optional[int]
    speculative_max_model_len: Optional[int]
    speculative_disable_by_batch_size: Optional[bool] = False
    ngram_prompt_lookup_max: Optional[int]
    ngram_prompt_lookup_min: Optional[int]
    spec_decoding_acceptance_method: Optional[Literal[
        "rejection_sampler", "typical_acceptance_sampler"
    ]]
    typical_acceptance_sampler_posterior_threshold: Optional[float]
    typical_acceptance_sampler_posterior_alpha: Optional[float]
    disable_logprobs_during_spec_decoding: Optional[bool] = False
    model_loader_extra_config: Optional[str]
    ignore_patterns: Optional[str]
    preemption_mode: Optional[str]
    served_model_name: Optional[List[str]]
    qlora_adapter_name_or_path: Optional[str]
    otlp_traces_endpoint: Optional[str]
    collect_detailed_traces: Optional[bool] = False
    disable_async_output_proc: Optional[bool] = False
    override_neuron_config: Optional[str]
    scheduling_policy: Optional[Literal["fcfs", "priority"]]
