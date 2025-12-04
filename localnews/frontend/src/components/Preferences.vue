<script setup>
import { ref, onMounted } from 'vue'
import authService from '../services/auth'

const location = ref('')
const message = ref('')

onMounted(async () => {
  try {
    const response = await authService.getProfile()
    location.value = response.data.preferred_location || ''
  } catch (err) {
    console.error(err)
  }
})

async function savePreferences() {
  try {
    await authService.updateProfile({ preferred_location: location.value })
    message.value = 'Preferences saved!'
    setTimeout(() => message.value = '', 3000)
  } catch (err) {
    message.value = 'Failed to save'
  }
}
</script>

<template>
  <div class="max-w-md mx-auto bg-white p-8 rounded shadow">
    <h2 class="text-2xl font-bold mb-6">Preferences</h2>
    <form @submit.prevent="savePreferences" class="space-y-4">
      <div>
        <label class="block text-gray-700">Preferred City</label>
        <input v-model="location" type="text" class="w-full border p-2 rounded" />
      </div>
      <div v-if="message" class="text-green-600">{{ message }}</div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Save Preferences</button>
    </form>
  </div>
</template>
