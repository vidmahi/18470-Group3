import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/login': 'http://127.0.0.1:5000',
      '/add_user': 'http://127.0.0.1:5000',
      '/main': 'http://127.0.0.1:5000',
      '/join_project': 'http://127.0.0.1:5000',
      '/get_user_projects_list': 'http://127.0.0.1:5000',
      '/create_project': 'http://127.0.0.1:5000',
      '/get_project_info': 'http://127.0.0.1:5000',
      '/get_all_hw_names': 'http://127.0.0.1:5000',
      '/get_hw_info': 'http://127.0.0.1:5000',
      '/check_out': 'http://127.0.0.1:5000',
      '/check_in': 'http://127.0.0.1:5000',
      '/create_hardware_set': 'http://127.0.0.1:5000',
      '/api/inventory': 'http://127.0.0.1:5000',
    }
  }
})
