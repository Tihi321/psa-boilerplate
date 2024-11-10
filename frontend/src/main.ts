import "./style.css";
import typescriptLogo from "./typescript.svg";
import viteLogo from "/vite.svg";
import { initializeSocket } from "psa-api";
import { setupButtons } from "./buttons.ts";

initializeSocket(() => {
  console.log("Connected to Python backend!");
});

document.querySelector<HTMLDivElement>("#header")!.innerHTML = `
  <a href="https://vite.dev" target="_blank">
    <img src="${viteLogo}" class="logo" alt="Vite logo" />
  </a>
  <a href="https://www.typescriptlang.org/" target="_blank">
    <img src="${typescriptLogo}" class="logo vanilla" alt="TypeScript logo" />
  </a>
`;

setupButtons();
