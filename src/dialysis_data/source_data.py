from datetime import date, timedelta
from decimal import Decimal

from dialysis_data.data import (
    BloodPressure,
    HeartRate,
    MillimetersOfMercury,
    SolutionStrength,
    Temperature,
    TreatmentLog,
    Volume,
    Weight,
)


def treatment_logs() -> list[TreatmentLog]:
    return [
        TreatmentLog(
            treatment_date=date(2022, 7, 27),
            weight=Weight(Decimal("53.8")),
            blood_pressure=BloodPressure(MillimetersOfMercury(121), MillimetersOfMercury(82)),
            heart_rate=HeartRate(84),
            temperature=Temperature(Decimal("98.6")),
            solution=SolutionStrength.YELLOW,
            initial_drain=Volume(6),
            ultra_filtration=Volume(147),
            average_dwell=timedelta(hours=2),
        ),
        TreatmentLog(
            treatment_date=date(2022, 7, 28),
            weight=Weight(Decimal("53.8")),
            blood_pressure=BloodPressure(MillimetersOfMercury(109), MillimetersOfMercury(75)),
            heart_rate=HeartRate(97),
            temperature=Temperature(Decimal("96.1")),
            solution=SolutionStrength.YELLOW,
            initial_drain=Volume(2),
            ultra_filtration=Volume(-21),
            average_dwell=timedelta(hours=1, minutes=49),
        ),
        TreatmentLog(
            treatment_date=date(2022, 7, 29),
            weight=Weight(Decimal("54.8")),
            blood_pressure=BloodPressure(MillimetersOfMercury(120), MillimetersOfMercury(82)),
            heart_rate=HeartRate(78),
            temperature=Temperature(Decimal("96.8")),
            solution=SolutionStrength.YELLOW,
            initial_drain=Volume(1),
            ultra_filtration=Volume(73),
            average_dwell=timedelta(hours=2, minutes=2),
        ),
        TreatmentLog(
            treatment_date=date(2022, 7, 30),
            weight=Weight(Decimal("55.8")),
            blood_pressure=BloodPressure(MillimetersOfMercury(113), MillimetersOfMercury(80)),
            heart_rate=HeartRate(98),
            temperature=Temperature(Decimal("97.0")),
            solution=SolutionStrength.YELLOW,
            initial_drain=Volume(3),
            ultra_filtration=Volume(32),
            average_dwell=timedelta(hours=2, minutes=8),
        ),
        TreatmentLog(
            treatment_date=date(2022, 7, 31),
            weight=Weight(Decimal("54.8")),
            blood_pressure=BloodPressure(MillimetersOfMercury(122), MillimetersOfMercury(81)),
            heart_rate=HeartRate(90),
            temperature=Temperature(Decimal("98.4")),
            solution=SolutionStrength.YELLOW,
            initial_drain=Volume(5),
            ultra_filtration=Volume(44),
            average_dwell=timedelta(hours=1, minutes=59),
        ),
    ]
