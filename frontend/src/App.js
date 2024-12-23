import React, { useEffect, useState } from "react";
import Dashboard from "./components/Dashboard";

function App() {
  const [forecastData, setForecastData] = useState({ dates: [], values: [] });

  useEffect(() => {
    fetch("/forecast", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ data_path: "sales_data.csv" }),
    })
      .then((response) => response.json())
      .then((data) =>
        setForecastData({
          dates: Array.from({ length: data.length }, (_, i) => `Day ${i + 1}`),
          values: data,
        })
      );
  }, []);

  return (
    <div>
      <Dashboard forecastData={forecastData} />
    </div>
  );
}

export default App;
