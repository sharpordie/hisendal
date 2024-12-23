## OVERVIEW

<div id="toc">
  <ul style="list-style: none;">
    <summary>
      <h2>OVERVIEW</h2>
    </summary>
  </ul>
</div>

<div id="toc">
  <ul>
    <summary>
      <h2>OVERVIEW</h2>
    </summary>
  </ul>
</div>

Android application that uses the [dadb](https://github.com/mobile-dev-inc/dadb) library.

<img src="assets/img1.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img2.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="23.875%"/>

## DONATION

<a href="../.." target="_blank"><img src="https://raw.githubusercontent.com/sharpordie/mybadges/main/src/kofi.svg"></a>

## FEATURES

**Update and tweak Windows**  
Lorem ipsum odor amet, consectetuer adipiscing elit. 
**Update and tweak Firefox**  
Lorem ipsum odor amet, consectetuer adipiscing elit.

## DONATION

## GUIDANCE

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
