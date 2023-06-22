#!/usr/bin/env python
import pytest
from click.testing import CliRunner
from images_upload_cli.__main__ import cli
from images_upload_cli.upload import HOSTINGS


@pytest.fixture()
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "args",
    [
        pytest.param(["--help"], id="help"),
        pytest.param(
            ["tests/resources/pic.png", "-C", "-h", "uploadcare", "--thumbnail", "--notify"],
            id="uploadcare,thumbnail",
        ),
    ],
)
def test_cli(runner: CliRunner, args: list[str]):
    assert runner.invoke(cli=cli, args=args).exit_code == 0


@pytest.mark.key_required()
@pytest.mark.parametrize(
    "args",
    [
        pytest.param(["tests/resources/pic.png", "-C", "-h", hosting], id=hosting)
        for hosting in HOSTINGS
    ],
)
def test_cli_all(runner: CliRunner, args: list[str]):
    assert runner.invoke(cli=cli, args=args).exit_code == 0
