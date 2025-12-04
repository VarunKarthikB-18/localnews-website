<script setup>
import { ref } from 'vue'

const emit = defineEmits(['change'])
const city = ref('')

function updateLocation() {
  emit('change', city.value)
}
</script>

<template>
  <div class="flex gap-2 relative group">
    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400 group-focus-within:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
      </svg>
    </div>
    <input 
      v-model="city" 
      @change="updateLocation"
      type="text" 
      placeholder="Enter city..." 
      class="border border-gray-300 pl-10 pr-4 py-2 rounded-lg w-full md:w-64 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
    />
  </div>
</template>
