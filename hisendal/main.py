from os.path import abspath, basename, dirname, exists, getsize, join
from re import search
from urllib.request import Request, urlopen

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.keygen import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.app import MDApp

from services.netsense import from_address

KV = """
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        padding: [16, 16, 16, 16]
        spacing: 16
        TextInput:
            id: txt_inpt
            text: ""
            size_hint: 1.0, 0.2
        MDBoxLayout:
            orientation: "horizontal"
            spacing: 16
            size_hint: 1.0, 0.8
            MDRectangleFlatButton:
                on_release: app.update()
                size_hint: 1.0, 1.0
                text: "UPDATE"
                disabled: app.loading
"""

CACHE_FOLDER_NAME = abspath(join(dirname(__file__), "cache"))

class MainApp(MDApp):
    loading = BooleanProperty(False)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.initilize_global_vars()
        return Builder.load_string(KV)

    def update(self):
        self.loading = True
        website = "arm64-v8a"
        website = f"https://repo.kodinerds.net/index.php?action=list&scope=cat&item=Binary%20({website})"
        pattern = 'download=(.*Matrix.apk)(?=")'
        content = urlopen(Request(website, headers={"user-agent": "mozilla/5.0"})).read().decode()
        address = search(pattern, content).group(1)
        address = f"https://repo.kodinerds.net/{address}"
        package = from_address(address)
        pvt_key = join(CACHE_FOLDER_NAME, "adbkey")
        pub_key = pvt_key + ".pub"
        if not exists(pvt_key):
            keygen(pvt_key)
        with open(pub_key) as f:
            pub_bin = f.read()
        with open(pvt_key) as f:
            pvt_bin = f.read()
        manager = AdbDeviceTcp("192.168.1.62")
        manager.connect(rsa_keys=[PythonRSASigner(pub_bin, pvt_bin)], auth_timeout_s=0.1)
        filesize = getsize(package)
        deposit = join("/sdcard", basename(package))
        manager.push(package, deposit)
        manager.shell(f"cat {deposit} | pm install -S {filesize}")
        self.loading = False


if __name__ == "__main__":
    MainApp().run()
