from textual.widgets import Label, Static
import subprocess

class Tprocess(Static):

    #function to get process info
    def update_info(self):
        process = subprocess.run('ps -aux', text=True, capture_output=True, shell=True)
        output = process.stdout.splitlines()[:10]
        self.query_one("#processlabel", Label).update("\n".join(output))
       
    #function to sort based on memory
    def sort_mem(self):
        process = subprocess.run('ps -aux --sort=-%mem', text=True, capture_output=True, shell=True)
        output = process.stdout.splitlines()[:10]
        self.query_one("#processlabel", Label).update("\n".join(output))

    #function to sort based on memory
    def sort_cpu(self):
        process = subprocess.run('ps -aux --sort=-%cpu', text=True, capture_output=True, shell=True)
        output = process.stdout.splitlines()[:10]
        self.query_one("#processlabel", Label).update("\n".join(output))
       
    def compose(self):
        yield Label(id="processlabel")

