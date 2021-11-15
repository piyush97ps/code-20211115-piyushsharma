import os
from src.bmi_cal.bmi_calculator import BMICalculator

def test_data_initalize():
    os.environ["JSON_DATA_FILE_PATH"] = "./tests/json/bmi_data.json"

def test_count_by_category():
    bmi = BMICalculator()
    assert bmi.get_count_by_bmi_category("Moderately obese") == 3
    assert bmi.get_count_by_bmi_category("Normal weight") == 2
    assert bmi.get_count_by_bmi_category("Overweight") == 4
    assert bmi.get_count_by_bmi_category("Underweight") == 2
    assert bmi.get_count_by_bmi_category("Severely obese") == 2
    assert bmi.get_count_by_bmi_category("Very Severely obese") == 1
    assert bmi.get_count_by_bmi_category("Invalid") == 0


def test_member_addition():
    bmi = BMICalculator()
    previoue_count = bmi.get_member_count()
    bmi.add_member_in_dataframe(data={"Gender": "Male", "HeightCm": 173, "WeightKg": 72})
    assert bmi.get_member_count() == previoue_count + 1
