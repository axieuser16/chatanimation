class ChatController {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.querySelector('.send-button');
        this.typingIndicator = document.querySelector('.typing-indicator');
        this.isProcessing = false;
        
        // Demo conversation matching Python version
        this.demoConversation = [
            { text: "Hej! Välkommen till Axie Studio! 👋", isBot: true },
            { text: "Vi hjälper företag med AI och chatbot-lösningar.", isBot: true },
            { text: "Hej! Jag är intresserad av era tjänster.", isBot: false },
            { text: "Vad bra! Jag kan hjälpa dig att boka en demo.", isBot: true },
            { text: "Det låter perfekt! När kan vi ses?", isBot: false },
            { text: "Vi har lediga tider nästa vecka. Passar tisdag eller onsdag?", isBot: true },
            { text: "Tisdag skulle fungera bra!", isBot: false },
            { text: "Utmärkt! Jag bokar in dig på tisdag kl 10:00. Du kommer få en kalenderinbjudan inom kort.", isBot: true },
            { text: "Tack så mycket! Ser fram emot mötet.", isBot: false },
            { text: "Tack själv! Vi ses på tisdag. Ha en fin dag! 😊", isBot: true }
        ];
        
        // Start the demo automatically
        this.startDemo();
    }

    async startDemo() {
        while (true) {
            // Clear previous messages
            this.chatMessages.innerHTML = '<div class="typing-indicator"><span></span><span></span><span></span></div>';
            this.typingIndicator = document.querySelector('.typing-indicator');
            
            // Run through demo conversation
            for (const message of this.demoConversation) {
                if (message.isBot) {
                    // Show typing indicator for bot messages
                    await this.showTypingIndicator();
                    await this.delay(1500);
                    await this.hideTypingIndicator();
                } else {
                    // Simulate user typing
                    await this.simulateUserTyping(message.text);
                }
                
                await this.addMessage(message.text, message.isBot);
                await this.delay(1000);
            }
            
            // Pause before restarting
            await this.delay(3000);
        }
    }

    async simulateUserTyping(text) {
        this.messageInput.value = '';
        const words = text.split(' ');
        
        for (const word of words) {
            this.messageInput.value += word + ' ';
            await this.delay(200);
        }
        
        // Simulate send button click
        this.sendButton.style.transform = 'scale(1.1)';
        await this.delay(200);
        this.sendButton.style.transform = 'scale(0.95)';
        await this.delay(100);
        this.sendButton.style.transform = 'scale(1)';
        this.messageInput.value = '';
    }

    async addMessage(text, isBot) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
        
        // Create message content
        const contentSpan = document.createElement('span');
        messageDiv.appendChild(contentSpan);
        
        // Add timestamp
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString('sv-SE', {
            hour: '2-digit',
            minute: '2-digit'
        });
        messageDiv.appendChild(timeDiv);
        
        this.chatMessages.appendChild(messageDiv);
        
        // Animate text appearance
        await this.typeText(contentSpan, text);
        
        // Scroll to new message
        this.smoothScrollToBottom();
    }

    async typeText(element, text) {
        const words = text.split(' ');
        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            if (i > 0) element.textContent += ' ';
            
            // Type each character in the word
            for (let char of word) {
                element.textContent += char;
                await this.delay(30);
            }
        }
    }

    async showTypingIndicator() {
        this.typingIndicator.classList.add('active');
        this.smoothScrollToBottom();
        
        // Animate typing dots
        const dots = this.typingIndicator.querySelectorAll('span');
        for (let i = 0; i < 3; i++) {
            dots[i].style.animation = 'typingBounce 1s infinite';
            dots[i].style.animationDelay = `${i * 0.2}s`;
        }
    }

    async hideTypingIndicator() {
        this.typingIndicator.classList.remove('active');
    }

    smoothScrollToBottom() {
        const target = this.chatMessages.scrollHeight - this.chatMessages.clientHeight;
        this.chatMessages.scrollTo({
            top: target,
            behavior: 'smooth'
        });
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize chat controller when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.chatController = new ChatController();
});