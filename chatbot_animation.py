import tkinter as tk
from tkinter import ttk, font
import time
import threading
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import math
from datetime import datetime, timedelta
import calendar

class BookingModal:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Boka Tid - Axie Studio")
        
        # Configure the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 500
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Set window style
        self.window.configure(bg='white')
        self.window.attributes('-alpha', 0.0)  # Start fully transparent
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=10)
        
        self.setup_ui()
        self.animate_appear()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.window, bg='#0066cc', height=60)
        header.pack(fill=tk.X, pady=0)
        header.pack_propagate(False)
        
        tk.Label(header, text="🎯 Boka Din AI-Konsultation", font=self.title_font,
                bg='#0066cc', fg='white').pack(pady=15)

        # Main content
        content = tk.Frame(self.window, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Welcome message
        welcome_frame = tk.Frame(content, bg='#f0f8ff', relief=tk.RAISED, bd=1)
        welcome_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(welcome_frame, text="🚀 Upptäck hur AI kan revolutionera ditt företag!", 
                font=self.header_font, bg='#f0f8ff', fg='#0066cc').pack(pady=10)
        tk.Label(welcome_frame, text="Välj en tid som passar dig bäst:", 
                font=self.normal_font, bg='#f0f8ff').pack(pady=(0,10))

        # Calendar section
        self.setup_calendar(content)
        
        # Time slots section
        self.setup_time_slots(content)
        
        # Contact info
        self.setup_contact_form(content)
        
        # Confirmation button
        self.confirm_button = tk.Button(content, text="🎉 Bekräfta Min Bokning",
                                      font=self.header_font, bg='#00cc66', fg='white',
                                      command=self.confirm_booking, relief=tk.FLAT)
        self.confirm_button.pack(pady=20, ipady=12, ipadx=30)

    def setup_calendar(self, parent):
        calendar_frame = tk.Frame(parent, bg='white')
        calendar_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(calendar_frame, text="📅 Välj Datum", font=self.header_font,
                bg='white', fg='#333').pack(anchor='w')
        
        # Month navigation
        nav_frame = tk.Frame(calendar_frame, bg='white')
        nav_frame.pack(fill=tk.X, pady=5)
        
        self.current_date = datetime.now()
        
        tk.Button(nav_frame, text="◀", command=self.prev_month, 
                 bg='#0066cc', fg='white', font=self.normal_font).pack(side=tk.LEFT)
        self.month_label = tk.Label(nav_frame, text=self.current_date.strftime("%B %Y"),
                                  font=self.header_font, bg='white')
        self.month_label.pack(side=tk.LEFT, expand=True)
        tk.Button(nav_frame, text="▶", command=self.next_month,
                 bg='#0066cc', fg='white', font=self.normal_font).pack(side=tk.RIGHT)
        
        # Calendar grid
        self.calendar_grid = tk.Frame(calendar_frame, bg='white')
        self.calendar_grid.pack(pady=10)
        self.update_calendar()

    def setup_time_slots(self, parent):
        time_frame = tk.Frame(parent, bg='white')
        time_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(time_frame, text="⏰ Tillgängliga Tider", font=self.header_font,
                bg='white', fg='#333').pack(anchor='w')
        
        times = ["09:00 - Morgonmöte", "10:30 - Förmiddagssamtal", "13:00 - Lunchmöte", 
                "14:30 - Eftermiddagssamtal", "16:00 - Kvällsmöte"]
        
        slots_frame = tk.Frame(time_frame, bg='white')
        slots_frame.pack(fill=tk.X, pady=5)
        
        for i, time in enumerate(times):
            btn = tk.Button(slots_frame, text=time, font=self.normal_font,
                          bg='#e6f0ff', fg='#0066cc', width=25, relief=tk.FLAT)
            btn.pack(pady=2, fill=tk.X)
            btn.bind('<Button-1>', lambda e, t=time: self.select_time(t))

    def setup_contact_form(self, parent):
        form_frame = tk.Frame(parent, bg='white')
        form_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(form_frame, text="📝 Dina Kontaktuppgifter", font=self.header_font,
                bg='white', fg='#333').pack(anchor='w')
        
        # Name field
        tk.Label(form_frame, text="Namn:", font=self.normal_font, bg='white').pack(anchor='w')
        self.name_entry = tk.Entry(form_frame, font=self.normal_font, bg='#f8f9fa')
        self.name_entry.pack(fill=tk.X, pady=(2,8))
        
        # Email field
        tk.Label(form_frame, text="E-post:", font=self.normal_font, bg='white').pack(anchor='w')
        self.email_entry = tk.Entry(form_frame, font=self.normal_font, bg='#f8f9fa')
        self.email_entry.pack(fill=tk.X, pady=(2,8))
        
        # Phone field
        tk.Label(form_frame, text="Telefon:", font=self.normal_font, bg='white').pack(anchor='w')
        self.phone_entry = tk.Entry(form_frame, font=self.normal_font, bg='#f8f9fa')
        self.phone_entry.pack(fill=tk.X, pady=(2,8))

    def update_calendar(self):
        # Clear existing calendar
        for widget in self.calendar_grid.winfo_children():
            widget.destroy()
        
        # Add day headers
        days = ["Mån", "Tis", "Ons", "Tor", "Fre", "Lör", "Sön"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_grid, text=day, font=self.normal_font,
                    bg='#0066cc', fg='white', width=4).grid(row=0, column=i, padx=1, pady=1)
        
        # Get calendar for current month
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        
        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.calendar_grid, text=str(day),
                                  font=self.normal_font, width=4, height=2,
                                  bg='#f0f8ff', fg='#333')
                    btn.grid(row=i+1, column=j, padx=1, pady=1)
                    btn.bind('<Button-1>', lambda e, d=day: self.select_date(d))

    def select_date(self, day):
        print(f"📅 Valt datum: {day}/{self.current_date.month}/{self.current_date.year}")

    def select_time(self, time):
        print(f"⏰ Vald tid: {time}")

    def prev_month(self):
        self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
        self.month_label.config(text=self.current_date.strftime("%B %Y"))
        self.update_calendar()

    def next_month(self):
        self.current_date = (self.current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
        self.month_label.config(text=self.current_date.strftime("%B %Y"))
        self.update_calendar()

    def confirm_booking(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        if name and email and phone:
            success_window = tk.Toplevel(self.window)
            success_window.title("Bokning Bekräftad!")
            success_window.geometry("400x200")
            success_window.configure(bg='#00cc66')
            
            tk.Label(success_window, text="🎉 Fantastiskt!", 
                    font=font.Font(size=16, weight="bold"),
                    bg='#00cc66', fg='white').pack(pady=20)
            tk.Label(success_window, text=f"Tack {name}! Din bokning är bekräftad.",
                    font=font.Font(size=12), bg='#00cc66', fg='white').pack()
            tk.Label(success_window, text="Vi skickar en kalenderinbjudan till din e-post.",
                    font=font.Font(size=10), bg='#00cc66', fg='white').pack(pady=10)
            
            tk.Button(success_window, text="Stäng", command=success_window.destroy,
                     bg='white', fg='#00cc66', font=font.Font(weight="bold")).pack(pady=20)
            
            self.window.after(3000, self.animate_disappear)
        else:
            error_label = tk.Label(self.window, text="⚠️ Vänligen fyll i alla fält!",
                                 bg='#ffcccc', fg='#cc0000', font=self.normal_font)
            error_label.pack(pady=5)
            self.window.after(3000, error_label.destroy)

    def animate_appear(self):
        alpha = self.window.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.1
            self.window.attributes('-alpha', alpha)
            self.window.after(30, self.animate_appear)

    def animate_disappear(self):
        alpha = self.window.attributes('-alpha')
        if alpha > 0:
            alpha -= 0.1
            self.window.attributes('-alpha', alpha)
            self.window.after(30, self.animate_disappear)
        else:
            self.window.destroy()

class AnimatedChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Axie Studio AI-Assistent")
        
        # Configure the window
        self.root.configure(bg='#ffffff')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 450
        window_height = 650
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Create custom fonts
        self.custom_font = font.Font(family="Helvetica", size=11)
        self.header_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Initialize colors and styles
        self.colors = {
            'primary': '#0066cc',
            'secondary': '#f8f9fa',
            'text': '#333333',
            'bot_bg': '#0066cc',
            'user_bg': '#e9ecef',
            'bot_text': '#ffffff',
            'user_text': '#333333',
            'success': '#00cc66'
        }
        
        self.setup_ui()
        self.setup_enhanced_conversation()
        
        # Maximum visible messages (rest will fade)
        self.max_visible_messages = 6
        self.current_message_index = 0
        
        # Start the automatic demo
        self.start_automatic_demo()

    def setup_ui(self):
        # Header Frame with gradient effect
        self.header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        self.header_frame.pack(fill=tk.X, pady=0)
        self.header_frame.pack_propagate(False)
        
        # Load and display logo
        try:
            logo_url = "https://www.axiestudio.se/logo.jpg"
            logo_response = requests.get(logo_url, timeout=5)
            logo_image = Image.open(BytesIO(logo_response.content))
            logo_image = logo_image.resize((50, 50), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = tk.Label(self.header_frame, image=self.logo_photo, bg=self.colors['primary'])
            self.logo_label.pack(side=tk.LEFT, padx=15, pady=15)
        except:
            self.logo_label = tk.Label(self.header_frame, text="🤖", font=font.Font(size=24), 
                                     bg=self.colors['primary'], fg='white')
            self.logo_label.pack(side=tk.LEFT, padx=15, pady=15)

        # Header text with enhanced styling
        header_text = tk.Frame(self.header_frame, bg=self.colors['primary'])
        header_text.pack(side=tk.LEFT, padx=10, pady=15)
        
        tk.Label(header_text, text="Axie Studio AI-Assistent", font=self.header_font,
                bg=self.colors['primary'], fg='white').pack(anchor='w')
        tk.Label(header_text, text="🟢 Online • Redo att revolutionera ditt företag", 
                font=self.small_font, bg=self.colors['primary'], fg='#ccddff').pack(anchor='w')

        # Chat display with enhanced canvas
        self.chat_frame = tk.Frame(self.root, bg='#f8f9fa')
        self.chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.canvas = tk.Canvas(self.chat_frame, bg='#f8f9fa', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.chat_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#f8f9fa')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        self.scrollable_frame.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Enhanced typing indicator
        self.typing_frame = tk.Frame(self.scrollable_frame, bg='#f8f9fa')
        self.typing_label = tk.Label(self.typing_frame, text="AI-assistenten skriver", 
                                   font=self.small_font, bg='#f8f9fa', fg='#666')
        self.typing_label.pack(side=tk.LEFT, padx=10)
        
        self.typing_dots = []
        for _ in range(3):
            dot = tk.Label(self.typing_frame, text="●", font=("Helvetica", 16), 
                          bg='#f8f9fa', fg=self.colors['primary'])
            dot.pack(side=tk.LEFT, padx=1)
            self.typing_dots.append(dot)

        # Enhanced input area
        self.input_frame = tk.Frame(self.root, bg='white', height=60)
        self.input_frame.pack(fill=tk.X, pady=(0, 15), padx=15)
        self.input_frame.pack_propagate(False)
        
        # Input field with placeholder effect
        self.message_var = tk.StringVar()
        self.input_field = tk.Entry(self.input_frame, textvariable=self.message_var,
                                  font=self.custom_font, bg='#f8f9fa', relief=tk.FLAT,
                                  bd=10)
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 15), pady=10)
        
        # Enhanced send button
        self.send_button = tk.Button(self.input_frame, text="🚀 Skicka", font=self.custom_font,
                                   bg=self.colors['primary'], fg='white', relief=tk.FLAT,
                                   bd=0, padx=20)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def setup_enhanced_conversation(self):
        """Enhanced conversation that builds excitement and leads to booking"""
        self.demo_conversation = [
            ("bot", "🤖 Hej och välkommen till Axie Studio! Jag är din AI-assistent."),
            ("bot", "Vi hjälper företag att implementera kraftfulla AI-lösningar som ökar produktiviteten med upp till 300%! 🚀"),
            ("user", "Hej! Det låter intressant. Vad kan ni hjälpa mitt företag med?"),
            ("bot", "Fantastisk fråga! Vi specialiserar oss på:\n\n🤖 Intelligenta chatbots\n📊 AI-driven dataanalys\n⚡ Automatisering av affärsprocesser\n💡 Skräddarsydda AI-lösningar"),
            ("user", "Wow, det låter som precis vad vi behöver! Kan ni ge konkreta exempel?"),
            ("bot", "Absolut! En av våra kunder ökade sin kundservice-effektivitet med 250% och minskade svarstider från 24 timmar till 2 minuter! 📈"),
            ("bot", "En annan kund automatiserade hela sin orderprocess och sparar nu 40 timmar per vecka. Tänk vad du kunde göra med den tiden! ⏰"),
            ("user", "Det är ju otroligt! Hur snabbt kan ni implementera något liknande för oss?"),
            ("bot", "Vi kan ha en grundlösning igång på bara 2-3 veckor! Men först skulle jag vilja förstå era specifika behov bättre. 🎯"),
            ("bot", "Vad säger du om en kostnadsfri 30-minuters konsultation där vi kan diskutera era utmaningar och visa konkreta lösningar?"),
            ("user", "Ja, det låter perfekt! När kan vi träffas?"),
            ("bot", "Utmärkt! Jag öppnar vårt bokningssystem så du kan välja en tid som passar dig bäst. Det här kommer att bli början på något fantastiskt! 🎉"),
            ("system", "OPEN_BOOKING_MODAL")
        ]

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def fade_old_messages(self):
        """Enhanced message fading with better visual effects"""
        messages = [w for w in self.scrollable_frame.winfo_children() 
                   if isinstance(w, tk.Frame) and w != self.typing_frame]
        
        if len(messages) > self.max_visible_messages:
            for i, msg in enumerate(messages[:-self.max_visible_messages]):
                self.fade_widget(msg, fade_level=min(0.3 + (i * 0.1), 0.8))

    def fade_widget(self, widget, fade_level=0.3):
        """Enhanced widget fading with smooth transitions"""
        try:
            # Calculate faded colors
            bg_value = int(248 + (7 * (1-fade_level)))  # Fade to light gray
            text_value = int(51 + (150 * (1-fade_level)))  # Fade text
            
            widget.configure(bg=f'#{bg_value:02x}{bg_value:02x}{bg_value:02x}')
            
            for child in widget.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(fg=f'#{text_value:02x}{text_value:02x}{text_value:02x}')
        except:
            pass  # Handle any color conversion errors gracefully

    def add_message(self, text, is_bot, animate_typing=True):
        """Enhanced message addition with better animations"""
        # Create message bubble with enhanced styling
        bubble_frame = tk.Frame(self.scrollable_frame, bg='#f8f9fa')
        bubble_frame.pack(anchor='w' if is_bot else 'e', padx=15, pady=8, fill=tk.X)
        
        # Message container with rounded corners effect
        message_container = tk.Frame(bubble_frame, bg='#f8f9fa')
        message_container.pack(anchor='w' if is_bot else 'e')
        
        # Enhanced message styling
        message = tk.Label(message_container, text="", font=self.custom_font, wraplength=300,
                         bg=self.colors['bot_bg'] if is_bot else self.colors['user_bg'],
                         fg=self.colors['bot_text'] if is_bot else self.colors['user_text'],
                         justify=tk.LEFT, padx=15, pady=12, relief=tk.FLAT)
        message.pack(anchor='w' if is_bot else 'e')
        
        # Add emoji indicator for bot messages
        if is_bot:
            emoji_label = tk.Label(message_container, text="🤖", font=self.small_font,
                                 bg='#f8f9fa', fg=self.colors['primary'])
            emoji_label.pack(anchor='w', padx=15, pady=(0, 5))
        
        # Enhanced typing animation
        if animate_typing:
            words = text.split(' ')
            current_text = ""
            
            for word in words:
                current_text += word + " "
                message.configure(text=current_text.strip())
                self.root.update()
                time.sleep(0.1)  # Faster typing for better flow
        else:
            message.configure(text=text)
        
        # Add timestamp
        timestamp = tk.Label(message_container, 
                           text=datetime.now().strftime("%H:%M"),
                           font=font.Font(size=8), bg='#f8f9fa', fg='#999')
        timestamp.pack(anchor='e' if is_bot else 'w', padx=15, pady=(2, 5))
        
        # Fade old messages
        self.fade_old_messages()
        
        # Keep typing indicator at bottom
        self.typing_frame.pack_forget()
        self.typing_frame.pack(anchor='w', padx=15, pady=5)
        
        # Enhanced scroll to bottom
        self.root.after(100, lambda: self.canvas.yview_moveto(1.0))

    def simulate_user_typing(self, text):
        """Enhanced user typing simulation"""
        self.message_var.set("")
        
        # Simulate realistic typing with pauses
        words = text.split(' ')
        for i, word in enumerate(words):
            if i > 0:
                self.message_var.set(self.message_var.get() + " ")
            
            for char in word:
                self.message_var.set(self.message_var.get() + char)
                self.root.update()
                time.sleep(0.08)  # Realistic typing speed
            
            # Pause between words
            if i < len(words) - 1:
                time.sleep(0.2)
        
        # Simulate send button press
        self.animate_send_button()
        time.sleep(0.5)
        self.message_var.set("")

    def animate_send_button(self):
        """Animate send button press"""
        original_bg = self.send_button.cget('bg')
        self.send_button.configure(bg=self.colors['success'])
        self.root.update()
        time.sleep(0.2)
        self.send_button.configure(bg=original_bg)

    def animate_typing_dots(self):
        """Enhanced typing indicator animation"""
        def animate():
            while True:
                for i, dot in enumerate(self.typing_dots):
                    dot.configure(fg=self.colors['primary'])
                    time.sleep(0.15)
                    self.root.update()
                
                for dot in self.typing_dots:
                    dot.configure(fg='#cccccc')
                    time.sleep(0.1)
                    self.root.update()
                
                time.sleep(0.5)  # Pause between cycles
        
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()

    def start_automatic_demo(self):
        """Enhanced automatic demo with better pacing"""
        def demo_loop():
            while True:
                # Clear previous messages with fade effect
                for widget in list(self.scrollable_frame.winfo_children()):
                    if widget != self.typing_frame:
                        self.fade_widget(widget, 0.0)
                        self.root.after(100, widget.destroy)
                
                time.sleep(1)
                self.root.update()
                
                # Start enhanced typing indicator
                self.animate_typing_dots()
                
                # Run through enhanced conversation
                for sender, message in self.demo_conversation:
                    if sender == "system" and message == "OPEN_BOOKING_MODAL":
                        time.sleep(1.5)
                        self.root.after(0, lambda: BookingModal(self.root))
                        time.sleep(8)  # Wait longer for booking interaction
                        break
                    elif sender == "bot":
                        # Show typing indicator for bot messages
                        self.typing_frame.pack(anchor='w', padx=15, pady=5)
                        time.sleep(2)  # Longer thinking time
                        self.typing_frame.pack_forget()
                        self.add_message(message, True)
                    else:
                        # Simulate user typing
                        self.simulate_user_typing(message)
                        self.add_message(message, False, animate_typing=False)
                    
                    time.sleep(2)  # Better pacing between messages
                
                time.sleep(5)  # Longer pause before restarting

        # Start enhanced demo in separate thread
        demo_thread = threading.Thread(target=demo_loop, daemon=True)
        demo_thread.start()

def main():
    root = tk.Tk()
    
    # Enhanced window styling
    root.configure(bg='#f8f9fa')
    root.resizable(True, True)
    
    # Set window icon (if available)
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    app = AnimatedChatbot(root)
    
    # Center window on screen
    root.update_idletasks()
    root.mainloop()

if __name__ == "__main__":
    main()