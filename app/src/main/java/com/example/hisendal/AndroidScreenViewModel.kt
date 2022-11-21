package com.example.hisendal

import android.app.Application
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withTimeoutOrNull

class AndroidScreenViewModel(application: Application) : AndroidViewModel(application) {
    private val context by lazy { application.baseContext }
    private var address = mutableStateOf("192.168.1.50")
    var content = mutableStateOf("Press the button")
    var loading = mutableStateOf(false)

    suspend fun onContinueButtonClicked() = viewModelScope.launch {
        loading.value = true
        val device = Device(address.value, context)
        try {
            device.attach()
            val invoked = device.invoke("getprop ro.product.model")
            device.detach()
            content.value = invoked.output.trim()
        } catch (e: Exception) {
            content.value = e.message.toString()
        }
        loading.value = false
    }
}