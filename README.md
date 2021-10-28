# Description

Simple utility for quickly generating changelogs, assuming your commits are ordered as they should be. This tool will
simply log all latest commits till last created tag.

# Installation

```shell
python3 -m pip install --user -U pychangelog2
```

# Example

```
➜  pychangelog2 git:(master) ✗ pychangelog2 <path to some repo>
* b1682a0ba253f21a91fabb4d02b9a6d0ec177f7b git: add .idea to .gitignore
* d499ab0f39688e371287ccf3dfc67366e0f70a48 cli: lockdown: add device-name subcommand
* 03f0bee3219fc30aa4f3b378420f5a807eda13b9 requirements: pyusb>=1.2.1
* 7456890e51244e014352a01a9670c35368a68c56 Bugfix: AFC: Pull, push, cd and completion
* d84f3d19f4db5499f0cdcf09bc1b993a96ea1cb0 Replace distutils.LooseVersion with packaging.Version.
```
