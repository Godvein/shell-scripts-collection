from re import A
from textual.app import App
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label
from tprocess import Tprocess
from tdisk import Tdisk
from textual import on

class Process(Screen):
    sort = "default"

    BINDINGS = {
            ("d", "go_disk", "view disk info"),
            ("m", "memsort", "memory sort"),
            ("c", "cpusort", "cpu sort")
            }

    def compose(self):
        yield Header()
        yield Footer()
        yield Label("processes")
        yield Button("Memory sort", id="memsort", classes="sort-button")
        yield Button("CPU sort", id="cpusort", classes="sort-button")
        yield Tprocess(id="tprocess", classes="static-widget")

    @on(Button.Pressed, "#memsort")
    def action_memsort(self):
        self.sort = "mem"
 
    @on(Button.Pressed, "#cpusort")
    def action_cpusort(self):
        self.sort = "cpu"
               
    #on mount set interval to trigger function
    def on_mount(self):
        self.set_interval(2, self.refresh_process)

    #function to update process info based on sort
    def refresh_process(self):
        if self.sort == "default":
            self.query_one("#tprocess", Tprocess).update_info()
        elif self.sort == "mem":
            self.query_one("#tprocess", Tprocess).sort_mem()
        elif self.sort == "cpu":
            self.query_one("#tprocess", Tprocess).sort_cpu()

    #screen management
    def action_go_disk(self):
        self.app.push_screen(Disk())

class Disk(Screen):
    BINDINGS = {
            ("p", "go_process", "view process info")
            }
    def compose(self):
        yield Header()
        yield Footer()
        yield Label("disk")
        yield Tdisk(id="tdisk", classes="static-widget")
   
    #trigger disk info function after widgets are loaded
    def on_ready(self):
       self.query_one("#tdisk", Tdisk).get_disk()

    #screen management
    def action_go_process(self):
        self.app.pop_screen()

class Tsystem(App):
    CSS_PATH = "main.css"

    def on_mount(self):
        self.push_screen(Process())

if __name__ == "__main__":
    Tsystem().run()
