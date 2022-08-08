from pathlib import Path

import typer
from attr import asdict, define, fields_dict
from cattr.preconf.json import JsonConverter
from rich import box
from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table

from dialysis_data import source_data
from dialysis_data.data import TreatmentLog, make_json_converter


APP_NAME = "dialysis-data"

app: typer.Typer = typer.Typer(name=APP_NAME)


@define(frozen=True, slots=True)
class TreatmentHistory:
    treatment_logs: list[TreatmentLog]

    def debug(self) -> None:
        row = self.treatment_logs[0]

        for key, value in asdict(row, recurse=True).items():
            print(f"Key '{key}': {value} is {type(value)})")

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        table = Table(title="Treatment Log", box=box.SIMPLE)

        for field in fields_dict(TreatmentLog).keys():
            table.add_column(field.title().replace("_", " "), justify="right")

        for row in sorted(self.treatment_logs):
            table.add_row(
                str(row.treatment_date),
                str(row.weight),
                str(row.blood_pressure),
                str(row.heart_rate),
                str(row.temperature),
                str(row.solution),
                str(row.initial_drain),
                str(row.ultra_filtration),
                str(row.average_dwell),
            )

        yield table


def data_file_location() -> Path:
    app_data_dir = Path(typer.get_app_dir(APP_NAME))

    if not app_data_dir.exists():
        app_data_dir.mkdir(parents=True)

    return app_data_dir / "data.json"


@app.command()
def start() -> None:
    """
    Start the dialysis application.
    """
    json_converter: JsonConverter = make_json_converter()
    data_file: Path = data_file_location()
    console: Console = Console()

    if not data_file.exists():
        console.print("Data file not found.")
        raise typer.Exit(code=1)

    with data_file.open() as f:
        treatment_logs: list[TreatmentLog] = json_converter.loads(f.read(), list[TreatmentLog])

    treatment_history: TreatmentHistory = TreatmentHistory(treatment_logs)

    console.print(treatment_history)


@app.command()
def save() -> None:
    """
    Saves the current hard-coded data to a file.
    """
    console: Console = Console()
    data_file: Path = data_file_location()
    json_converter: JsonConverter = make_json_converter()
    treatment_logs: list[TreatmentLog] = source_data.treatment_logs()

    with data_file.open("w") as f:
        f.write(json_converter.dumps(treatment_logs))

    console.print("Successfully wrote source data.")
