# ft_package

A sample test package.

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

## API

### `count_in_list(lst: list[str], target: str) -> int`

Return how many times `target` appears in `lst`.

## License

MIT
