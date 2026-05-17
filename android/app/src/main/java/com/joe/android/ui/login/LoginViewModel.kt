package com.joe.android.ui.login

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.joe.android.R
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class LoginViewModel(
    application: Application,
) : AndroidViewModel(application) {

    private val _uiState = MutableStateFlow(LoginUiState())
    val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()

    private val resources get() = getApplication<Application>().resources

    fun onUsernameChange(value: String) {
        _uiState.update {
            it.copy(
                username = value,
                usernameError = null,
                loginError = null,
            )
        }
    }

    fun onPasswordChange(value: String) {
        _uiState.update {
            it.copy(
                password = value,
                passwordError = null,
                loginError = null,
            )
        }
    }

    fun onRememberMeChange(checked: Boolean) {
        _uiState.update { it.copy(rememberMe = checked) }
    }

    fun onPasswordVisibilityToggle() {
        _uiState.update { it.copy(isPasswordVisible = !it.isPasswordVisible) }
    }

    fun onLoginClick() {
        val state = _uiState.value
        if (state.isLoading) return

        val usernameError = validateUsername(state.username)
        val passwordError = validatePassword(state.password)

        if (usernameError != null || passwordError != null) {
            _uiState.update {
                it.copy(
                    usernameError = usernameError,
                    passwordError = passwordError,
                    loginError = null,
                )
            }
            return
        }

        viewModelScope.launch {
            _uiState.update {
                it.copy(
                    isLoading = true,
                    usernameError = null,
                    passwordError = null,
                    loginError = null,
                )
            }

            delay(800)

            val success = state.username == DEMO_USERNAME && state.password == DEMO_PASSWORD
            _uiState.update {
                it.copy(
                    isLoading = false,
                    isLoginSuccess = success,
                    loginError = if (success) null else resources.getString(R.string.login_error_invalid_credentials),
                )
            }
        }
    }

    private fun validateUsername(username: String): String? {
        return if (username.isBlank()) {
            resources.getString(R.string.login_error_username_empty)
        } else {
            null
        }
    }

    private fun validatePassword(password: String): String? {
        return when {
            password.isBlank() -> resources.getString(R.string.login_error_password_empty)
            password.length < MIN_PASSWORD_LENGTH -> resources.getString(R.string.login_error_password_short)
            else -> null
        }
    }

    companion object {
        const val DEMO_USERNAME = "demo"
        const val DEMO_PASSWORD = "123456"
        private const val MIN_PASSWORD_LENGTH = 6
    }
}
