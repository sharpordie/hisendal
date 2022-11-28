<hr><div>
<a href="../.."><img align="right" height="91" src="assets/logo.png" alt="logo"></a>
<h1>Hisendal</h1>
<p>Dadb usage within Android</p>
</div><hr>

## `Overview`

Example of an Android application that uses Dadb to connect to an Android device and returns its product name.
Note this example will not work in emulator with a NAT network.

## `Donation`

<a href=""><img src="https://fakeimg.pl/260x80/000/fff/?text=‏‏‎ ‎" width="260"></a>

## `Guidance`

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

## `Pictures`

<a href="assets/img1.png"><img src="assets/img1.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img2.png"><img src="assets/img2.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img3.png"><img src="assets/img3.png" width="32%"/></a>
