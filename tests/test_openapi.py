import json
from pathlib import Path
from openapi_spec_validator import validate_spec

def test_openapi_valid():
    spec_path = Path(__file__).resolve().parents[1] / "basics" / "openapi.json"
    with spec_path.open() as f:
        spec = json.load(f)
    # validate_spec will raise an exception if the spec is invalid
    validate_spec(spec)
