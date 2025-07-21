// Chat Controller - Heavy Python-inspired JavaScript Automation

class ChatController {
    constructor() {
        this.conversations = this.setupConversations();
        this.currentConversation = 0;
        this.messageIndex = 0;
        this.isRunning = false;
        this.typingSpeed = 50; // milliseconds per character
        this.messageDelay = 2000; // milliseconds between messages
        this.conversationDelay = 5000; // milliseconds between conversations
        
        this.chatArea = document.getElementById('chatArea');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        this.conversationCounter = document.getElementById('conversationCounter');
        
        this.init();
    }

    setupConversations() {
        return [
            // Conversation 1: Enthusiastic startup
            [
                { sender: "bot", message: "🤖 Hej! Välkommen till Axie Studio - Sveriges ledande AI-byrå!" },
                { sender: "bot", message: "Vi hjälper företag att öka produktiviteten med 300% genom intelligenta AI-lösningar! 🚀" },
                { sender: "user", message: "Hej! Det låter fantastiskt. Vi är ett startup som behöver automatisera vår kundservice." },
                { sender: "bot", message: "Perfekt! Startups är våra favoriter! 💡 Vi kan implementera en AI-chatbot som hanterar 80% av era kundförfrågningar automatiskt." },
                { sender: "bot", message: "En av våra startup-kunder minskade sina supportkostnader med 70% på bara 3 veckor! 📊" },
                { sender: "user", message: "Wow! Hur snabbt kan ni implementera något liknande för oss?" },
                { sender: "bot", message: "För startups har vi en speciallösning som kan vara igång på 5 arbetsdagar! ⚡" },
                { sender: "bot", message: "Vill du boka en kostnadsfri 30-minuters demo där jag visar exakt hur det fungerar?" },
                { sender: "user", message: "Ja, absolut! Det låter som precis vad vi behöver." },
                { sender: "bot", message: "Fantastiskt! Jag öppnar vårt bokningssystem så du kan välja en tid som passar. Detta kommer att förändra ert företag! 🎯" },
                { sender: "system", message: "OPEN_BOOKING_MODAL" }
            ],
            
            // Conversation 2: Established company
            [
                { sender: "bot", message: "🤖 Välkommen till Axie Studio! Vi revolutionerar företag med AI-teknik." },
                { sender: "bot", message: "Sedan 2020 har vi hjälpt över 200 företag att automatisera sina processer och öka effektiviteten dramatiskt! 📈" },
                { sender: "user", message: "Hej! Vi är ett etablerat företag med 50 anställda. Kan AI verkligen hjälpa oss?" },
                { sender: "bot", message: "Absolut! Etablerade företag ser ofta de största fördelarna! 🏢 Ni har redan processer som kan optimeras." },
                { sender: "bot", message: "Ett liknande företag sparade 25 timmar per vecka genom att automatisera sin orderhantering med vår AI-lösning." },
                { sender: "user", message: "Det låter intressant. Vilka andra områden kan ni hjälpa med?" },
                { sender: "bot", message: "Vi specialiserar oss på: 📋\n• Intelligent dokumenthantering\n• Automatisk dataanalys\n• Prediktiv underhåll\n• Smart personalplanering" },
                { sender: "bot", message: "Vad säger du om en djupgående konsultation där vi analyserar era specifika behov?" },
                { sender: "user", message: "Ja, det vore värdefullt. När kan vi träffas?" },
                { sender: "bot", message: "Perfekt! Låt mig öppna vårt bokningssystem så du kan välja en tid som passar era scheman. 🗓️" },
                { sender: "system", message: "OPEN_BOOKING_MODAL" }
            ],
            
            // Conversation 3: Skeptical customer
            [
                { sender: "bot", message: "🤖 Hej och välkommen till Axie Studio! Vi gör AI tillgängligt för alla företag." },
                { sender: "bot", message: "Oavsett bransch eller storlek kan vi hjälpa er att dra nytta av AI:s kraft! 💪" },
                { sender: "user", message: "Hej. Jag är lite skeptisk till AI. Är det verkligen värt investeringen?" },
                { sender: "bot", message: "Jag förstår din skepsis helt! 🤔 Många av våra mest nöjda kunder var skeptiska från början." },
                { sender: "bot", message: "Därför erbjuder vi alltid en kostnadsfri analys först. Inga löften - bara konkreta siffror på vad AI kan göra för ert företag." },
                { sender: "user", message: "Okej, det låter rimligt. Men hur vet jag att ni kan leverera?" },
                { sender: "bot", message: "Bra fråga! Vi har en 100% nöjd-kund-garanti. 🛡️ Om ni inte ser resultat inom 30 dagar får ni pengarna tillbaka." },
                { sender: "bot", message: "Plus att vi kan visa er exakt ROI innan ni investerar en krona. Vill du se hur?" },
                { sender: "user", message: "Ja, det skulle övertyga mig. Hur gör vi det?" },
                { sender: "bot", message: "Perfekt! Jag bokar in en ROI-analys där vi räknar på era specifika siffror. Helt kostnadsfritt! 📊" },
                { sender: "system", message: "OPEN_BOOKING_MODAL" }
            ]
        ];
    }

    init() {
        this.startAutomaticDemo();
        this.setupEventListeners();
    }

    setupEventListeners() {
        this.sendButton.addEventListener('click', () => {
            // Disabled during demo
        });
        
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                // Disabled during demo
            }
        });
    }

    startAutomaticDemo() {
        this.isRunning = true;
        this.runConversationLoop();
    }

    async runConversationLoop() {
        while (this.isRunning) {
            for (let convIndex = 0; convIndex < this.conversations.length; convIndex++) {
                this.currentConversation = convIndex;
                this.updateConversationCounter();
                
                // Clear chat for new conversation
                await this.clearChat();
                await this.sleep(1000);
                
                // Run conversation
                const conversation = this.conversations[convIndex];
                for (let msgIndex = 0; msgIndex < conversation.length; msgIndex++) {
                    const { sender, message } = conversation[msgIndex];
                    
                    if (sender === "system" && message === "OPEN_BOOKING_MODAL") {
                        await this.sleep(1500);
                        this.openBookingModal();
                        await this.sleep(10000); // Wait for booking interaction
                        break;
                    } else if (sender === "bot") {
                        await this.showTypingIndicator();
                        await this.sleep(2000);
                        await this.hideTypingIndicator();
                        await this.addMessage(message, true);
                    } else {
                        await this.simulateUserTyping(message);
                        await this.addMessage(message, false);
                    }
                    
                    await this.sleep(this.messageDelay);
                }
                
                // Pause between conversations
                await this.sleep(this.conversationDelay);
            }
        }
    }

    async clearChat() {
        // Fade out existing messages
        const messages = this.chatArea.querySelectorAll('.message');
        messages.forEach(msg => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateY(-20px)';
        });
        
        await this.sleep(500);
        
        // Clear and add welcome message
        this.chatArea.innerHTML = `
            <div class="welcome-message">
                <p>🎯 Automatisk AI-Demo Startar</p>
                <p>Du kommer att se olika kundscenarier som visar hur vår AI-assistent hanterar olika typer av förfrågningar.</p>
            </div>
        `;
    }

    updateConversationCounter() {
        this.conversationCounter.textContent = `Konversation ${this.currentConversation + 1}/${this.conversations.length}`;
    }

    async showTypingIndicator() {
        this.typingIndicator.style.display = 'flex';
        this.scrollToBottom();
    }

    async hideTypingIndicator() {
        this.typingIndicator.style.display = 'none';
    }

    async simulateUserTyping(text) {
        this.messageInput.value = '';
        this.messageInput.focus();
        
        // Simulate realistic typing
        for (let i = 0; i <= text.length; i++) {
            this.messageInput.value = text.substring(0, i);
            
            // Variable typing speed
            let delay = this.typingSpeed;
            if (text[i] === ' ') delay += 100;
            if (text[i] === '.' || text[i] === '!' || text[i] === '?') delay += 200;
            
            await this.sleep(delay);
        }
        
        // Animate send button
        this.animateSendButton();
        await this.sleep(500);
        this.messageInput.value = '';
    }

    animateSendButton() {
        this.sendButton.style.background = '#00cc66';
        this.sendButton.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
            this.sendButton.style.background = '#0066cc';
            this.sendButton.style.transform = 'scale(1)';
        }, 200);
    }

    async addMessage(text, isBot) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isBot ? 'bot' : 'user'}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.textContent = isBot ? '🤖' : '👤';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        
        const timestamp = document.createElement('div');
        timestamp.className = 'message-timestamp';
        timestamp.textContent = new Date().toLocaleTimeString('sv-SE', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        
        if (isBot) {
            messageDiv.appendChild(avatar);
            messageDiv.appendChild(content);
        } else {
            messageDiv.appendChild(content);
            messageDiv.appendChild(avatar);
        }
        
        content.appendChild(timestamp);
        this.chatArea.appendChild(messageDiv);
        
        // Animate text typing
        if (isBot) {
            await this.animateTextTyping(content, text);
        } else {
            content.insertBefore(document.createTextNode(text), timestamp);
        }
        
        this.scrollToBottom();
    }

    async animateTextTyping(element, text) {
        const textNode = document.createTextNode('');
        element.insertBefore(textNode, element.firstChild);
        
        const words = text.split(' ');
        let currentText = '';
        
        for (const word of words) {
            currentText += word + ' ';
            textNode.textContent = currentText.trim();
            
            // Variable delay based on word length
            const delay = word.length * 30 + Math.random() * 200 + 100;
            await this.sleep(delay);
        }
    }

    openBookingModal() {
        // This will be handled by booking-controller.js
        if (window.bookingController) {
            window.bookingController.openModal();
        }
    }

    scrollToBottom() {
        this.chatArea.scrollTop = this.chatArea.scrollHeight;
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize chat controller when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.chatController = new ChatController();
});