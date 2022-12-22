**Alter the device address**

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

**Force refreshing the ADB keys**

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```

**Some screenshots**

<img src="assets/img1.png" width="32.333%"/></a><a><img src="assets/none.png" width="1.5%"/><img src="assets/img2.png" width="32.333%"/><img src="assets/none.png" width="1.5%"/><img src="assets/img3.png" width="32.333%"/>
