const URI = "ws://172.20.10.2:8765";

// Create WebSocket connection.
const socket = new WebSocket(URI);

// Connection opened
// socket.addEventListener('open', (event) => {
//     socket.send('Hello Server!');
// });

// Listen for messages
socket.addEventListener("message", (event) => {
  console.log("Message from server ", event.data);
});
