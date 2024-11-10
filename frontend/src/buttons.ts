import { sendAndReceive } from "psa-api";

export const setupButtons = () => {
  const receiveButton = document.querySelector<HTMLButtonElement>("#receiveButton")!;
  const resetButton = document.querySelector<HTMLButtonElement>("#resetButton")!;
  const messageElement = document.querySelector<HTMLButtonElement>("#message")!;

  const resetMessage = () => {
    messageElement?.setHTMLUnsafe("Hello from frontend!");
  };
  const receiveMessage = () => {
    console.log("send");
    sendAndReceive("message", "Hello from frontend!", (value) => {
      messageElement.setHTMLUnsafe(value);
    });
  };

  receiveButton.addEventListener("click", receiveMessage);
  resetButton.addEventListener("click", resetMessage);
};
