from typer.testing import CliRunner

from dialysis_data import __version__
from dialysis_data.main import app


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_dialysis_data_cli_start() -> None:
    runner = CliRunner()
    result = runner.invoke(app, "start")
    assert result.exit_code == 0
