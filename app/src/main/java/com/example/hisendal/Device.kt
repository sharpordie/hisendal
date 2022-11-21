package com.example.hisendal

import android.content.Context
import dadb.AdbKeyPair
import dadb.AdbShellResponse
import dadb.Dadb
import kotlinx.coroutines.DelicateCoroutinesApi
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.async
import kotlinx.coroutines.withContext
import java.io.File

class Device(private val address: String, private val context: Context) {
    private lateinit var manager: Dadb

    suspend fun attach(timeout: Int = 5000) = withContext(IO) {
        var handler: Dadb? = null
        val running = GlobalScope.async { handler = Dadb.discover(address, keygen(refresh = false)) }
        Thread.sleep(timeout.toLong())
        running.cancel()
        if (handler == null) throw Exception("Target machine is waiting for authorization, authorize and retry")
        manager = handler as Dadb
    }

    suspend fun detach() = withContext(IO) {
        manager.close()
    }

    suspend fun gather(distant: String): String? = withContext(IO) {
        val created = File(context.cacheDir, File(distant).name) // TODO: Test the basename.
        manager.pull(File(distant), created.path)
        if (created.exists()) created.path else null
    }

    suspend fun invoke(command: String): AdbShellResponse = withContext(IO) {
        manager.shell(command)
    }

    suspend fun keygen(refresh: Boolean = false): AdbKeyPair = withContext(IO) {
        val deposit = context.cacheDir
        val pvtFile = File(deposit, "adbkey")
        val pubFile = File(deposit, "adbkey.pub")
        if (refresh || !pubFile.exists() || !pvtFile.exists()) {
            if (pubFile.exists()) pubFile.delete()
            if (pvtFile.exists()) pvtFile.delete()
            AdbKeyPair.generate(pvtFile, pubFile)
        }
        AdbKeyPair.read(pvtFile, pubFile)
    }

    suspend fun upload(storage: String, distant: String) = withContext(IO) {
        manager.push(File(storage), distant)
    }
}