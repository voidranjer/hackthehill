const URI = "ws://172.20.10.2:8765";

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

  if (data === "gatorade") {
    element.src = "BottomLeft.png";
  } else if (data === "popcorners") {
    element.src = "BottomRight.png";
  } else if (data === "gingerale") {
    element.src = "Bottom.png";
  }
});
