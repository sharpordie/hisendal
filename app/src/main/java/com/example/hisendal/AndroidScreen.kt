package com.example.hisendal

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.CircularProgressIndicator
import androidx.compose.material.Icon
import androidx.compose.material.Text
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.launch

@Composable
fun AndroidScreen(viewModel: AndroidScreenViewModel) {
    val scoping = rememberCoroutineScope()
    Column(
        horizontalAlignment = Alignment.CenterHorizontally
    )
    {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center,
            modifier = Modifier
                .fillMaxWidth()
                .weight(1f)
                .background(Color(0xfffafafa))
                .padding(40.dp)
        ) {
            if (viewModel.loading.value) {
                CircularProgressIndicator(
                    strokeWidth = 32.dp,
                    modifier = Modifier.size(200.dp),
                )
            } else {
                CircularProgressIndicator(
                    progress = 1.0f,
                    strokeWidth = 32.dp,
                    modifier = Modifier.size(200.dp),
                )
            }
            Spacer(modifier = Modifier.height(56.dp))
            Text(
                text = if (viewModel.loading.value) "Loading, please wait" else viewModel.content.value,
                color = Color.Black,
                style = TextStyle(
                    fontSize = 28.sp,
                    lineHeight = 48.sp,
                    textAlign = TextAlign.Center
                )
            )
        }
        Row(
            horizontalArrangement = Arrangement.spacedBy(16.dp),
            modifier = Modifier
                .fillMaxWidth()
                .background(Color.DarkGray)
                .padding(16.dp)
        ) {
            Button(
                onClick = {
                    scoping.launch {
                        viewModel.onContinueButtonClicked()
                    }
                },
                enabled = !viewModel.loading.value,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(56.dp),
            ) {
                Icon(
                    Icons.Default.ArrowForward,
                    contentDescription = "",
                    tint = Color.White,
                    modifier = Modifier.fillMaxSize(),
                )
            }
        }
    }
}