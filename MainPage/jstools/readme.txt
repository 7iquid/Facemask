npm install -D tailwindcss
npm install autoprefixer

npx tailwindcss init

module.exports = {  content: ["./src/**/*.{html,js}"],  theme: {    extend: {},  },  plugins: [],}


npx tailwindcss -i ../static/css/tailwind.css -o ../static/css/style.css


