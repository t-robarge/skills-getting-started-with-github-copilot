import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Ensure each test runs with a clean in-memory activity dataset."""
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
