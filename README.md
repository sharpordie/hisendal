<h1><samp>HISENDAL</samp></h1>

Android application that uses the [dadb](https://github.com/mobile-dev-inc/dadb) library.

<!--
## <samp>OVERVIEW</samp>
## <samp>EXAMPLES</samp>
## <samp>SUPPORTS</samp>
## <samp>SOLUTION</samp>
## <samp>GUIDANCE</samp>
## <samp>SCHEDULE</samp>
-->

## <samp>OVERVIEW</samp>

<img src="assets/img1.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img2.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/>

## <samp>GUIDANCE</samp>

### Verify the device network

This example will not work on a device with NAT network which is the default on Android emulators.
Therefore you will need to use a physical Android device or an Android emulator that supports bridge network.

<!--
<table>
  <tr>
    <td align="center" valign="middle">
      <p><br><img src="https://cdn-icons-png.flaticon.com/512/2058/2058197.png" width="80%"/><br></p>
    </td>
    <td width="85%">
      This example will not work on a device with NAT network which is the default on Android emulators.
      Therefore you will need to use a physical Android device or an Android emulator that supports bridge network.
    </td>
  </tr>
</table>
-->

### Change the device address

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

### Vanish the connection keys

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```
