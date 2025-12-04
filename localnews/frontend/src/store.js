import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
    const token = ref(localStorage.getItem('access_token'))
    const userId = ref(localStorage.getItem('user_id'))
    const user = ref(null)

    const isAuthenticated = computed(() => !!token.value)

    function setToken(newToken, newUserId) {
        token.value = newToken
        userId.value = newUserId
        localStorage.setItem('access_token', newToken)
        localStorage.setItem('user_id', newUserId)
    }

    function logout() {
        token.value = null
        userId.value = null
        user.value = null
        localStorage.removeItem('access_token')
        localStorage.removeItem('user_id')
    }

    return { token, userId, user, isAuthenticated, setToken, logout }
})
