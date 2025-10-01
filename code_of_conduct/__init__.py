import os
import sys
import tomllib

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

def _run(output_path: Path, verbose: bool = False) -> None:
    # Get the directory where this module is located
    package_dir = Path(__file__).parent

    env = Environment(
        loader=FileSystemLoader(package_dir / "templates"),
        autoescape=select_autoescape(),
    )

    sections: list[dict] = []
    sections_dir = package_dir / "sections"
    for dirpath, _, filenames in os.walk(sections_dir):
        for filename in sorted(filenames):
            content = Path(dirpath, filename).read_text(encoding="utf-8")
            sections.append(tomllib.loads(content))

    rendered = env.get_template("README.md.jinja").render(sections=sections)
    output_path.write_text(rendered, encoding="utf-8")

    if verbose:
        print(f"Generated {output_path.name} for local development")


def main() -> None:
    if len(sys.argv) > 2:
        raise AssertionError(f"expected 0 to 1 arguments, got {len(sys.argv) - 1}")

    out = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("README.md")
    _run(out)


def main_test() -> None:
    """Generate test-README.md for local development."""
    _run(Path("test-README.md"), verbose=True)
