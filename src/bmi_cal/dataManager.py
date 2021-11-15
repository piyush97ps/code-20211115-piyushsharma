import json
import copy
import os
from typing import Dict, List, Any

from src.bmi_cal.BMI_TABLE_DATA import data

# os.environ["JSON_DATA_FILE_PATH"] = "./bmi_data.json"


class DataLoader:

    def __init__(self, JSON_DATA_FILE_PATH: str = None, data: Any = None):
        """
            Initating the Data Loader with data

            :params
            JSON_DATA_FILE_PATH: json data file path in string
            data: data to be manager or used

            NOTE: if both 'data' and 'JSON_DATA_FILE_PATH' are give
                  then 'data' will assigned directly to __data
        """
        if data:
            self.__data = data
        elif JSON_DATA_FILE_PATH:
            file_obj = open(JSON_DATA_FILE_PATH)
            self.__data = json.load(file_obj)
        elif "JSON_DATA_FILE_PATH" in os.environ:
            file_obj = open(os.environ.get("JSON_DATA_FILE_PATH"))
            self.__data = json.load(file_obj)
        else:
            self.__data = None

    def get_data_list(self) -> List:
        """
            get the list of bmi data
            return: DeepCopy of the data if its type list
                    else it empty list
        """
        if isinstance(self.__data, list):
            return copy.deepcopy(self.__data)

        return []

    def get_json_data(self) -> Any:
        """
            get json data
            return: DeepCopy of the data
        """
        return copy.deepcopy(self.__data)

    def update_data(self, data: str) -> Any:
        """
            Update data
            return: DeepCopy of the data
        """
        self.__data = data
        return copy.deepcopy(self.__data)


class BMIEvaluator:

    @staticmethod
    def get_bmi_category_and_health_risk(bmi: float) -> Dict:
        """
            return bmi category and health risk for the given bmi
        """
        try:
            return next(filter(lambda x: x.get("BMIRange", -1) >= bmi, data))
        except StopIteration:
            return data[-1]

    @staticmethod
    def calculate_bmi(weight_kg: float, height_cm: int) -> float:
        """
            calculate Body Mass Index of given weight (kg) and height (cm)
            BMI formula: BMI(kg/m**2) = mass(kg) / height(m)**2

            :params
            weight_kg: weight in kg for BMI
            height_cm: height in cm for BMI

            return: BMI values
        """
        height_meters = height_cm/100
        return round(weight_kg / (height_meters)**2, 1)

    @staticmethod
    def evaluate_bmi_category(bmi: float) -> str:
        """
            Evaluate BMI Category for given bmi
            :params
            bmi: bmi value for which category to be determine

            return: BMI Category
        """
        try:
            return next(filter(lambda x: x.get("BMIRange", -1) >= bmi, data)).get("BMICategory")
        except StopIteration:
            return data[-1].get("BMICategory", "NA")

    @staticmethod
    def evaluate_bmi_health_risk(bmi: float) -> str:
        """
             Evaluate BMI Health Risk for given bmi
            :params
            bmi: bmi value for which health risk to be determine

            return: BMI Health Risk
        """
        try:
            return next(filter(lambda x: x.get("BMIRange", -1) >= bmi, data)).get("HealthRisk")
        except StopIteration:
            return data[-1].get("HealthRisk", "Na")
