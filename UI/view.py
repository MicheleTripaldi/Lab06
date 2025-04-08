import flet as ft

from database.DAO import DAO


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._dd_anno = None
        self._dd_brand = None
        self._dd_retailer = None
        self._btn_TopVendite = None
        self._btn_AnalizzaVendite = None
        self.txt_result = None


    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._dd_anno= ft.Dropdown(label="anno",options= [ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddAnno()
        self._dd_brand = ft.Dropdown(label="brand",options= [ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddBrand()
        self._dd_retailer = ft.Dropdown(label="retailer", options= [ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddRetailer()
        self._btn_TopVendite = ft.ElevatedButton(text="Top Vendite", on_click= self._controller.handleTopVendite)
        self._btn_AnalizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_analizza)
        self._page.controls.append(self._title)

        #ROW with some controls
        row1= ft.Row([self._dd_anno, self._dd_brand, self._dd_retailer])
        row2 = ft.Row([self._btn_TopVendite, self._btn_AnalizzaVendite], alignment= ft.MainAxisAlignment.CENTER)

        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )



        # List View where the reply is printed
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
