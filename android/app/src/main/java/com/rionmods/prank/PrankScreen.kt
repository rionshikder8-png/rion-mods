package com.rionmods.prank

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import kotlinx.coroutines.delay

@Composable
fun PrankScreen(navController: NavController) {
    var timeLeft by remember { mutableStateOf(15) }
    var active by remember { mutableStateOf(true) }

    LaunchedEffect(active) {
        while (active && timeLeft > 0) {
            delay(1000)
            timeLeft--
        }
        if (timeLeft == 0) {
            navController.popBackStack()
        }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.Black)
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "RION MODS",
            color = Color.Red,
            fontSize = 42.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(bottom = 16.dp)
        )
        Text(
            text = "🖕",
            fontSize = 72.sp,
            modifier = Modifier.padding(bottom = 32.dp)
        )
        Text(
            text = "SYSTEM OVERRIDE SIMULATION",
            color = Color.Red,
            fontSize = 18.sp,
            fontWeight = FontWeight.Medium
        )
        Text(
            text = "JUST FOR FUN",
            color = Color.Gray,
            fontSize = 14.sp,
            modifier = Modifier.padding(vertical = 8.dp)
        )
        Text(
            text = "Restoring in: $timeLeft",
            color = Color.White,
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(bottom = 48.dp)
        )
        
        Button(
            onClick = { navController.popBackStack() },
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF333333)),
            modifier = Modifier.fillMaxWidth(0.6f)
        ) {
            Text("RESTORE NOW", color = Color.White)
        }
    }
}
