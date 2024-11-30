# `ai`

**Usage**:

```console
ai [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `commit`
- `repo`

## `ai commit`

**Usage**:

```console
ai commit [OPTIONS] [PATH]...
```

**Arguments**:

- `[PATH]...`

**Options**:

- `--default-exclude / --no-default-exclude`: [default: default-exclude]
- `--verify / --no-verify`: [default: verify]
- `--model TEXT`
- `--help`: Show this message and exit.

## `ai repo`

**Usage**:

```console
ai repo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `description`
- `topics`

### `ai repo description`

**Usage**:

```console
ai repo description [OPTIONS]
```

**Options**:

- `--long / --no-long`: [default: no-long]
- `--model TEXT`
- `--help`: Show this message and exit.

### `ai repo topics`

**Usage**:

```console
ai repo topics [OPTIONS]
```

**Options**:

- `--model TEXT`
- `--help`: Show this message and exit.
