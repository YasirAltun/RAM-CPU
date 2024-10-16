import rumps
import psutil

class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("Loading...", quit_button=None)
        self.menu = ["Quit"]
        self.timer = rumps.Timer(self.update_status, 0.01)
        self.timer.start()

    def update_status(self, _):
        ram_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent(interval=1)
        self.title = f"RAM: {ram_usage}% CPU: {cpu_usage}%"

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()

if __name__ == "__main__":
    app = MenuBarApp()
    app.run()
