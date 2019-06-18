# flake8-assertAlmostEqual
A `Flake8` plugin to check for the use of `round()` in `assertEqual` and `assertAlmostEqual`.

It detects and flags two issues:

  - AAE100 Don't use 'assertAlmostEqual' with 'round'. Use it's implemented rounding.
  - AAE110 Don't use 'assertEqual' with 'round'. Use 'assertAlmostEqual' instead.

## Don't use `assertAlmostEqual` with `round`... (AAE100)
`assertAlmostEqual` has built in rounding. Thus `round()` is not required.

### Anti-pattern

```python
assertAlmostEqual(round(my_result, 2), 1.52)
```

### Best practice
```python
assertAlmostEqual(my_result, 1.52, 2)
```

## Don't use `assertEqual` with `round`... (AAE110)
If you need rounding, don't use `assertEqual`. Use `assertAlmostEqual`
instead.

### Anti-pattern
```python
assertEqual(round(my_result, 2), 1.52)
```

### Best practice
```python
assertAlmostEqual(my_result, 1.52, 2)
```
