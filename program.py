print("welcome to outfit recommender")
// CONFIGURATION
const API_KEY = 'YOUR_API_KEY'; // Replace with your actual OpenWeatherMap API key
const city = 'London'; // You can dynamically set this based on user location

// Fetch current weather data
fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`)
  .then(response => {
    if (!response.ok) throw new Error('Failed to fetch weather data');
    return response.json();
  })
  .then(data => {
    const tempC = data.main.temp - 273.15; // Convert from Kelvin to Celsius
    const weatherMain = data.weather[0].main; // e.g., Rain, Clear, Snow
    const isRaining = weatherMain.toLowerCase().includes('rain');
    const isSnowing = weatherMain.toLowerCase().includes('snow');

    console.log(`🌡️ Temperature: ${tempC.toFixed(1)}°C`);
    console.log(`🌦️ Weather: ${weatherMain}`);

    // Sample outfit suggestion logic
    let outfit = '';

    if (isSnowing) {
      outfit = 'Wear a heavy coat, boots, gloves, and a scarf.';
    } else if (isRaining) {
      outfit = 'Wear a raincoat, waterproof shoes, and carry an umbrella.';
    } else if (tempC < 10) {
      outfit = 'Wear a jacket and layered clothing.';
    } else if (tempC < 20) {
      outfit = 'Wear a light sweater or long-sleeve shirt.';
    } else {
      outfit = 'Wear shorts and a t-shirt.';
    }

    console.log(`👕 Recommended Outfit: ${outfit}`);
    
    // Optional: Update UI here if you're using React, Vue, etc.

  })
  .catch(error => {
    console.error('Error fetching weather data:', error);
  });

