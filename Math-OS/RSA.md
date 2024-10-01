# RSA

```python
def code_ou_decode(clef: int, commun: int, message: int) -> int:
    return (message ** clef) % commun
```
