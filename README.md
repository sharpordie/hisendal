<hr><div>
<a href="../.."><img align="right" height="94" src="https://user-images.githubusercontent.com/72373746/205586156-a45fc4a0-8aa7-4a71-908c-bae4c07ed41d.png"></a>
<h1><code>HISENDAL</code></h1>
<p>Dadb Usage Within Android</p>
</div><hr>

<!--
## `DOWNLOAD`
## `EXAMPLES`
## `GUIDANCE`
## `IGNITION`
## `OVERVIEW`
## `PICTURES`
## `STARTING`
-->

## `OVERVIEW`

Example of an Android application that uses Dadb to connect to an Android device and returns its product name.
Note this example will not work in emulator with a NAT network.

## `STARTING`

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

## `PICTURES`

<a href="assets/img1.png"><img src="assets/img1.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img2.png"><img src="assets/img2.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img3.png"><img src="assets/img3.png" width="32%"/></a>
