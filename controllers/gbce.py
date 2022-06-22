from services.gbce_service import GBCEService
from errors.error import InvalidValueError


class GBCEController:
    @staticmethod
    def calculate():
        try:
            return "success", GBCEService.calculate()
        except InvalidValueError as IVE:
            print(IVE)
            return "fail", None
