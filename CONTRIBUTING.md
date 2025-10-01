# Contributing to the Code of Conduct

## How the Code of Conduct is created

Rules are made from sections, these sections are in a
`section{index}.toml` that you can find in `code_of_conduct/sections/`.
Additionally, rules can have expectations, as well as a glossary.

## How to add new rules

A rule can be added by opening the section you want to add a new rule
to (read [here](#how-to-add-a-new-section) if you want to make a new
section) and add something of the following format:

```toml
[[rule]]
# EXPECTED TO EXIST
title = "My new rule"
description = """
I am describing my new rule.
"""

# OPTIONAL
[[rule.expectations]]
expectation = "Mild"
description = """
Hello world! This is your punishment for doing something bad! Feel the
wrath of the sword!
"""

[[rule.glossary]]
word = "describing"
meaning = "talking about"
```

### Guidelines
- You are expected to keep every line around 72 characters long for
  readability purposes.
- Make sure the quotes and the text are separate from each other for
  readability.
- If using bullet points, do not title them.

## How to add a new section

To create a new section, you can create a new file in
`code_of_conduct/sections/{{index}}.toml` to maintain consistency
as well as not trip the generator into writing the COC out of order.

```toml
title = "My section"

[[rule]]
title = "My rule"
description = "Description of my rule."

# fill in the rest
```

## What to do after you made your changes

We use GitHub Actions to handle updating the COC, though if you are
updating it manually, follow the steps below.

### Setting up your development environment

Before setting up your development environment, please make sure you are
running Python version 3.11 or above by running `python --version`.

We use `uv` for dependency management and virtual environment handling.
If you don't have `uv` installed, you can install it using:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pipx
pipx install uv

# Or using pip
pip install uv
```

Once you have `uv` installed, you can set up your development environment
by running:

```bash
# This will create a virtual environment and install dependencies
uv sync
```

You can then test your changes by generating the README to a temporary file:
```bash
uv run gencoc-test
```

This will create a `test-README.md` file that you can review to ensure
your changes are correct without modifying the actual `README.md`. Don't change
the actual `README.md`, the CI will handle that for you when changes are merged to main.
