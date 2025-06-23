import os
import sys
import tomllib

from jinja2 import Environment, PackageLoader, select_autoescape

from pathlib import Path


def read_file(fp: Path) -> str:
    with fp.open("r") as f:
        return f.read()


def main() -> None:
    sections: list[map] = []
    env = Environment(
        loader=PackageLoader("code_of_conduct"),
        autoescape=select_autoescape(),
    )

    for dirpath, _, filenames in os.walk("./code_of_conduct/sections/"):
        filenames.sort()
        for filename in filenames:
            output = read_file(Path(dirpath) / Path(filename))
            sections.append(tomllib.loads(output))

    template = env.get_template("README.md.jinja")

    with Path("README.md").open("w") as f:
        print(template.render(sections=sections), file=f)


if __name__ == "__main__":
    sys.exit(main())
