from asyncio import run
from os.path import abspath, basename, dirname, exists, getsize, join
from re import search
from threading import Thread

from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.adb_device_async import AdbDeviceTcpAsync
from adb_shell.auth.keygen import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from kivy.app import App
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from requests import get

from services.netsense import from_address, from_dropbox


class MainView(BoxLayout):
    address = ObjectProperty()
    results = ObjectProperty()
    loading = BooleanProperty(False)

    def __init__(self):
        super(MainView, self).__init__()

    def gather(self):
        Thread(target=self._gather).start()

    def unpack(self):
        Thread(target=run, args=(self._unpack(),)).start()

    def update(self):
        Thread(target=run, args=(self._update(),)).start()

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
            manager = AdbDeviceTcp(self.address.text)
            manager.connect(rsa_keys=[PythonRSASigner(pub_bin, pvt_bin)], auth_timeout_s=0.1)
            self.results.text = manager.shell("getprop ro.product.model").strip()
        except Exception as e:
            self.results.text = str(e)
        finally:
            self.loading = False

    async def _unpack(self):
        try:
            self.loading = True
            pvt_key = join(abspath(join(dirname(__file__))), "adbkey")
            pub_key = pvt_key + ".pub"
            if not exists(pvt_key):
                keygen(pvt_key)
            with open(pub_key) as f:
                pub_bin = f.read()
            with open(pvt_key) as f:
                pvt_bin = f.read()
            manager = AdbDeviceTcpAsync(self.address.text)
            await manager.connect(rsa_keys=[PythonRSASigner(pub_bin, pvt_bin)], auth_timeout_s=0.1)
            address = f"https://www.dropbox.com/s/f5dz07b4t4bm9s3/shield_dummies_20220710.zip?dl=0"
            package = from_dropbox(address)
            deposit = join("/sdcard", basename(package))
            await manager.push(package, deposit, read_timeout_s=20)
            await manager.shell(f"cd {dirname(deposit)} ; unzip -o {deposit}")
            self.results.text = "UNPACKED"
        except Exception as e:
            self.results.text = str(e)
        finally:
            await manager.close()
            self.loading = False

    async def _update(self):
        try:
            self.loading = True
            pvt_key = join(abspath(join(dirname(__file__))), "adbkey")
            pub_key = pvt_key + ".pub"
            if not exists(pvt_key):
                keygen(pvt_key)
            with open(pub_key) as f:
                pub_bin = f.read()
            with open(pvt_key) as f:
                pvt_bin = f.read()
            manager = AdbDeviceTcpAsync(self.address.text)
            await manager.connect(rsa_keys=[PythonRSASigner(pub_bin, pvt_bin)], auth_timeout_s=0.1)
            bitness = (await manager.shell("uname -m")).strip()
            website = "arm64-v8a" if bitness == "aarch64" else "armeabi-v7a"
            website = f"https://repo.kodinerds.net/index.php?action=list&scope=cat&item=Binary%20({website})"
            pattern = 'download=(.*Matrix.apk)(?=")'
            content = get(website, headers={"user-agent": "mozilla/5.0"}, allow_redirects=True).content.decode()
            address = search(pattern, content).group(1)
            address = f"https://repo.kodinerds.net/{address}"
            package = from_address(address)
            filesize = getsize(package)
            deposit = join("/sdcard", basename(package))
            await manager.push(package, deposit, read_timeout_s=20)
            await manager.shell(f"cat {deposit} | pm install -S {filesize}")
            self.results.text = "INSTALLED"
        except Exception as e:
            self.results.text = str(e)
        finally:
            await manager.close()
            self.loading = False


class Hisendal(App):
    def build(self):
        return MainView()


Hisendal().run()
