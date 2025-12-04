<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import authService from '../services/auth'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

async function handleRegister() {
  try {
    await authService.register({ email: email.value, password: password.value })
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.msg || 'Registration failed'
  }
}
</script>

<template>
  <div class="max-w-md mx-auto bg-white p-8 rounded shadow">
    <h2 class="text-2xl font-bold mb-6">Register</h2>
    <form @submit.prevent="handleRegister" class="space-y-4">
      <div>
        <label class="block text-gray-700">Email</label>
        <input v-model="email" type="email" required class="w-full border p-2 rounded" />
      </div>
      <div>
        <label class="block text-gray-700">Password</label>
        <input v-model="password" type="password" required class="w-full border p-2 rounded" />
      </div>
      <div v-if="error" class="text-red-500">{{ error }}</div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Register</button>
    </form>
  </div>
</template>
