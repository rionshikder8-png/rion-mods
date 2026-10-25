package com.rionmods.dashboard

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController

@Composable
fun DashboardScreen(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF0A0A12))
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = "RION MODS",
            color = Color(0xFF00E5FF),
            fontSize = 28.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(top = 32.dp, bottom = 24.dp)
        )
        
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = Color(0xFF161622))
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text("System Status: DISCONNECTED", color = Color.White)
                Text("Registered Devices: 0", color = Color.Gray)
            }
        }
        
        Spacer(modifier = Modifier.height(24.dp))
        
        Button(
            onClick = { navController.navigate("pairing") },
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF00E5FF)),
            modifier = Modifier.fillMaxWidth().height(50.dp)
        ) {
            Text("PAIR DEVICE", color = Color.Black, fontWeight = FontWeight.Bold)
        }
        
        Spacer(modifier = Modifier.height(16.dp))
        
        Button(
            onClick = { navController.navigate("prank") },
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFD50000)),
            modifier = Modifier.fillMaxWidth().height(50.dp)
        ) {
            Text("ATTACK MODE (PRANK)", color = Color.White, fontWeight = FontWeight.Bold)
        }
    }
}
