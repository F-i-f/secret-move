secret-move: a tool to list, copy and move libsecret secrets between keyrings
==============================================================================

# Installation

## With pip

``` shell
pip install secret-move
```

# Usage

## List keyrings

``` shell
secret-move keyrings
```

## List keyring contents

``` shell
secret-move list
secret-move list -v
secret-move list -vv
secret-move list -s OtherKeyring
```

## Copy keyring contents

``` shell
secret-move copy OtherKeyring Secret1
secret-move copy -s SourceKeyring DestKeyring Secret1
```

## Move keyring contents

``` shell
secret-move move OtherKeyring Secret1
secret-move move -s SourceKeyring DestKeyring Secret1
```

## Move/copy by regular expression

``` shell
secret-move move OtherKeyring -r 'RDP.*'
```
