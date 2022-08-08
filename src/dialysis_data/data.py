from datetime import date, timedelta
from decimal import Decimal
from enum import Enum
from typing import Any, Type

from attrs import define
from cattr.preconf.json import JsonConverter, make_converter
from cattrs.converters import T


class SolutionStrength(Enum):
    YELLOW = "Yellow"
    GREEN = "Green"

    def __str__(self) -> str:
        return self.value


@define(slots=True, frozen=True)
class MillimetersOfMercury:
    value: int

    def __str__(self) -> str:
        return f"{self.value} mmHg"


@define(slots=True, frozen=True)
class BloodPressure:
    systolic: MillimetersOfMercury
    diastolic: MillimetersOfMercury

    def __str__(self) -> str:
        return f"{self.systolic} / {self.diastolic}"


@define(slots=True, frozen=True)
class HeartRate:
    value: int

    def __str__(self) -> str:
        return f"{self.value} bpm"


@define(slots=True, frozen=True)
class Weight:
    value: Decimal

    def __str__(self) -> str:
        return f"{self.value} kg"


@define(slots=True, frozen=True)
class Temperature:
    value: Decimal

    def __str__(self) -> str:
        return f"{self.value} °F"


@define(slots=True, frozen=True)
class Volume:
    value: int

    def __str__(self) -> str:
        return f"{self.value} mL"


@define(slots=True, frozen=True, kw_only=True, order=True)
class TreatmentLog:
    treatment_date: date
    weight: Weight
    blood_pressure: BloodPressure
    heart_rate: HeartRate
    temperature: Temperature
    solution: SolutionStrength
    initial_drain: Volume
    ultra_filtration: Volume
    average_dwell: timedelta


def make_json_converter() -> JsonConverter:
    converter = make_converter()

    def structure_date(s: Any, _type: Type[T]) -> Any:
        return date.fromisoformat(s)

    def unstructure_date(d: date) -> str:
        return d.isoformat()

    converter.register_structure_hook(date, structure_date)
    converter.register_unstructure_hook(date, unstructure_date)

    def structure_timedelta(s: Any, _type: Type[T]) -> Any:
        return timedelta(seconds=float(s))

    def unstructure_timedelta(t: timedelta) -> Any:
        return t.total_seconds()

    converter.register_structure_hook(timedelta, structure_timedelta)
    converter.register_unstructure_hook(timedelta, unstructure_timedelta)

    def structure_decimal(s: Any, _type: Type[T]) -> Any:
        return Decimal(s)

    def unstructure_decimal(d: Decimal) -> Any:
        return str(d)

    converter.register_structure_hook(Decimal, structure_decimal)
    converter.register_unstructure_hook(Decimal, unstructure_decimal)

    return converter
