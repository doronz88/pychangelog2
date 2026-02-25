# pychangelog2

Generate a simple changelog from Git history.

`pychangelog2` prints commit lines in chronological order and is designed for
release notes workflows where commit subjects are already clean and meaningful.

## Features

- Generates changelog entries from a local Git repository path.
- Defaults to commits from the latest tag to `HEAD`.
- Supports explicit `--start-tag` and `--end-tag` ranges.
- Excludes merge commits created by GitHub PR merges and branch merges.

## Installation

Install from PyPI:

```bash
python3 -m pip install --user -U pychangelog2
```

Install from source:

```bash
git clone https://github.com/doronz88/pychangelog2.git
cd pychangelog2
python3 -m pip install -e .
```

## Usage

```bash
pychangelog2 [OPTIONS] PATH
```

- `PATH`: path to a local Git repository.
- `--start-tag TEXT`: start changelog after this tag.
- `--end-tag TEXT`: end changelog at this tag (defaults to `HEAD`).

## Behavior

- If `--start-tag` is omitted, the tool starts from the most recently authored
  tag in the repository.
- If `--end-tag` is provided, `--start-tag` is required.
- If a provided tag does not exist, the command exits with an error.
- Output format is:

```text
* <full-commit-sha> <first-line-of-commit-message>
```

## Examples

Generate changelog from the latest tag to `HEAD`:

```bash
pychangelog2 /path/to/repo
```

Generate changelog from a specific tag to `HEAD`:

```bash
pychangelog2 /path/to/repo --start-tag v1.2.0
```

Generate changelog between two tags:

```bash
pychangelog2 /path/to/repo --start-tag v1.2.0 --end-tag v1.4.0
```
