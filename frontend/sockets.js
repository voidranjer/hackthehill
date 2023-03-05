const URI = "ws://172.20.10.7:8765";

// Create WebSocket connection.
const socket = new WebSocket(URI);

// Connection opened
// socket.addEventListener('open', (event) => {
//     socket.send('Hello Server!');
// });

// Listen for messages
socket.addEventListener("message", (event) => {
  const data = event.data;
  const element = document.getElementById("myImage");

  console.log("Message from server ", data);

  if (data === "landfill") {
    element.src = "first.png";
  } else if (data === "metal") {
    element.src = "second.png";
  } else if (data === "plastic") {
    element.src = "third.png";
  } else if (data === "cardboard") {
    element.src = "fourth.png";
  }
});
