/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        vinhomes: { blue: '#1A365D', gold: '#D4AF37' }
      }
    },
  },
  plugins: [],
}