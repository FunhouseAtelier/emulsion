# routes/api/demo/weather/route.py

from fastapi import Request, HTTPException
import httpx

async def get_weather_data(request: Request):
    # Step 1: Get client IP
    client_ip = request.client.host
    if client_ip == "127.0.0.1":
      client_ip = "8.8.8.8"  # Google Public DNS — for testing purposes


    # Step 2: Get geolocation info from ip-api.com
    async with httpx.AsyncClient() as client:
        geo_response = await client.get(f"http://ip-api.com/json/{client_ip}")
        geo_data = geo_response.json()

        if geo_data.get("status") != "success":
            return {"error": "Failed to determine location."}

        lat = geo_data.get("lat")
        lon = geo_data.get("lon")
        city = geo_data.get("city", "Unknown")

    # Step 3: Fetch weather data from open-meteo.com
    async with httpx.AsyncClient() as client:
        weather_response = await client.get(
            f"https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "temperature_unit": "fahrenheit",
                "windspeed_unit": "mph",
                "current_weather": "true"
            }
        )
        weather_data = weather_response.json()

        current = weather_data.get("current_weather")
        if not current:
            raise HTTPException(status_code=400, detail="Weather data not found")

    # Step 4: Return simplified response
    return {
        "city": city,
        "temperature_f": current.get("temperature"),
        "windspeed_mph": current.get("windspeed"),
        "weather_code": current.get("weathercode")
    }

