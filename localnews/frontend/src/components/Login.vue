<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../store'
import authService from '../services/auth'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const userStore = useUserStore()

async function handleLogin() {
  try {
    const response = await authService.login({ email: email.value, password: password.value })
    userStore.setToken(response.data.access_token, response.data.user_id)
    router.push('/')
  } catch (err) {
    error.value = err.response?.data?.msg || 'Login failed'
  }
}
</script>

<template>
  <div class="max-w-md mx-auto bg-white p-8 rounded shadow">
    <h2 class="text-2xl font-bold mb-6">Login</h2>
    <form @submit.prevent="handleLogin" class="space-y-4">
      <div>
        <label class="block text-gray-700">Email</label>
        <input v-model="email" type="email" required class="w-full border p-2 rounded" />
      </div>
      <div>
        <label class="block text-gray-700">Password</label>
        <input v-model="password" type="password" required class="w-full border p-2 rounded" />
      </div>
      <div v-if="error" class="text-red-500">{{ error }}</div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Login</button>
    </form>
  </div>
</template>
