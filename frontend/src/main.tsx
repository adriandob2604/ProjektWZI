import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Stations from "./assets/components/stations.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Stations />
  </StrictMode>
);
