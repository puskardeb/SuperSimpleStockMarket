from services.datastore_service import DataStoreService

class DataStoreController:
    def __init__(self):
        pass

    @staticmethod
    def get_stock_list():
        return DataStoreService.stock_list

    @staticmethod
    def populate():
        # all error handling to be done here
        # service handles the core functionality
        # and is not concerned with error,
        # if any error is faced by service, it will
        # propagate the error to the outer layer i.e.
        # the service and it needs to handle the error

        DataStoreService.populate()