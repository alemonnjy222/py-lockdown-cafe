from datetime import datetime, date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str):
        self.name = name
        
     if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

        if expiration_date < date.today():
            raise OutdatedVaccineError("Vaccine is outdated")
