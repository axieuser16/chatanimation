// Paper Plane Animation for Send Button

class PaperPlaneAnimation {
    constructor() {
        this.sendButton = document.getElementById('sendButton');
        this.init();
    }

    init() {
        this.setupSendButtonAnimation();
    }

    setupSendButtonAnimation() {
        this.sendButton.addEventListener('click', () => {
            this.animatePaperPlane();
        });
    }

    animatePaperPlane() {
        // Create paper plane element
        const plane = document.createElement('div');
        plane.innerHTML = '✈️';
        plane.style.cssText = `
            position: absolute;
            font-size: 20px;
            pointer-events: none;
            z-index: 1000;
            transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        `;

        // Get button position
        const buttonRect = this.sendButton.getBoundingClientRect();
        plane.style.left = buttonRect.left + 'px';
        plane.style.top = buttonRect.top + 'px';

        document.body.appendChild(plane);

        // Animate plane flying
        setTimeout(() => {
            plane.style.transform = 'translateX(-200px) translateY(-100px) rotate(45deg)';
            plane.style.opacity = '0';
        }, 10);

        // Remove plane after animation
        setTimeout(() => {
            if (plane.parentNode) {
                plane.parentNode.removeChild(plane);
            }
        }, 800);

        // Button feedback
        this.sendButton.style.transform = 'scale(0.9)';
        this.sendButton.style.background = '#00cc66';
        
        setTimeout(() => {
            this.sendButton.style.transform = 'scale(1)';
            this.sendButton.style.background = '#0066cc';
        }, 200);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PaperPlaneAnimation();
});