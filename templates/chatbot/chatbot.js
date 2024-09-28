document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const chatbox = document.getElementById('chatbox');
    const userInput = document.getElementById('user-input');

    sendButton.addEventListener('click', sendMessage);

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessageToChat('user', message);
            getChatbotResponse(message);
            userInput.value = ''; // Clear input field
        }
    }

    function addMessageToChat(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add(sender);
        messageElement.innerText = message;
        chatbox.appendChild(messageElement);
        chatbox.scrollTop = chatbox.scrollHeight; // Scroll to bottom
    }

    function getChatbotResponse(userMessage) {
        const response = 'This is a placeholder response!'; // Replace with AI logic
        setTimeout(() => addMessageToChat('bot', response), 1000); // Simulate delay
    }
});
