import os
import sys
import tomllib

from jinja2 import Environment, PackageLoader, select_autoescape

from pathlib import Path


def read_file(fp: Path) -> str:
    with fp.open("r") as f:
        return f.read()


TWO_ARGS = 2

def main() -> None:
    if len(sys.argv) > TWO_ARGS:
        error = f"expected 0 to 1 arguments, got {len(sys.argv) - 1}"
        raise AssertionError(error)

    env = Environment(
        loader=PackageLoader("code_of_conduct"),
        autoescape=select_autoescape(),
    )

    sections: list[map] = []
    for dirpath, _, filenames in os.walk("./src/code_of_conduct/sections/"):
        filenames.sort()
        for filename in filenames:
            output = read_file(Path(dirpath) / Path(filename))
            sections.append(tomllib.loads(output))

    template = env.get_template("README.md.jinja")

    path = sys.argv[1] if len(sys.argv) > 1 else "test-README.md"

    with Path(path).open("w", encoding="utf-8") as f:
        f.write(template.render(sections=sections))


def main_test() -> None:
    """Generate test-README.md for local development."""
    env = Environment(
        loader=PackageLoader("code_of_conduct"),
        autoescape=select_autoescape(),
    )

    sections: list[map] = []
    for dirpath, _, filenames in os.walk("./src/code_of_conduct/sections/"):
        filenames.sort()
        for filename in filenames:
            output = read_file(Path(dirpath) / Path(filename))
            sections.append(tomllib.loads(output))

    template = env.get_template("README.md.jinja")

    with Path("test-README.md").open("w", encoding="utf-8") as f:
        f.write(template.render(sections=sections))

    print("Generated test-README.md for local development")
