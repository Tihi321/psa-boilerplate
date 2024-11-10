/* @refresh reload */
import { render } from "solid-js/web";
import App from "./App";
import { initializeSocket } from "./hooks/connection";

const root = document.getElementById("root");

if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
  throw new Error("Root element not found. Did you forget to add it to your index.html?");
}

initializeSocket(() => {
  console.log("Connected to Python backend!");
});

render(() => <App />, root!);
