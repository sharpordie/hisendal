<div>
<img align="right" src="https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/61e11d430afb112ea33c3aa5_Button-1-p-800.png" width="260"/>
<h1><code>Hisendal</code></h1>
</div>

Example of an Android application that uses Dadb to connect to an Android device and returns its product name.
Note this example will not work in emulator with a NAT network.

<h2><code>Guidance</code></h2>

### Alter the device address

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

### Force refreshing the adb keys

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```

<h2><code>Showcase</code></h2>

<a href="assets/img1.png"><img src="assets/img1.png" width="32.666%"/></a><a><img src="assets/none.png" width="1%"/></a><a href="assets/img2.png"><img src="assets/img2.png" width="32.666%"/></a><a><img src="assets/none.png" width="1%"/></a><a href="assets/img3.png"><img src="assets/img3.png" width="32.666%"/></a>
