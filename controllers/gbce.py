from services.gbce_service import GBCEService
from errors.error import InvalidValueError


class GBCEController:
    @staticmethod
    def process_gbce_opt():
        ret_str, value = GBCEController.calculate()
        if ret_str == "success":
            print("The GBCE All Share Index is {}.".format(value))
        else:
            print("Unable to calculate GBCE All Share Index!")

    @staticmethod
    def calculate():
        try:
            return "success", GBCEService.calculate()
        except InvalidValueError as IVE:
            print(IVE)
            return "fail", None
        except Exception as ex:
            print(ex)
            return "fail", None
