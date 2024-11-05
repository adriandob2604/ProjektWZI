import axios from "axios";
import React, { useState, useEffect } from "react";

interface Station {
  actual_date: string;
  adres: string;
  name: string;
  price: string;
}

function Stations(): JSX.Element {
  const [data, setData] = useState<Station[]>([]);

  useEffect(() => {
    axios.get("http://localhost:5000/stations").then((response) => {
      setData(response.data);
      console.log(response.data);
    });
  }, []);

  return (
    <>
      <div>Stacja</div>
      <div>E95</div>
      {data.map((station, index) => (
        <div key={index}>
          <div>{station.name}</div>
          <div>{station.adres}</div>
          <div>{station.price}</div>
          <div>{station.actual_date}</div>
        </div>
      ))}
    </>
  );
}

export default Stations;
