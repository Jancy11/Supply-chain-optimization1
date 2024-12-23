import React from "react";
import { Line } from "react-chartjs-2";

function Dashboard({ forecastData }) {
  const data = {
    labels: forecastData.dates,
    datasets: [
      {
        label: "Forecasted Demand",
        data: forecastData.values,
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  return (
    <div>
      <h2>Demand Forecast Dashboard</h2>
      <Line data={data} />
    </div>
  );
}

export default Dashboard;
