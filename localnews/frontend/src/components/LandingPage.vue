<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateToFeed = () => {
  router.push('/feed')
}
</script>

<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center justify-center relative overflow-hidden">
    <!-- Floating Background Elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 opacity-10 transform -rotate-12 animate-float-slow">
        <span class="text-9xl">📰</span>
      </div>
      <div class="absolute bottom-20 right-10 opacity-10 transform rotate-12 animate-float-medium">
        <span class="text-9xl">🗞️</span>
      </div>
      <div class="absolute top-40 right-20 opacity-5 transform rotate-45 animate-float-fast">
        <span class="text-8xl">🌍</span>
      </div>
    </div>

    <!-- Hero Content -->
    <div class="z-10 text-center px-4 max-w-4xl mx-auto">
      <div class="mb-8 inline-block">
        <span class="bg-blue-100 text-blue-700 px-4 py-1.5 rounded-full text-sm font-bold tracking-wide uppercase shadow-sm">
          Hyper-Local News
        </span>
      </div>
      
      <h1 class="text-6xl md:text-8xl font-black text-gray-900 mb-6 tracking-tight leading-tight">
        Your City.<br/>
        <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
          Your News.
        </span>
      </h1>
      
      <p class="text-xl md:text-2xl text-gray-600 mb-12 max-w-2xl mx-auto leading-relaxed">
        Stay connected with what's happening right outside your door. Real-time local updates powered by AI.
      </p>
      
      <button 
        @click="navigateToFeed"
        class="group relative inline-flex items-center justify-center px-8 py-4 text-lg font-bold text-white transition-all duration-200 bg-blue-600 rounded-full hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-600 shadow-lg hover:shadow-xl transform hover:-translate-y-1"
      >
        Get Started
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ml-2 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(var(--rotation)); }
  50% { transform: translateY(-20px) rotate(var(--rotation)); }
}

.animate-float-slow {
  --rotation: -12deg;
  animation: float 8s ease-in-out infinite;
}

.animate-float-medium {
  --rotation: 12deg;
  animation: float 6s ease-in-out infinite;
}

.animate-float-fast {
  --rotation: 45deg;
  animation: float 5s ease-in-out infinite;
}
</style>
