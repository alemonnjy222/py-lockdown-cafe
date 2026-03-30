from datetime import datetime, date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineError,
)


class Cafe:
    def __init__(self, name: Cafe):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")
        
        expiration_date = visitor["vaccine"].get("expiration_date")

        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
            
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")
            
        return f"Welcome to {self.name}"
