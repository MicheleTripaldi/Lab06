from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def getAnno(self):
        return DAO.getAllanno()
    def getBrand(self):
        return DAO.getAllBrand()
    def getRetailer(self):
        return DAO.getAllRetailer()
    def FiltroTop(self,anno, brand, retailer):
        return DAO.FiltroTop(anno,brand,retailer)