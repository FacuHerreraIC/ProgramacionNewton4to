class MobilePhone:
    def __init__(self,manufacturer: str, screen_size: float, num_cores: int, apps: list,status: bool):
        self.manpufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = apps
        self.status = status
    def power_on(self):
        self.status = True
        print('MP is currently on')
    def power_off(self):
        self.status = False
        print('MP is currently off')
    def install_app(self, app):
        if app not in self.apps:
            self.apps.append(app)
            print(f"{app} Sucessffully installed!")
        else:
            print(f"Careful, {app} is already installed")
    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
            print(f"{app} Sucessffully uninstalled!")
        else:
            print(f"Careful, {app} is not installed")

S21FE = MobilePhone(
    manufacturer="Samsung",
    screen_size=7.2,
    num_cores="8",
    apps=["Wsp","Instagram", "Twitter", "Maps"], 
    status=False)

S21FE.power_on()
S21FE.install_app("Maps")
S21FE.uninstall_app("Facebook")
S21FE.power_off()
print(S21FE.status)
