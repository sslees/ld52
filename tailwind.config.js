/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: [
      {
        harvest: {
          "primary": "#9f1239",
          "secondary": "#dc2626",
          "accent": "#3730a3",
          "neutral": "#111827",
          "base-100": "#1f2937",
          "info": "#6b7280",
          "success": "#3f6212",
          "warning": "#fcd34d",
          "error": "#f87171",
        }
      }
    ],
  },
}
