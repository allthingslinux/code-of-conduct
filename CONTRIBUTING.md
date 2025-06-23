# Contributing to the Code of Conduct

> [!NOTE]
> This is a living document, and will grow with time. Please be aware
> that nothing in this document will last forever. Check back whenever
> you want to contribute.

## How the Code of Conduct is created

Rules are made from sections, these sections are in a
`section{index}.toml` that you can find in `code_of_conduct/sections/`.
This is done to standardise the code of conduct format, as well as
making it portable in case it were to be used in our own Tux for
example. There are some quirks with the format due to using Markdown
which will be described in this document.

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

You are expected to keep every line around 72 characters long for
readability purposes. You also should aim to use listing less as
paragraphs tend to work just about as well without being unmemorable.
Make sure the quotes and the text are separate from each other for
readability.

## How to add a new section

To create a new section, you can create a new file in
`code_of_conduct/sections`. Preferably, you can name it
`section{index}.toml` for consistency. You must write it out like below:
```toml
title = "My section"

[[rule]]
title = "My rule"
description = "Description of my rule."

# fill in the rest
```

## What to do after you made your changes

CI is not setup for this yet. As such, you will have to set up a
development environment for Python **3.11 and higher** to regenerate
the README file. This isn't an annoying process but we will eventually
add CI to make this step irrelevant.

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
pip install --upgrade pip
```
This is to prevent any vulnerabilities when installing software via pip,
and therefore it will be safer. We will now need `poetry` as pip doesn't
have a stable lockfile format as of now.

To install `poetry`, you must run this command:
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
can now commit your work and make a pull request.
