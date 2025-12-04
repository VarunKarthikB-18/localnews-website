<script setup>
import { ref, onMounted, watch } from 'vue'
import newsService from '../services/newsService'
import ArticleCard from './ArticleCard.vue'
import LocationSelector from './LocationSelector.vue'

const articles = ref([])
const loading = ref(false)
const city = ref('')
const query = ref('')
const page = ref(1)

async function fetchNews() {
  loading.value = true
  try {
    const params = {
      city: city.value,
      q: query.value,
      page: page.value
    }
    const response = await newsService.getNews(params)
    if (page.value === 1) {
      articles.value = response.data.articles
    } else {
      articles.value.push(...response.data.articles)
    }
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

function handleLocationChange(newCity) {
  city.value = newCity
  page.value = 1
  fetchNews()
}

function handleSearch() {
  page.value = 1
  fetchNews()
}

function loadMore() {
  page.value++
  fetchNews()
}

onMounted(() => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords
        // Fetch news with lat/lon
        loading.value = true
        newsService.getNews({ lat: latitude, lon: longitude, page: 1 })
          .then(res => {
            articles.value = res.data.articles
            // If backend returns a location name (e.g. city), we could update city.value
          })
          .catch(err => console.error(err))
          .finally(() => loading.value = false)
      },
      (error) => {
        console.log('Geolocation denied or failed, using default')
        fetchNews()
      }
    )
  } else {
    fetchNews()
  }
})
</script>

<template>
  <div>
    <div class="mb-8 bg-white p-6 rounded-xl shadow-sm border border-gray-100">
      <div class="flex flex-col md:flex-row gap-4">
        <LocationSelector @change="handleLocationChange" />
        <div class="flex-1 flex gap-2">
          <input 
            v-model="query" 
            @keyup.enter="handleSearch"
            type="text" 
            placeholder="Search news topics..." 
            class="flex-1 border border-gray-300 px-4 py-2 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
          />
          <button @click="handleSearch" class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 font-medium transition-colors shadow-sm hover:shadow">
            Search
          </button>
        </div>
      </div>
    </div>

    <div v-if="loading && page === 1" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <ArticleCard v-for="article in articles" :key="article.url" :article="article" />
    </div>
    
    <div v-if="articles.length > 0" class="text-center mt-12 mb-8">
      <button @click="loadMore" :disabled="loading" class="bg-white border border-gray-200 text-gray-700 px-8 py-3 rounded-full hover:bg-gray-50 hover:border-gray-300 transition-all font-medium shadow-sm hover:shadow">
        {{ loading ? 'Loading...' : 'Load More Articles' }}
      </button>
    </div>
    
    <div v-if="!loading && articles.length === 0" class="text-center py-12 bg-white rounded-xl shadow-sm border border-gray-100">
      <p class="text-gray-500 text-lg">No news found matching your criteria.</p>
      <button @click="fetchNews" class="mt-4 text-blue-600 hover:underline">Refresh Feed</button>
    </div>
  </div>
</template>
