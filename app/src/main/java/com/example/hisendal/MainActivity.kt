package com.example.hisendal

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.Surface
import androidx.compose.ui.Modifier
import com.example.hisendal.ui.theme.HisendalTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val viewModel: AndroidScreenViewModel by viewModels()
        setContent {
            HisendalTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    AndroidScreen(viewModel)
                }
            }
        }
    }
}