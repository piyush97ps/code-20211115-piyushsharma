# Under Implemention
class Member:

    def __init__(self, gender: str, weight_kg: float, height_cm: float) -> None:
        """
            Initalize Member Object
            :params
            gender: gender of member
            weight_kg: weight of member in kg
            height_cm: height pf member in cm
        """
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.bmi: float = self.calculate_bmi()
        self.bmi_catagory: str = self.get_bmi_catagory()
        self.health_risk: str = self.get_health_risk()

    def calculate_bmi(self, height_cm: float = None, weight_kg: float = None) -> float:
        """
            calculate bmi
        """
        if height_cm and weight_kg:
            return weight_kg/(height_cm/100)**2
        return self.weight_kg/(self.height_cm/100)**2

    def get_bmi(self):
        """
            get member bmi
        """
        if self.bmi:
            return self.bmi
        self.bmi = self.calculate_bmi()
        return self.bmi
