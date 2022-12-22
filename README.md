# <samp>HISENDAL</samp>

Android application that uses the [dadb](https://github.com/mobile-dev-inc/dadb) library.

<!--
## <samp>OVERVIEW</samp>
## <samp>EXAMPLES</samp>
## <samp>SUPPORTS</samp>
## <samp>SOLUTION</samp>
## <samp>GUIDANCE</samp>
## <samp>SCHEDULE</samp>
-->

## <samp>GUIDANCE</samp>

### Verify the device network

<table>
  <tr>
    <td width="20%">
      <img src="https://cdn-icons-png.flaticon.com/512/3061/3061375.png"/>
    </td>
    <td>
      This example will not work on a device with NAT network which is the default on Android emulators.
      Therefore you will need to use a physical Android device or an Android emulator that supports bridge network.
      Actually using bridge network with the default emulators is doable, but it is not that simple and is quite different from one host system to another.
    </td>
  </tr>
</table>

<div>
<img align="left" src="https://cdn-icons-png.flaticon.com/512/3061/3061375.png" height="65"/>
This example will not work on a device with NAT network which is the default on Android emulators.
Therefore you will need to use a physical Android device or an Android emulator that supports bridge network.
Actually using bridge network with the default emulators is doable, but it is not that simple and is quite different from one host system to another.
</div>
  
### Change the device address

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

### Vanish the device keys

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```

## <samp>OVERVIEW</samp>

<img src="assets/img1.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img2.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/>
