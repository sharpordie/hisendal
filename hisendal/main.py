from os.path import abspath, basename, dirname, exists, getsize, join
from re import search
from threading import Thread
from urllib.request import Request, urlopen

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.keygen import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from kivy.app import App
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class MainView(BoxLayout):
    results = ObjectProperty()
    loading = BooleanProperty(False)

    def __init__(self):
        super(MainView, self).__init__()

    def gather(self):
        Thread(target=self._gather).start()

    def update(self):
        Thread(target=self._update).start()

    def _gather(self):
        self.loading = True

        pvt_key = join(abspath(join(dirname(__file__))), "adbkey")
        pub_key = pvt_key + ".pub"
        if not exists(pvt_key):
            keygen(pvt_key)
        with open(pub_key) as f:
            pub_bin = f.read()
        with open(pvt_key) as f:
            pvt_bin = f.read()
        try:
            manager = AdbDeviceTcp("192.168.1.62")
            manager.connect(rsa_keys=[PythonRSASigner(pub_bin, pvt_bin)], auth_timeout_s=0.1)
            self.results.text = manager.shell("getprop ro.product.model")
        except:
            self.results.text = "Authentication required"
        finally:
            self.loading = False

    def _update(self):
        self.loading = True
        website = "arm64-v8a"
        website = f"https://repo.kodinerds.net/index.php?action=list&scope=cat&item=Binary%20({website})"
        pattern = 'download=(.*Matrix.apk)(?=")'
        content = urlopen(Request(website, headers={"user-agent": "mozilla/5.0"})).read().decode()
        address = search(pattern, content).group(1)
        address = f"https://repo.kodinerds.net/{address}"
        self.results.text = basename(address)
        self.loading = False


class Hisendal(App):
    def build(self):
        return MainView()


Hisendal().run()
