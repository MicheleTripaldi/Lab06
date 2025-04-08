import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def fillddAnno(self):
        for anno in self._model.getAnno():
            self._view._dd_anno.options.append(ft.dropdown.Option(anno))


    def fillddBrand(self):
        for brand in self._model.getBrand():
            self._view._dd_brand.options.append(ft.dropdown.Option(brand))

    def fillddRetailer(self):
        for retailer in self._model.getRetailer():
            self._view._dd_retailer.options.append(ft.dropdown.Option(key= retailer.Retailer_code,text=retailer.Retailer_name,data=retailer,on_click=self.read_retailer)
                                                   )

    def read_retailer(self,e):
        self._retailer = e.control.data


    # funzione bottoni
    def handleTopVendite(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._retailer # potrebbe essere sbagliato

        if anno is None or anno == "":
            self._view.create_alert("Inserisci anno")
            return
        if brand is None or brand == "":
            self._view.create_alert("Inserisci brand")
            return
        if retailer is None or retailer == "":
            self._view.create_alert("Inserisci retailer")
            return

        listaTopVendite = []
        for ret in self._model.FiltroTop(anno, brand, retailer.Retailer_code):
            listaTopVendite.append(ret)

        sorted_listaTop = sorted(listaTopVendite, key=lambda s: s.Quantity * s.Unit_sale_price, reverse=True )

        for ret in sorted_listaTop[0:5]:
            self._view.txt_result.controls.append(ft.Text(
                f"Data: {ret.Date}; Ricavo: {ret.Quantity * ret.Unit_sale_price}; Retailer: {ret.Retailer_code}; Product: {ret.Product_number}"))
        self._view.update_page()

    def handle_analizza(self, e):
        anno = self._view._dd_anno.value
        brand = self._view._dd_brand.value
        retailer = self._retailer

        if anno is None or anno == "":
            self._view.create_alert("Inserire anno")
            return
        if brand is None or brand == "":
            self._view.create_alert("Inserire brand")
            return
        if retailer is None or retailer == "":
            self._view.create_alert("Inserire retailer")
            return

        listaAnalize = []
        for ret in self._model.FiltroTop(anno, brand, retailer.Retailer_code):
            listaAnalize.append(ret)

        contaAffari = 0
        numVendite = 0
        numRetailers = 0
        numProdotti = 0
        setRetailer = set()
        setProdotti = set()
        for ret in listaAnalize:
            contaAffari=contaAffari+(ret.Quantity*ret.Unit_sale_price)
            numVendite=numVendite+1
            if ret.Retailer_code not in setRetailer:
                numRetailers = numRetailers+1
                setRetailer.add(ret.Retailer_code)
            if ret.Product_number not in setProdotti:
                numProdotti = numProdotti+1
                setProdotti.add(ret.Product_number)






        self._view.txt_result.controls.append(ft.Text(
            f"Statistiche vendite"+
            f"Giro d'affari: {contaAffari}\n"+
            f"Numero di vendite: {numVendite}\n"+
            f"Numero dei retailers coinvolti : {numRetailers}\n"+
            f"Numero di prodotti coinvolti: {numProdotti}\n"))

        self._view.update_page()

