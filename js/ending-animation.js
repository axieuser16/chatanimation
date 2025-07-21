// Ending Animation Controller

class EndingAnimation {
    constructor() {
        this.isPlaying = false;
        this.init();
    }

    init() {
        // Listen for booking completion
        document.addEventListener('bookingCompleted', () => {
            this.playEndingAnimation();
        });
    }

    playEndingAnimation() {
        if (this.isPlaying) return;
        this.isPlaying = true;

        // Create celebration overlay
        this.createCelebrationOverlay();
        
        // Play confetti animation
        this.playConfetti();
        
        // Show final message
        setTimeout(() => {
            this.showFinalMessage();
        }, 2000);
    }

    createCelebrationOverlay() {
        const overlay = document.createElement('div');
        overlay.id = 'celebrationOverlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, #0066cc, #00cc66);
            z-index: 9999;
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.5s ease;
        `;

        document.body.appendChild(overlay);

        setTimeout(() => {
            overlay.style.opacity = '0.9';
        }, 10);
    }

    playConfetti() {
        const colors = ['#ff6b35', '#f7931e', '#ffd700', '#00cc66', '#0066cc'];
        
        for (let i = 0; i < 50; i++) {
            setTimeout(() => {
                this.createConfettiPiece(colors[Math.floor(Math.random() * colors.length)]);
            }, i * 50);
        }
    }

    createConfettiPiece(color) {
        const confetti = document.createElement('div');
        confetti.style.cssText = `
            position: fixed;
            width: 10px;
            height: 10px;
            background: ${color};
            top: -10px;
            left: ${Math.random() * 100}%;
            z-index: 10000;
            border-radius: 50%;
            animation: confettiFall 3s linear forwards;
        `;

        document.body.appendChild(confetti);

        // Remove after animation
        setTimeout(() => {
            if (confetti.parentNode) {
                confetti.parentNode.removeChild(confetti);
            }
        }, 3000);
    }

    showFinalMessage() {
        const overlay = document.getElementById('celebrationOverlay');
        if (!overlay) return;

        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div style="font-size: 64px; margin-bottom: 20px;">🎉</div>
                <h1 style="font-size: 32px; margin-bottom: 20px;">Grattis!</h1>
                <p style="font-size: 18px; margin-bottom: 30px;">Du har precis sett kraften i AI-automation!</p>
                <div style="font-size: 14px; opacity: 0.9;">
                    <p>✅ Automatisk kundinteraktion</p>
                    <p>✅ Intelligent bokningssystem</p>
                    <p>✅ Smidig användarupplevelse</p>
                </div>
                <button id="restartDemo" style="
                    margin-top: 30px;
                    padding: 15px 30px;
                    background: white;
                    color: #0066cc;
                    border: none;
                    border-radius: 25px;
                    font-size: 16px;
                    font-weight: bold;
                    cursor: pointer;
                    transition: all 0.3s ease;
                ">🔄 Starta Om Demo</button>
            </div>
        `;

        // Add restart functionality
        document.getElementById('restartDemo').addEventListener('click', () => {
            this.restartDemo();
        });
    }

    restartDemo() {
        // Remove celebration overlay
        const overlay = document.getElementById('celebrationOverlay');
        if (overlay) {
            overlay.style.opacity = '0';
            setTimeout(() => {
                if (overlay.parentNode) {
                    overlay.parentNode.removeChild(overlay);
                }
            }, 500);
        }

        // Reset demo state
        this.isPlaying = false;
        
        // Restart chat controller
        if (window.chatController) {
            window.chatController.startAutomaticDemo();
        }
    }
}

// Add confetti animation CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes confettiFall {
        0% {
            transform: translateY(-100vh) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new EndingAnimation();
});