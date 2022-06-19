from services.datastore_service import DataStoreService


class DataStoreController:
    def __init__(self):
        pass

    @staticmethod
    def get_stock_list():
        return DataStoreService.get_stock_list()

    @staticmethod
    def populate():
        DataStoreService.populate()
