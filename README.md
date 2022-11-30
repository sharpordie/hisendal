<hr><div>
<a href="../.."><img align="left" height="91" src="https://user-images.githubusercontent.com/72373746/204132526-193bd3df-e3fd-4f33-99e0-eea7972247f8.png" alt="logo"></a>
<h1>HISENDAL</h1>
<p>Dadb usage within Android</p>
</div><hr>

<!--
## PREFACE
## FUNDING
## FEATURE
## STARTER
## GALLERY
## EXECUTE
## CAUTION
## PREVIEW
## RELEASE
## TEASING
-->

## PREFACE

Example of an Android application that uses Dadb to connect to an Android device and returns its product name.
Note this example will not work in emulator with a NAT network.

## FUNDING

<a href="../.." target="_blank"><img src="https://raw.githubusercontent.com/sharpordie/mybadges/main/src/kofi.svg" width="260"></a>

## CAUTION

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

## GALLERY

<a href="assets/img1.png"><img src="assets/img1.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img2.png"><img src="assets/img2.png" width="32%"/></a><a><img src="assets/none.png" width="2%"/></a><a href="assets/img3.png"><img src="assets/img3.png" width="32%"/></a>
