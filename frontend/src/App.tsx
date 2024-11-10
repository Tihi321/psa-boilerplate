import { createSignal } from "solid-js";
import { sendMessage, subscribeMessage } from "./hooks/connection";

function App() {
  const [message, setMessage] = createSignal("Waiting for backend...");

  subscribeMessage((data) => {
    setMessage(data);
  });

  const sendButtonMessage = () => {
    sendMessage("Hello from frontend!");
  };

  return (
    <div class="container">
      <h1>Solid + Python WebView</h1>
      <p>{message()}</p>
      <button onClick={sendButtonMessage}>Send Message</button>
      <style>{`
        .container {
          text-align: center;
          padding: 2rem;
          font-family: Arial, sans-serif;
        }
        button {
          padding: 0.5rem 1rem;
          margin: 1rem;
          cursor: pointer;
        }
      `}</style>
    </div>
  );
}

export default App;
