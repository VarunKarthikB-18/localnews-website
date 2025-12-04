import api from './api'

export default {
    register(credentials) {
        return api.post('/auth/register', credentials)
    },
    login(credentials) {
        return api.post('/auth/login', credentials)
    },
    getProfile() {
        return api.get('/user/profile')
    },
    updateProfile(data) {
        return api.put('/user/profile', data)
    },
    getPreferences() {
        // Assuming profile contains preferences
        return api.get('/user/profile').then(res => res.data.preferences)
    }
}
