# Botanical

Compressed symbolic reasoning for LLMs.

## What It Does

Recursive LLM calls build a symbolic program.

Each call adds symbols. No English. No verbose chain-of-thought.

Final iteration triggers decoder. Symbols become answer.

## Install

```bash
pip install anthropic
```

## Usage

```python
from reasoner import reason

result = reason("Your problem here")
print(result)
```

## Files

- `system_prompt.txt` — instructions for symbolic output
- `botanical.py` — the engine
- `reasoner.py` — the interface

## Symbol Reference

| Symbol | Meaning |
|--------|---------|
| ⌁ | ground truth |
| ◇ | input |
| → | implies |
| ⇒ | therefore |
| ⊕ | and |
| ⊖ | or |
| ⊘ | not |
| △ | branch |
| ⊢ | conclude |
| ≈ | approximate |
| ⬡ | compress |
| ◾ | halt |
