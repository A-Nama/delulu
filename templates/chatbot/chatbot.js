document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const userMessage = document.getElementById('user-message');
    const messagesDiv = document.getElementById('messages');

    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const messageText = userMessage.value;
        if (messageText === '') return;

        // Add user's message to chatbox
        const userMessageDiv = document.createElement('div');
        userMessageDiv.textContent = "You: " + messageText;
        messagesDiv.appendChild(userMessageDiv);
        userMessage.value = '';

        // Send message to chatbot and get response
        fetch(chatForm.action, {
            method: 'POST',
            body: new URLSearchParams(new FormData(chatForm)),
        })
        .then(response => response.text())
        .then(botResponse => {
            // Add bot's message to chatbox
            const botMessageDiv = document.createElement('div');
            botMessageDiv.textContent = "Bot: " + botResponse;
            messagesDiv.appendChild(botMessageDiv);
        });
    });
});
