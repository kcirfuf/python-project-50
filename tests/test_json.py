import json
from pathlib import Path

from gendiff import generate_diff


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "test_data"

FILE1 = DATA_DIR / "flat_json1.json"
FILE2 = DATA_DIR / "flat_json2.json"
EXPECTED_VALUE = DATA_DIR / "flat_json_expected_value"


def load_json(path: Path):
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def load_expected(path: Path):
    return path.read_text(encoding="utf-8").rstrip()


def test_generate_diff():
    file_content1 = load_json(FILE1)
    file_content2 = load_json(FILE2)
    assert_value = load_expected(EXPECTED_VALUE)

    assert generate_diff(file_content1, file_content2) == assert_value


def test_generate_diff_empty_dicts():
    assert generate_diff({}, {}) == "{\n}"
