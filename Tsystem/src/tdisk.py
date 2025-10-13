from textual.widgets import Static, Label
import subprocess

class Tdisk(Static):

    #trigger get disk after screen is active
    def on_mount(self):
        self.get_disk()

    #function to get disk info
    def get_disk(self):
        process = subprocess.run('df -h', shell=True, text=True, capture_output=True)
        self.query_one("#disklabel", Label).update(process.stdout)

    def compose(self):
        yield Label(id="disklabel")
