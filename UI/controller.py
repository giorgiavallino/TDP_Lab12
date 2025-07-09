import flet as ft

class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # Other things
        self._listYear = []
        self._listCountry = []

    def fillDDYear(self):
        for i in range(2015, 2019):
            self._view.ddyear.options.append(ft.dropdown.Option(str(i)))

    def fillDDCountry(self):
        stati = self._model._countries
        for stato in stati:
            self._view.ddcountry.options.append(ft.dropdown.Option(stato))

    def handle_graph(self, e):
        stato = self._view.ddcountry.value
        if stato is None:
            self._view.create_alert(f"Selezionare uno stato!")
            self._view.update_page()
            return
        anno = self._view.ddyear.value
        if anno is None:
            self._view.create_alert(f"Selezionare un anno!")
            self._view.update_page()
            return
        self._model.buildGraph(stato, anno)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è stato creato correttamente."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}, numero di archi: {self._model.getNumEdges()}"))
        self._view.update_page()


    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
