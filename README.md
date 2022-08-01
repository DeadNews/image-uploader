# py-image-uploader

> Upload images via APIs

[![PyPI version](https://img.shields.io/pypi/v/py-image-uploader)](https://pypi.org/project/py-image-uploader)
[![CI/CD](https://github.com/DeadNews/py-image-uploader/actions/workflows/python-app.yml/badge.svg)](https://github.com/DeadNews/py-image-uploader/actions/workflows/python-app.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/DeadNews/py-image-uploader/main.svg)](https://results.pre-commit.ci/latest/github/DeadNews/py-image-uploader/main)
[![codecov](https://codecov.io/gh/DeadNews/py-image-uploader/branch/main/graph/badge.svg?token=OCZDZIYPMC)](https://codecov.io/gh/DeadNews/py-image-uploader)

## Hostings

| host                                  | key required | return example                                    |
| :------------------------------------ | :----------: | :------------------------------------------------ |
| [catbox](https://catbox.moe/)         |      -       | https://files.catbox.moe/$id                      |
| [fastpic](https://fastpic.org/)       |      -       | https://i120.fastpic.org/big/2022/0730/d9/$id.png |
| [filecoffee](https://file.coffee/)    |      -       | https://file.coffee/u/$id.png                     |
| [freeimage](https://freeimage.host/)  |      -       | https://iili.io/$id.png                           |
| [geekpic](https://geekpic.net/)       |      -       | https://s01.geekpic.net/$id.png                   |
| [gyazo](https://gyazo.com/)           |      +       | https://i.gyazo.com/$id.png                       |
| [imageban](https://imageban.ru/)      |      +       | https://i2.imageban.ru/out/2022/07/30/$id.png     |
| [imgbb](https://imgbb.com/)           |      +       | https://i.ibb.co/$id/image.png                    |
| [imgchest](https://imgchest.com/)     |      +       | https://cdn.imgchest.com/files/$id.png            |
| [imgur](https://imgur.com/)           |      +       | https://i.imgur.com/$id.png                       |
| [pictshare](https://pictshare.net/)   |      -       | https://pictshare.net/$id.png                     |
| [pixeldrain](https://pixeldrain.com/) |      -       | https://pixeldrain.com/api/file/$id               |
| [pixhost](https://pixhost.to/)        |      -       | https://img75.pixhost.to/images/69/$id_img.png    |
| [ptpimg](https://ptpimg.me/)          |      +       | https://ptpimg.me/$id.png                         |
| [up2sha](https://up2sha.re/)          |      +       | https://up2sha.re/media/raw/$id.png               |
| [uploadcare](https://uploadcare.com/) |      +       | https://ucarecdn.com/$id/img.png                  |

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
  -h, --hosting [catbox|fastpic|filecoffee|freeimage|geekpic|gyazo|imageban|imgbb|imgchest|imgur|pictshare|pixeldrain|pixhost|ptpimg|up2sha|uploadcare]
                                  [default: geekpic]
  -b, --bbcode                    Add bbcode tags
  -t, --thumbnail                 Add thumbnails and bbcode tags
  --version                       Show the version and exit.
  --help                          Show this message and exit.
```

## Env variables

```ini
CAPTION_FONT= # default arial.ttf

BEEIMG_KEY=
FREEIMAGE_KEY=
GYAZO_TOKEN=
IMAGEBAN_TOKEN=
IMGBB_KEY=
IMGCHEST_KEY=
IMGUR_CLIENT_ID=
PTPIMG_KEY=
UP2SHA_KEY=
UPLOADCARE_KEY=
```

You can set these in environment variables, or in `.env` file:

- Unix: `~/.config/py-image-uploader/.env`
- MacOS: `~/Library/Application Support/py-image-uploader/.env`
- Windows: `C:\Users\<user>\AppData\Roaming\py-image-uploader\.env`
