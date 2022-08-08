import logging

import pytest
from cattr.preconf.json import JsonConverter

from dialysis_data.data import TreatmentLog, make_json_converter


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def json_converter() -> JsonConverter:
    return make_json_converter()


@pytest.fixture(scope="session")
def treatment_logs_json(json_converter: JsonConverter, treatment_logs: list[TreatmentLog]) -> str:
    return json_converter.dumps(treatment_logs)


def test_serialize_treatement_logs(treatment_logs_json: str) -> None:
    assert treatment_logs_json is not None
    assert treatment_logs_json != ""
    assert treatment_logs_json.count("treatment_date") == 5


def test_load_treatment_logs(
    json_converter: JsonConverter, treatment_logs_json: str, treatment_logs: list[TreatmentLog]
) -> None:
    treatment_logs_deserialized = json_converter.loads(treatment_logs_json, list[TreatmentLog])

    LOGGER.info(f"{treatment_logs_deserialized}")

    assert treatment_logs_deserialized is not None
    assert len(treatment_logs_deserialized) == 5
    assert treatment_logs_deserialized == treatment_logs

    # LOGGER.info(
    #     f"treatment_logs: {id(treatment_logs)}, "
    #     f"treatment_logs_deserialized: {id(treatment_logs_deserialized)}"
    # )

    # for x, y in zip(treatment_logs, treatment_logs_deserialized):
    #     LOGGER.info(f"{x.treatment_date}: x: {id(x)}, y: {id(y)}")
