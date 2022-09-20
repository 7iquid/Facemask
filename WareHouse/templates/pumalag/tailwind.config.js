module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
  theme: {
  boxShadow: {
    loob: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0)'
    }
  }
}
