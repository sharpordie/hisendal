from os.path import abspath, dirname, exists, join

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.keygen import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        padding: [16, 16, 16, 16]
        spacing: 16
        TextInput:
            id: txt_inpt
            text: ""
        MDBoxLayout:
            orientation: "horizontal"
            spacing: 16
            MDRectangleFlatButton:
                on_release: app.clear()
                size_hint: 1.0, 1.0
                text: "CLEAR"
            MDRectangleFlatButton:
                on_release: app.fetch()
                size_hint: 1.0, 1.0
                text: "FETCH"
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def clear(self):
        self.root.ids.txt_inpt.text = ""

    def fetch(self):
        keypair = join(dirname(abspath(__file__)), "adbkey")
        if not exists(keypair):
            keygen(keypair)
        with open(keypair) as f:
            priv = f.read()
        with open(keypair + ".pub") as f:
            pub = f.read()
        machine = AdbDeviceTcp("192.168.1.62", 5555, default_transport_timeout_s=9.0)
        machine.connect(rsa_keys=[PythonRSASigner(pub, priv)], auth_timeout_s=0.1)
        content = machine.shell("getprop ro.product.model")
        self.root.ids.txt_inpt.text = content


MainApp().run()