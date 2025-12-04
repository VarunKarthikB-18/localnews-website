<script setup>
import { computed } from 'vue'
import { useUserStore } from '../store'
import newsService from '../services/newsService'

const props = defineProps({
  article: Object
})

const userStore = useUserStore()

const formattedDate = computed(() => {
  if (!props.article.published_at) return ''
  return new Date(props.article.published_at).toLocaleDateString()
})

async function saveArticle() {
  if (!userStore.isAuthenticated) {
    alert('Please login to save articles')
    return
  }
  try {
    await newsService.saveArticle(props.article)
    alert('Article saved!')
  } catch (err) {
    alert(err.response?.data?.msg || 'Failed to save')
  }
}
</script>

<template>
  <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden flex flex-col h-full hover:shadow-xl transition-all duration-300 hover:-translate-y-1 group">
    <div class="relative h-48 overflow-hidden">
      <img v-if="article.image_url" :src="article.image_url" alt="Article Image" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" />
      <div v-else class="h-full w-full bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center text-gray-400">
        <span class="text-4xl">📰</span>
      </div>
      <div class="absolute top-3 left-3 bg-white/90 backdrop-blur text-xs font-bold px-2 py-1 rounded-md shadow-sm text-gray-800">
        {{ article.source_name }}
      </div>
    </div>
    
    <div class="p-5 flex-1 flex flex-col">
      <div class="text-xs font-medium text-gray-400 mb-2 uppercase tracking-wide">{{ formattedDate }}</div>
      <h3 class="text-lg font-bold mb-3 leading-tight text-gray-900 group-hover:text-blue-600 transition-colors">
        <router-link :to="`/article/${encodeURIComponent(article.external_id)}`">
          {{ article.title }}
        </router-link>
      </h3>
      <p class="text-gray-600 text-sm mb-4 line-clamp-3 flex-1 leading-relaxed">{{ article.description }}</p>
      
      <div class="flex justify-between items-center mt-auto pt-4 border-t border-gray-50">
        <a :href="article.url" target="_blank" class="text-blue-600 text-sm font-medium hover:text-blue-800 flex items-center gap-1">
          Read Original
          <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
          </svg>
        </a>
        <button v-if="userStore.isAuthenticated" @click="saveArticle" class="text-gray-400 hover:text-blue-500 transition-colors p-2 hover:bg-blue-50 rounded-full">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
