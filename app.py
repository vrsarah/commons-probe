import platform
from pathlib import Path

from shiny.express import render

from commons._execution import _sandbox


def _try(fn):
    try:
        return fn()
    except Exception as err:
        return f"{type(err).__name__}: {err}"


@render.code
def out():
    return "\n".join(
        [
            f"kernel: {platform.release()}",
            f"lsm: {_try(lambda: Path('/sys/kernel/security/lsm').read_text())}",
            f"capabilities: {_try(_sandbox.sandbox_capabilities)}",
            f"protection_mode: {_try(_sandbox.protection_mode)}",
        ]
    )
