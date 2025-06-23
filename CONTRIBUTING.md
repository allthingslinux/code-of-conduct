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

### Setting up your .venv

Before setting up `.venv`, please make sure you are running version
3.11 or above by running `python --version`. After checking and
verifying that you have a high enough version, you can setup a .venv by
running this command in your shell:
```
$ python -m venv .venv
```
This will create a .venv directory which will contain a local
development environment you can access by sourcing `.venv/bin/activate`.
You will want to check for an activation script that supports your shell
however. If you are on PowerShell, you will need to source
`.venv/bin/activate.ps1`, fish users must source `activate.fish` and so
on with other shells.

Once you are in your .venv environment, make sure pip is up to date by
running this command:
```
$ pip install --upgrade pip
```

We must now install `poetry` to install the COC generator. This can be
done with the following command:
```
$ pip install poetry
```
You will then be able to use poetry to install our package as well as
any dependencies needed for said package. This can be done by running
the following command:
```
$ poetry install
```

You can then generate the README by running the following command:
```
$ python -m code_of_conduct
```
The README will then be modified to include your changed you made. You
can now commit your work, but make sure to add `[skip ci]` to avoid
unnecessarily running the CI. After that, you can make a pull request.
