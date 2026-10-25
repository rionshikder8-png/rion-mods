package com.rionmods.pairing

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

@Composable
fun PairingScreen(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF0A0A12))
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("PAIR DEVICE", color = Color.White, modifier = Modifier.padding(top = 32.dp))
        Spacer(modifier = Modifier.height(32.dp))
        Text("Scan QR code or enter PIN from Terminal", color = Color.Gray)
        Spacer(modifier = Modifier.height(16.dp))
        Button(
            onClick = { navController.popBackStack() },
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF00E5FF))
        ) {
            Text("BACK", color = Color.Black)
        }
    }
}
