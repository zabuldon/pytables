"""Start PyTables."""
import sys

from pytables.const import REQUIRED_PYTHON_VER


def validate_python() -> None:
    """Validate that the right Python version is running."""
    if sys.version_info[:3] < REQUIRED_PYTHON_VER:
        print("Home Assistant requires at least Python {}.{}.{}".format(*REQUIRED_PYTHON_VER))
        sys.exit(1)
