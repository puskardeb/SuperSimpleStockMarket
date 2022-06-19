from services.gbce_service import GBCEService

class GBCEController:
    @staticmethod
    def calculate():
        return GBCEService.calculate()