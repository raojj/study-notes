package com.joe.android

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.joe.android.ui.login.LoginScreen
import com.joe.android.ui.login.LoginViewModel
import com.joe.android.ui.theme.BasicGrammarTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            BasicGrammarTheme {
                val viewModel: LoginViewModel = viewModel()
                val uiState = viewModel.uiState.collectAsStateWithLifecycle().value

                LoginScreen(
                    uiState = uiState,
                    onUsernameChange = viewModel::onUsernameChange,
                    onPasswordChange = viewModel::onPasswordChange,
                    onRememberMeChange = viewModel::onRememberMeChange,
                    onPasswordVisibilityToggle = viewModel::onPasswordVisibilityToggle,
                    onLoginClick = viewModel::onLoginClick,
                    onForgotPasswordClick = {
                        Toast.makeText(this, R.string.login_forgot_password, Toast.LENGTH_SHORT).show()
                    },
                    onRegisterClick = {
                        Toast.makeText(this, R.string.login_register, Toast.LENGTH_SHORT).show()
                    },
                    modifier = Modifier.fillMaxSize(),
                )
            }
        }
    }
}
