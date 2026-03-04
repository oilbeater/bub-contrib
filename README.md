# bub-contrib

Contributions and packages for the `bub` ecosystem.

## Repository Layout

- `packages/tg-feed`: Python package for Telegram feed related functionality.

## Development

### Prerequisites

- Python 3.10+
- `uv` or `pip`

### Setup

```bash
cd packages/tg-feed
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Run Tests

```bash
cd packages/tg-feed
pytest
```

## License

This repository is licensed under the terms in [LICENSE](./LICENSE).
