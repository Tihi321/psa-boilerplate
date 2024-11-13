import "./style.css";
import typescriptLogo from "./typescript.svg";
import viteLogo from "/vite.svg";
import { setupButtons } from "./buttons.ts";
import { initializeSocket } from "psa-api";

initializeSocket((value) => {
  console.log(value);
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
