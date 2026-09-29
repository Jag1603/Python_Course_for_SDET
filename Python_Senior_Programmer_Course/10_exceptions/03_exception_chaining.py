try:
    int("abc")
except ValueError as exc:
    raise RuntimeError("Parsing failed") from exc