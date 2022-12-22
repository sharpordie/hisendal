**Ensure You Are on a Bridged Network**

This example will not work on a NAT network, so use device or an emulator with a bridged network interface.

**Alter the Device Address**

Replace address in [AndroidScreenViewModel.kt](app/src/main/java/com/example/hisendal/AndroidScreenViewModel.kt).

```kotlin
private var address = mutableStateOf("192.168.X.XX")
```

**Force Refreshing the ADB Keys**

Change refresh parameter in [Device.kt](app/src/main/java/com/example/hisendal/Device.kt).

```kotlin
handler = Dadb.discover(address, keygen(refresh = true))
```
