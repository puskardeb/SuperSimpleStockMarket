from services.datastore_service import DataStoreService


class DataStoreController:

    @staticmethod
    def get_stock_list():
        return DataStoreService.get_stock_list()

    @staticmethod
    def populate():
        try:
            DataStoreService.populate_from_csv()
        except FileNotFoundError:
            DataStoreService.populate_from_defaults()
