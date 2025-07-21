// Booking Controller - Advanced Modal Management

class BookingController {
    constructor() {
        this.modal = document.getElementById('bookingModal');
        this.successModal = document.getElementById('successModal');
        this.selectedDate = null;
        this.selectedTime = null;
        this.bookingData = {};
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.generateDateOptions();
        this.setupAutoPopulation();
    }

    setupEventListeners() {
        // Close modal when clicking outside
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) {
                this.closeModal();
            }
        });

        // Booking confirmation
        document.getElementById('confirmBooking').addEventListener('click', () => {
            this.confirmBooking();
        });

        // Secondary buttons
        document.getElementById('callInstead').addEventListener('click', () => {
            this.showContactInfo();
        });

        document.getElementById('cancelBooking').addEventListener('click', () => {
            this.closeModal();
        });

        // Success modal close
        document.getElementById('closeSuccess').addEventListener('click', () => {
            this.closeSuccessModal();
        });

        // Date selection
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('date-option')) {
                this.selectDate(e.target);
            }
        });

        // Time selection
        document.addEventListener('click', (e) => {
            if (e.target.closest('.time-slot')) {
                this.selectTime(e.target.closest('.time-slot'));
            }
        });
    }

    generateDateOptions() {
        const dateContainer = document.getElementById('dateOptions');
        const today = new Date();
        const businessDays = [];
        let currentDate = new Date(today);
        currentDate.setDate(currentDate.getDate() + 1);

        // Generate next 5 business days
        while (businessDays.length < 5) {
            if (currentDate.getDay() >= 1 && currentDate.getDay() <= 5) {
                businessDays.push(new Date(currentDate));
            }
            currentDate.setDate(currentDate.getDate() + 1);
        }

        businessDays.forEach((date, index) => {
            const dateOption = document.createElement('div');
            dateOption.className = 'date-option';
            dateOption.dataset.date = date.toISOString();
            
            const dayName = date.toLocaleDateString('sv-SE', { weekday: 'long' });
            const dateStr = date.toLocaleDateString('sv-SE', { day: 'numeric', month: 'long' });
            
            dateOption.innerHTML = `
                <strong>${dayName}</strong>
                <span>${dateStr}</span>
            `;
            
            dateContainer.appendChild(dateOption);
            
            // Animate appearance
            setTimeout(() => {
                dateOption.style.opacity = '1';
                dateOption.style.transform = 'translateY(0)';
            }, index * 200);
        });
    }

    setupAutoPopulation() {
        // Auto-populate demo data after a delay
        setTimeout(() => {
            this.autoPopulateForm();
        }, 3000);
    }

    autoPopulateForm() {
        const demoData = {
            nameField: 'Anna Andersson',
            emailField: 'anna.andersson@företag.se',
            phoneField: '070-123 45 67',
            companyField: 'Innovativa Lösningar AB',
            positionField: 'VD'
        };

        Object.entries(demoData).forEach(([fieldId, value], index) => {
            setTimeout(() => {
                const field = document.getElementById(fieldId);
                if (field) {
                    this.typeInField(field, value);
                }
            }, index * 500);
        });
    }

    async typeInField(field, text) {
        field.focus();
        field.value = '';
        
        for (let i = 0; i <= text.length; i++) {
            field.value = text.substring(0, i);
            await this.sleep(50);
        }
        
        field.blur();
    }

    openModal() {
        this.modal.style.display = 'flex';
        this.modal.style.opacity = '0';
        
        // Animate modal appearance
        setTimeout(() => {
            this.modal.style.opacity = '1';
        }, 10);
        
        // Auto-select first date and time for demo
        setTimeout(() => {
            this.autoSelectDateTime();
        }, 2000);
    }

    autoSelectDateTime() {
        // Auto-select first date
        const firstDate = document.querySelector('.date-option');
        if (firstDate) {
            this.selectDate(firstDate);
        }
        
        // Auto-select a time after a delay
        setTimeout(() => {
            const timeSlots = document.querySelectorAll('.time-slot');
            if (timeSlots.length > 0) {
                const randomIndex = Math.floor(Math.random() * timeSlots.length);
                this.selectTime(timeSlots[randomIndex]);
            }
        }, 1500);
    }

    selectDate(dateElement) {
        // Remove previous selection
        document.querySelectorAll('.date-option').forEach(el => {
            el.classList.remove('selected');
        });
        
        // Select new date
        dateElement.classList.add('selected');
        this.selectedDate = new Date(dateElement.dataset.date);
        
        // Update progress
        this.updateProgress(25, `Steg 2 av 4: Valt datum ${this.selectedDate.toLocaleDateString('sv-SE', { day: 'numeric', month: 'long' })}`);
        
        console.log('📅 Valt datum:', this.selectedDate.toLocaleDateString('sv-SE'));
    }

    selectTime(timeElement) {
        // Remove previous selection
        document.querySelectorAll('.time-slot').forEach(el => {
            el.classList.remove('selected');
        });
        
        // Select new time
        timeElement.classList.add('selected');
        this.selectedTime = timeElement.dataset.time;
        
        // Update progress
        this.updateProgress(50, `Steg 3 av 4: Vald tid ${this.selectedTime}`);
        
        console.log('⏰ Vald tid:', this.selectedTime);
    }

    updateProgress(percentage, text) {
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');
        
        progressFill.style.width = `${percentage}%`;
        progressText.textContent = text;
    }

    confirmBooking() {
        // Validate required fields
        const requiredFields = ['nameField', 'emailField', 'companyField'];
        const missingFields = [];
        
        requiredFields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (!field.value.trim()) {
                missingFields.push(fieldId);
            }
        });
        
        if (missingFields.length > 0) {
            alert('Vänligen fyll i alla obligatoriska fält!');
            return;
        }
        
        if (!this.selectedDate || !this.selectedTime) {
            alert('Vänligen välj både datum och tid!');
            return;
        }
        
        // Update progress to 100%
        this.updateProgress(100, 'Bokning bekräftad! 🎉');
        
        // Show success animation
        setTimeout(() => {
            this.showSuccessModal();
        }, 1000);
    }

    showSuccessModal() {
        const name = document.getElementById('nameField').value;
        const dateStr = this.selectedDate.toLocaleDateString('sv-SE', { 
            weekday: 'long', 
            day: 'numeric', 
            month: 'long' 
        });
        
        document.getElementById('successName').textContent = `Tack ${name}!`;
        document.getElementById('successDetails').textContent = 
            `Din AI-konsultation är bokad: ${dateStr} kl ${this.selectedTime}`;
        
        this.successModal.style.display = 'flex';
        this.successModal.style.opacity = '0';
        
        setTimeout(() => {
            this.successModal.style.opacity = '1';
        }, 10);
    }

    closeSuccessModal() {
        this.successModal.style.opacity = '0';
        setTimeout(() => {
            this.successModal.style.display = 'none';
            this.closeModal();
        }, 300);
    }

    showContactInfo() {
        alert(`📞 Kontakta Oss\n\nTelefon: 08-123 456 78\nE-post: info@axiestudio.se\nWebb: www.axiestudio.se\n\nVi svarar inom 2 timmar!`);
    }

    closeModal() {
        this.modal.style.opacity = '0';
        setTimeout(() => {
            this.modal.style.display = 'none';
        }, 300);
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize booking controller when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.bookingController = new BookingController();
});