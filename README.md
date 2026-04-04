secret-move \
list, copy and move libsecret secrets between keyrings
=======================================================

[![Latest PyPI version](https://img.shields.io/pypi/v/secret-move.svg)](https://pypi.org/project/secret-move/)
[![CI](https://github.com/F-i-f/secret-move/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/F-i-f/secret-move/actions)

# Installation

## From PyPI

``` shell
pip install secret-move
```

## From git

``` shell
git clone https://github.com/F-i-f/secret-move.git
cd secret-move
python -m build
pip install dist/secret_move-*.whl
```

# Help screens

<pre><font color="#C01C28"><b>user@localhost:~/%</b></font> <font color="#008700"><b>secret-move</b></font> <font color="#005FFF">--help</font>
<font color="#12488B"><b>usage: </b></font><font color="#A347BA"><b>secret-move</b></font> [<font color="#26A269">-h</font>] [<font color="#26A269">-V</font>] <font color="#26A269">{copy,keyrings,list,move} ...</font>

List, copy and move secrets across libsecret keyrings.

<font color="#12488B"><b>positional arguments:</b></font>
  <font color="#26A269"><b>{copy,keyrings,list,move}</b></font>
						command to execute
	<font color="#26A269"><b>copy</b></font>                copy items between keyrings
	<font color="#26A269"><b>keyrings</b></font>            list all available keyrings
	<font color="#26A269"><b>list</b></font>                list all keys in a keyring
	<font color="#26A269"><b>move</b></font>                move items between keyrings

<font color="#12488B"><b>options:</b></font>
  <font color="#26A269"><b>-h</b></font>, <font color="#2AA1B3"><b>--help</b></font>            show this help message and exit
  <font color="#26A269"><b>-V</b></font>, <font color="#2AA1B3"><b>--version</b></font>         show version and copyright notice
</pre>

<pre>
<font color="#C01C28"><b>user@localhost:~/%</b></font> <font color="#008700"><b>secret-move</b></font> keyrings <font color="#005FFF">--help</font>
<font color="#12488B"><b>usage: </b></font><font color="#A347BA"><b>secret-move keyrings</b></font> [<font color="#26A269">-h</font>]

List all available keyrings.

<font color="#12488B"><b>options:</b></font>
  <font color="#26A269"><b>-h</b></font>, <font color="#2AA1B3"><b>--help</b></font>  show this help message and exit
</pre>

<pre>
<font color="#C01C28"><b>user@localhost:~/%</b></font> <font color="#008700"><b>secret-move</b></font> list <font color="#005FFF">--help</font>
<font color="#12488B"><b>usage: </b></font><font color="#A347BA"><b>secret-move list</b></font> [<font color="#26A269">-h</font>] [<font color="#26A269">-s </font><font color="#A2734C">SOURCE</font>] [<font color="#26A269">-v</font>]

List all keys in SOURCE keyring.

<font color="#12488B"><b>options:</b></font>
  <font color="#26A269"><b>-h</b></font>, <font color="#2AA1B3"><b>--help</b></font>           show this help message and exit
  <font color="#26A269"><b>-s</b></font>, <font color="#2AA1B3"><b>--source</b></font> <font color="#A2734C"><b>SOURCE</b></font>  source keyring (default: login)
  <font color="#26A269"><b>-v</b></font>, <font color="#2AA1B3"><b>--verbose</b></font>        show item attributes, repeat a second time to show
					   secrets
</pre>

<pre>
<font color="#C01C28"><b>user@localhost:~/%</b></font> <font color="#008700"><b>secret-move</b></font> copy <font color="#005FFF">--help</font>
<font color="#12488B"><b>usage: </b></font><font color="#A347BA"><b>secret-move copy</b></font> [<font color="#26A269">-h</font>] [<font color="#26A269">-s </font><font color="#A2734C">SOURCE</font>] [<font color="#26A269">-v</font>] [<font color="#26A269">-f</font>] [<font color="#26A269">-i</font>] [<font color="#26A269">-n</font>] [<font color="#26A269">-q</font>] [<font color="#26A269">-r</font>]
						   <font color="#26A269">DEST</font> <font color="#26A269">SEARCH</font>

Copy items matching SEARCH from SOURCE to DEST keyrings.

<font color="#12488B"><b>positional arguments:</b></font>
  <font color="#26A269"><b>DEST</b></font>                  destination keyring
  <font color="#26A269"><b>SEARCH</b></font>                label to search for

<font color="#12488B"><b>options:</b></font>
  <font color="#26A269"><b>-h</b></font>, <font color="#2AA1B3"><b>--help</b></font>            show this help message and exit
  <font color="#26A269"><b>-s</b></font>, <font color="#2AA1B3"><b>--source</b></font> <font color="#A2734C"><b>SOURCE</b></font>   source keyring (default: login)
  <font color="#26A269"><b>-v</b></font>, <font color="#2AA1B3"><b>--verbose</b></font>         show item attributes, repeat a second time to show
						secrets
  <font color="#26A269"><b>-f</b></font>, <font color="#2AA1B3"><b>--force</b></font>           overwrite existing items in destination
  <font color="#26A269"><b>-i</b></font>, <font color="#2AA1B3"><b>--ignore-case</b></font>     case-insensitive matching
  <font color="#26A269"><b>-n</b></font>, <font color="#2AA1B3"><b>--dry-run</b></font>, <font color="#2AA1B3"><b>--no-do</b></font>
						dry-run mode
  <font color="#26A269"><b>-q</b></font>, <font color="#2AA1B3"><b>--quiet</b></font>           suppress all output except errors
  <font color="#26A269"><b>-r</b></font>, <font color="#2AA1B3"><b>--regex</b></font>           enable anchored regex matching
</pre>

# Examples

## List keyrings

``` shell
secret-move keyrings
```

## List keyring contents

| | |
|---------------------------------------------------|------------------------------------|
| List all secrets (in default keyring, _Login_)    | `secret-move list`                 |
| List all secrets with their attributes            | `secret-move list -v`              |
| List all secrets with their attributes and secret | `secret-move list -vv`             |
| List all secrets from keyring _OtherKeyring_      | `secret-move list -s OtherKeyring` |

## Copy keyring contents

| | |
|--------------------------------------------------------------------------------|---------------------------------------------------------|
| Copy secret _Secret1_ from default keyring (_Login_) to _OtherKeyring_         | `secret-move copy OtherKeyring Secret1`                 |
| Copy secret _Secret1_ from alternate keyring _SourceKeyring_ to _OtherKeyring_ | `secret-move copy -s SourceKeyring DestKeyring Secret1` |

## Move keyring contents

| | |
|--------------------------------------------------------------------------------|---------------------------------------------------------|
| Move secret _Secret1_ from default keyring (_Login_) to _OtherKeyring_         | `secret-move move OtherKeyring Secret1`                 |
| Move secret _Secret1_ from alternate keyring _SourceKeyring_ to _OtherKeyring_ | `secret-move move -s SourceKeyring DestKeyring Secret1` |


## Move/copy by regular expression

| | |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Copy all secrets starting with `RDP` from the default keyring (_Login_) to _OtherKeyring_                       | `secret-move move OtherKeyring -r 'RDP.*'`      |
| Copy all secrets containing `rdp` (case insensitive match) from the default keyring (_Login_) to _OtherKeyring_ | `secret-move move OtherKeyring -i -r '.*rdp.*'` |

# Changelog
## Version 0.5

- Created.
