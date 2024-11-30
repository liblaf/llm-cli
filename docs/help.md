# `ai-cli`

**Usage**:

```console
ai-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `commit`
- `repo`

## `ai-cli commit`

**Usage**:

```console
ai-cli commit [OPTIONS] [PATH]...
```

**Arguments**:

- `[PATH]...`

**Options**:

- `--default-exclude / --no-default-exclude`: [default: default-exclude]
- `--verify / --no-verify`: [default: verify]
- `--model TEXT`
- `--help`: Show this message and exit.

## `ai-cli repo`

**Usage**:

```console
ai-cli repo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `description`
- `topics`

### `ai-cli repo description`

**Usage**:

```console
ai-cli repo description [OPTIONS]
```

**Options**:

- `--model TEXT`
- `--help`: Show this message and exit.

### `ai-cli repo topics`

**Usage**:

```console
ai-cli repo topics [OPTIONS]
```

**Options**:

- `--model TEXT`
- `--help`: Show this message and exit.
