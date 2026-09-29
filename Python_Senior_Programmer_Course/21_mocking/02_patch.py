from unittest.mock import patch
from pathlib import Path

def load_name():
    return Path("user.txt").read_text()
with patch.object(Path, "read_text", return_value="Ada"):
    print(load_name())