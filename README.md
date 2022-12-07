<div><hr>
<a href="../.."><img align="right" height="91" src="assets/logo.png"></a>
<h1>HISENDAL</h1>
<p>Dadb Usage Within Android</p>
<hr></div>

<!--
<h2><samp>COVERAGE</samp></h2>
<h2><samp>DOWNLOAD</samp></h2>
<h2><samp>EXAMPLES</samp></h2>
<h2><samp>GUIDANCE</samp></h2>
<h2><samp>IGNITION</samp></h2>
<h2><samp>OVERVIEW</samp></h2>
<h2><samp>PICTURES</samp></h2>
<h2><samp>SHOWCASE</samp></h2>
<h2><samp>STARTING</samp></h2>
-->

<h2><samp>OVERVIEW</samp></h2>

Example of an Android application that uses Dadb to connect to an Android device and returns its product name.
Note this example will not work in emulator with a NAT network.

<h2><samp>STARTING</samp></h2>

### Alter the Device Address

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

### Force Refreshing the ADB Keys

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```

<h2><samp>SHOWCASE</samp></h2>

<a href="assets/img1.png"><img src="assets/img1.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img2.png"><img src="assets/img2.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img3.png"><img src="assets/img3.png" width="32%"/></a>

<h2></h2>
