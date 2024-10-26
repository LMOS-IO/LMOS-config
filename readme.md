# LMOS-Config
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![API Docs](https://img.shields.io/badge/API-Documentation-green)](https://docs.lmos.io)
[![Schema](https://img.shields.io/badge/Schema-JSON-blue)](https://lmos-io.github.io/LMOS-config/schema.json)

> Configuration management and validation for LMOS (Language Model Orchestration System)

## Overview
LMOS-Config provides a unified configuration system for the entire LMOS ecosystem. It includes schema validation, IDE support via JSON schema, and flexible loading options for both local and HTTP-based configurations. S3 integration planned.

## Features
- 🔍 **Schema Validation**: Pydantic-based validation for all configuration options
- 💡 **IDE Integration**: VSCode integration with JSON schema for autocompletion
- 🌐 **Flexible Loading**: Support for both local and HTTP-based configuration files
- 🔄 **Auto-generated Schema**: GitHub Actions workflow to maintain up-to-date JSON schema
- 📝 **YAML & JSON Support**: Load configurations from either YAML or JSON formats

## Usage

### Basic Configuration
Add the schema reference to your YAML config file:
```yaml
# yaml-language-server: $schema=https://lmos-io.github.io/LMOS-config/schema.json

internal_configuration:
  redis:
    redis_url: redis://localhost:6379
  # ... more configuration
```

### 2. Loading Configuration

#### Local Configuration
Set `LMOS_CONFIG_YAML_PATH` env var to the path for your config.yaml IE: `"path/to/your/config.yaml"`

#### HTTP Configuration
Set `LMOS_CONFIG_HTTP_URL` env var to the url for your config.yaml IE: `"https://example.com/config.yaml"`


## Configuration Structure

### Internal Configuration
- **Redis**: Connection settings for Redis
- **Database**: Database connection configuration
- **Prometheus**: Logging and monitoring settings

### Services Configuration
- **Router**: LMOS Router settings
- **LLM Runner**: Language model service configurations
- **STT Runner**: Speech-to-text service configurations
- **TTS Runner**: Text-to-speech service configurations
- **Rerank Runner**: Document reranking service configurations

## Development

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt
```

### Generate Schema
```bash
# Generate new schema.json
python export-schema.py
```

### Running Tests
```bash
# Test local configuration loading
python quick_test_local.py

# Test HTTP configuration loading
python quick_test_http.py
```

## Continuous Integration

The repository includes a GitHub Actions workflow (`schema_gen.yml`) that:
1. Generates the JSON schema from the Pydantic models
2. Deploys the schema to GitHub Pages
3. Makes it available at `https://lmos-io.github.io/LMOS-config/schema.json`

## Project Structure
```
├── lmos_config/
│   ├── ConfigTypes/
│   │   └── base.py          # Core configuration models
│   ├── http_config.py       # HTTP configuration loader
│   └── local_config.py      # Local configuration loader
├── example_configurations/   # Example configuration files
├── export-schema.py         # Schema generation script
└── .github/workflows/       # CI/CD workflows
```

## Contributing
0. Join the discord, chat about what you'd like to do
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
Apache 2.0 - See [LICENSE](LICENSE) for details

## Part of the LMOS Ecosystem
This package is part of the larger LMOS (Language Model Orchestration System) ecosystem. Visit [LMOS.io](https://lmos.io) to learn more about our other packages and services.