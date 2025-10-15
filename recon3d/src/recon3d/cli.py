from __future__ import annotations

import argparse
import sys

from . import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="recon3d", description="CLI de recon3d")
    parser.add_argument("command", nargs="?", default=None, help="Comando a ejecutar (p.ej., smoke)")
    parser.add_argument("--version", action="version", version=f"recon3d {__version__}")

    args = parser.parse_args(argv)

    if args.command in (None, "help"):
        parser.print_help()
        return 0

    if args.command == "smoke":
        print("recon3d: smoke OK")
        return 0

    print(f"Comando desconocido: {args.command}", file=sys.stderr)
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

