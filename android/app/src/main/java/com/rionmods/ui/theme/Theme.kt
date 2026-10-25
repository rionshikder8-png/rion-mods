package com.rionmods.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFF00E5FF),
    secondary = Color(0xFFB388FF),
    tertiary = Color(0xFFD50000),
    background = Color(0xFF0A0A12),
    surface = Color(0xFF161622)
)

@Composable
fun RionModsTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DarkColorScheme,
        content = content
    )
}
