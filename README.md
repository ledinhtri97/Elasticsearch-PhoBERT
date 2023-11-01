# Search with Elasticsearch (ES) and a Language Model

An Big Data topic. Semantic Search with Elasticsearch and a Large Language model

## Prerequisites
If you are planning to run the Flask app locally, you also need
- Python 3.10 or above (Recommended installing by [pyenv](https://github.com/pyenv/pyenv))
- [Poetry](https://python-poetry.org)
- Ubuntu (Recommended)
- [Docker](https://docs.docker.com/desktop/install/linux-install)

## Installation

### Quickstart

#### Stop all services and clean up resources

```zsh
sh scripts/bash.stop.all.sh
```

#### Start every services (Elasticsearch + Kibana + Flask server)

```zsh
# Without CUDA
sh scripts/bash.run.all.sh

```

## Clean up resources

```zsh
sh bash.run.clean.sh
```

## Usage

Access the site at <http://127.0.0.1:5000>
