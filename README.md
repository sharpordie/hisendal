# <samp>HISENDAL</samp>

Android application that uses the [dadb](https://github.com/mobile-dev-inc/dadb) library.

## <samp>PREFACE</samp>
## <samp>SURFACE</samp>
## <samp>GALLERY</samp>
## <samp>PROCESS</samp>
## <samp>SERVICE</samp>
## <samp>HANDOUT</samp>
## <samp>WARNING</samp>
## <samp>EXAMPLE</samp>
## <samp>SAMPLES</samp>
## <samp>STARTER</samp>
## <samp>ANSWERS</samp>

### Ensure you are on a bridged network

This example will not work on a NAT network, so use a device or an emulator with a bridged network interface.

### Alter the device address

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

### Force refreshing the keys

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```

## <samp>GLASSWARE</samp>

<img src="assets/img1.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img2.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/>
