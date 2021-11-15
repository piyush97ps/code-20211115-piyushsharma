from typing import Any, List
import pandas as pd
import logging

from src.bmi_cal.dataManager import DataLoader, BMIEvaluator


class BMICalculator:

    def __init__(self, JSON_DATA_FILE_PATH: str = None, data: Any = None):
        if data:
            self.dataLoader = DataLoader(data=data)
        elif JSON_DATA_FILE_PATH:
            self.dataLoader = DataLoader(
                JSON_DATA_FILE_PATH=JSON_DATA_FILE_PATH)
        else:
            self.dataLoader = DataLoader()
        self.bmi_df = self.load_dataframe_with_bmi(
            self.dataLoader.get_data_list())

    def load_dataframe_with_bmi(self, data: List = None) -> pd.DataFrame:
        """
            loading data in pandas dataframe
            :params
            data: list of dictinary object to be loaded in pandas data frame
            return: Pandas DataFrame with give data
        """
        if isinstance(data, list):
            for i in range(len(data)):
                bmi = BMIEvaluator.calculate_bmi(
                    weight_kg=data[i]["WeightKg"],
                    height_cm=data[i]["HeightCm"]
                )
                bmi_data = BMIEvaluator.get_bmi_category_and_health_risk(
                    bmi=bmi)
                bmi_category = bmi_data.get("BMICategory", -1)
                health_risk = bmi_data.get("HealthRisk", -1)
                data[i].update(
                    {
                        "BMI": bmi,
                        "BMICategory": bmi_category,
                        "HealthRisk": health_risk
                    })
            return pd.DataFrame(data=data)

        logging.info(
            "Empty given data is not of type list,\
            Initailting DataFrame with empty list")
        return pd.DataFrame([])

    def get_dataFrame(self) -> pd.DataFrame:
        return self.bmi_df

    def get_dataLoader(self) -> DataLoader:
        """
            Return DataLoader object initalize with data
        """
        return self.dataLoader

    def get_count_by_bmi_category(self, category: str) -> int:
        """
            Get Count by the bmi catagory
        """
        if self.bmi_df is not None:
            return len(self.bmi_df[self.bmi_df["BMICategory"] == category])
        return -1

    def add_member_in_dataframe(self, data: dict) -> pd.DataFrame:
        """
            add member to the dataFrame
            :params
            data: data dict containing the member required
                  info like
                  {
                    "Gender": "Male",
                    "HeightCm": 171,
                    "WeightKg": 96
                }
            return: add member in dataFrame
        """
        bmi = BMIEvaluator.calculate_bmi(
            weight_kg=data["WeightKg"],
            height_cm=data["HeightCm"]
        )
        bmi_data = BMIEvaluator.get_bmi_category_and_health_risk(
            bmi=bmi)
        bmi_category = bmi_data.get("BMICategory", -1)
        health_risk = bmi_data.get("HealthRisk", -1)

        data.update({
                "BMI": bmi,
                "BMICategory": bmi_category,
                "HealthRisk": health_risk
            })

        self.bmi_df = pd.concat([self.bmi_df,
                                pd.DataFrame(data=[data])],
                                ignore_index=True)

        self.bmi_df.reset_index()
        return self.bmi_df

    def get_member_by_category(self, category: str) -> List:
        if self.bmi_df is not None:
            return (self.bmi_df[self.bmi_df["BMICategory"] == category]
                    ).to_dict('records')
        return -1

    def get_member_count(self) -> int:
        """
            number of members in dataFrame
        """
        return len(self.bmi_df)
