package com.rionmods.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.rionmods.dashboard.DashboardScreen
import com.rionmods.prank.PrankScreen
import com.rionmods.pairing.PairingScreen

@Composable
fun RionNavGraph() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = "dashboard") {
        composable("dashboard") { DashboardScreen(navController) }
        composable("prank") { PrankScreen(navController) }
        composable("pairing") { PairingScreen(navController) }
    }
}
