const chatForm = document.getElementById("chat-form");
const chatBody = document.getElementById("chat-body");

chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const userMessage = document.getElementById("user-message").value;
    addMessage("user", userMessage);
    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ user_message: userMessage }),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => response.json())
        .then((data) => addMessage("bot", data.bot_message));
    document.getElementById("user-message").value = "";
});

function addMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message");
    if (sender === "user") {
        messageDiv.classList.add("user-message");
    } else {
        messageDiv.classList.add("bot-message");
    }
    messageDiv.innerHTML = `<p>${message}</p>`;
    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}
