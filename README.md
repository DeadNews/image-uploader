# py-image-uploader

> Upload images via APIs

[![PyPI version](https://img.shields.io/pypi/v/py-image-uploader)](https://pypi.org/project/py-image-uploader)
[![CI/CD](https://github.com/DeadNews/py-image-uploader/actions/workflows/python-app.yml/badge.svg)](https://github.com/DeadNews/py-image-uploader/actions/workflows/python-app.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/DeadNews/py-image-uploader/main.svg)](https://results.pre-commit.ci/latest/github/DeadNews/py-image-uploader/main)
[![codecov](https://codecov.io/gh/DeadNews/py-image-uploader/branch/main/graph/badge.svg?token=OCZDZIYPMC)](https://codecov.io/gh/DeadNews/py-image-uploader)

## Hostings

- Works out of the box:

  - [fastpic](https://fastpic.org/)
  - [file_coffee](https://file.coffee/)
  - [geekpic](https://geekpic.net/)
  - [pixeldrain](https://pixeldrain.com/)
  - [pixhost](https://pixhost.to/)

- Key required:

  - [freeimage](https://freeimage.host/)
  - [gyazo](https://gyazo.com/)
  - [imageban](https://imageban.ru/)
  - [imageshack](https://imageshack.us/)
  - [imgbb](https://imgbb.com/)
  - [imgur](https://imgur.com/)
  - [up2sha](https://up2sha.re/)
  - [uploadcare](https://uploadcare.com/)

## Installation

```sh
pip install py-image-uploader
```

or

```sh
pipx install py-image-uploader
```

## Usage

```sh
Usage: py-image-uploader [OPTIONS] [IMAGES]...

  Upload images via APIs. The result will be copied to the clipboard.

Options:
  -h, --hosting [fastpic|file_coffee|freeimage|geekpic|gyazo|imageban|imageshack|imgbb|imgur|pixhost|up2sha|uploadcare]
                                  [default: geekpic]
  -b, --bbcode                    Add bbcode tags
  -t, --thumbnail                 Add thumbnails and bbcode tags
  --version                       Show the version and exit.
  --help                          Show this message and exit.
```

## Env variables

```ini
CAPTION_FONT= # default arial.ttf

FREEIMAGE_KEY=
GYAZO_TOKEN=
IMAGEBAN_TOKEN=
IMAGESHACK_KEY=
IMGBB_KEY=
IMGUR_CLIENT_ID=
UP2SHA_KEY=
UPLOADCARE_KEY=
```

You can set these in environment variables, or in `.env` file:

- Unix: `~/.config/py-image-uploader/.env`
- MacOS: `~/Library/Application Support/py-image-uploader/.env`
- Windows: `C:\Users\<user>\AppData\Roaming\py-image-uploader\.env`
