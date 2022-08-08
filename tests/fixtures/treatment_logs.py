import pytest

from dialysis_data import source_data
from dialysis_data.data import TreatmentLog


@pytest.fixture(scope="session")
def treatment_logs() -> list[TreatmentLog]:
    return source_data.treatment_logs()
