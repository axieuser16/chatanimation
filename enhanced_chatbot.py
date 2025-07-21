#!/usr/bin/env python3
"""
Enhanced Axie Studio Chatbot with Advanced Automation
This version focuses heavily on Python automation with minimal CSS/JS dependencies
"""

import tkinter as tk
from tkinter import ttk, font, messagebox
import time
import threading
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import requests
from io import BytesIO
import math
from datetime import datetime, timedelta
import calendar
import random
import json

class AdvancedBookingModal:
    """Advanced booking modal with enhanced automation and visual effects"""
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("🚀 AI-Powered Booking System - Axie Studio")
        self.parent = parent
        
        # Enhanced window configuration
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 600
        window_height = 700
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Advanced styling
        self.window.configure(bg='white')
        self.window.attributes('-alpha', 0.0)
        self.window.grab_set()  # Make modal
        
        # Enhanced fonts
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=11)
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Color scheme
        self.colors = {
            'primary': '#0066cc',
            'secondary': '#00cc66',
            'accent': '#ff6b35',
            'bg_light': '#f8f9fa',
            'bg_dark': '#343a40',
            'text_light': '#6c757d',
            'text_dark': '#212529'
        }
        
        self.selected_date = None
        self.selected_time = None
        self.booking_data = {}
        
        self.setup_advanced_ui()
        self.start_entrance_animation()
        self.auto_populate_demo_data()

    def setup_advanced_ui(self):
        """Setup advanced UI with multiple sections and animations"""
        
        # Animated header with gradient effect
        self.create_animated_header()
        
        # Main scrollable content
        self.create_scrollable_content()
        
        # Progress indicator
        self.create_progress_indicator()
        
        # Booking steps
        self.create_booking_steps()
        
        # Action buttons
        self.create_action_buttons()

    def create_animated_header(self):
        """Create animated header with gradient background"""
        header = tk.Frame(self.window, bg='#0066cc', height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Animated title
        title_frame = tk.Frame(header, bg='#0066cc')
        title_frame.pack(expand=True, fill=tk.BOTH)
        
        self.title_label = tk.Label(title_frame, text="🎯 Boka Din AI-Transformation", 
                                   font=self.title_font, bg='#0066cc', fg='white')
        self.title_label.pack(pady=20)
        
        self.subtitle_label = tk.Label(title_frame, 
                                      text="Upptäck hur AI kan revolutionera ditt företag på bara 30 minuter",
                                      font=self.normal_font, bg='#0066cc', fg='#ccddff')
        self.subtitle_label.pack()
        
        # Animate header text
        self.animate_header_text()

    def create_scrollable_content(self):
        """Create scrollable content area"""
        # Canvas for scrolling
        self.canvas = tk.Canvas(self.window, bg='white', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.canvas.yview)
        self.content_frame = tk.Frame(self.canvas, bg='white')
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        
        self.content_frame.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

    def create_progress_indicator(self):
        """Create animated progress indicator"""
        progress_frame = tk.Frame(self.content_frame, bg='white', pady=20)
        progress_frame.pack(fill=tk.X, padx=30)
        
        tk.Label(progress_frame, text="📊 Bokningsprocess", font=self.header_font,
                bg='white', fg=self.colors['text_dark']).pack(anchor='w')
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var,
                                          maximum=100, length=400, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=10)
        
        self.progress_label = tk.Label(progress_frame, text="Steg 1 av 4: Välj datum",
                                      font=self.small_font, bg='white', fg=self.colors['text_light'])
        self.progress_label.pack(anchor='w')

    def create_booking_steps(self):
        """Create all booking steps with enhanced styling"""
        
        # Step 1: Date Selection
        self.create_date_selection()
        
        # Step 2: Time Selection  
        self.create_time_selection()
        
        # Step 3: Service Selection
        self.create_service_selection()
        
        # Step 4: Contact Information
        self.create_contact_form()

    def create_date_selection(self):
        """Enhanced date selection with calendar widget"""
        date_frame = tk.Frame(self.content_frame, bg='white', pady=20)
        date_frame.pack(fill=tk.X, padx=30)
        
        tk.Label(date_frame, text="📅 Välj Datum för Din AI-Konsultation", 
                font=self.header_font, bg='white', fg=self.colors['primary']).pack(anchor='w')
        
        tk.Label(date_frame, text="Vi har lediga tider nästa vecka - välj det som passar dig bäst:",
                font=self.normal_font, bg='white', fg=self.colors['text_light']).pack(anchor='w', pady=(5,15))
        
        # Quick date options
        quick_dates_frame = tk.Frame(date_frame, bg='white')
        quick_dates_frame.pack(fill=tk.X, pady=10)
        
        # Generate next 5 business days
        today = datetime.now()
        business_days = []
        current_date = today + timedelta(days=1)
        
        while len(business_days) < 5:
            if current_date.weekday() < 5:  # Monday to Friday
                business_days.append(current_date)
            current_date += timedelta(days=1)
        
        for i, date in enumerate(business_days):
            date_btn = tk.Button(quick_dates_frame, 
                               text=f"{date.strftime('%A')}\n{date.strftime('%d %B')}",
                               font=self.normal_font, bg=self.colors['bg_light'], 
                               fg=self.colors['text_dark'], width=12, height=3,
                               relief=tk.FLAT, bd=2,
                               command=lambda d=date: self.select_date(d))
            date_btn.grid(row=0, column=i, padx=5, pady=5)
            
            # Auto-animate button appearance
            self.window.after(i * 200, lambda btn=date_btn: self.animate_button_appear(btn))

    def create_time_selection(self):
        """Enhanced time selection with availability indicators"""
        time_frame = tk.Frame(self.content_frame, bg='white', pady=20)
        time_frame.pack(fill=tk.X, padx=30)
        
        tk.Label(time_frame, text="⏰ Välj Tid som Passar Dig", 
                font=self.header_font, bg='white', fg=self.colors['primary']).pack(anchor='w')
        
        tk.Label(time_frame, text="Alla tider är 30 minuter och helt kostnadsfria:",
                font=self.normal_font, bg='white', fg=self.colors['text_light']).pack(anchor='w', pady=(5,15))
        
        # Time slots with availability
        times_data = [
            ("09:00", "Morgonmöte", "🌅", "Perfekt för att starta dagen med AI-inspiration"),
            ("10:30", "Förmiddagssamtal", "☕", "Kaffe och AI - en perfekt kombination"),
            ("13:00", "Lunchmöte", "🍽️", "Diskutera AI över lunch"),
            ("14:30", "Eftermiddagssamtal", "🌞", "Mitt på dagen när hjärnan är skarp"),
            ("16:00", "Kvällsmöte", "🌆", "Avsluta arbetsdagen med framtidstankar")
        ]
        
        for i, (time, title, emoji, description) in enumerate(times_data):
            time_container = tk.Frame(time_frame, bg=self.colors['bg_light'], relief=tk.FLAT, bd=1)
            time_container.pack(fill=tk.X, pady=5)
            
            time_btn = tk.Button(time_container, 
                               text=f"{emoji} {time} - {title}",
                               font=self.normal_font, bg=self.colors['bg_light'],
                               fg=self.colors['text_dark'], anchor='w',
                               relief=tk.FLAT, padx=20, pady=10,
                               command=lambda t=time, title=title: self.select_time(t, title))
            time_btn.pack(fill=tk.X)
            
            tk.Label(time_container, text=description, font=self.small_font,
                    bg=self.colors['bg_light'], fg=self.colors['text_light'],
                    anchor='w').pack(fill=tk.X, padx=20, pady=(0,10))
            
            # Animate appearance
            self.window.after(i * 150, lambda container=time_container: self.animate_button_appear(container))

    def create_service_selection(self):
        """Create service selection with detailed options"""
        service_frame = tk.Frame(self.content_frame, bg='white', pady=20)
        service_frame.pack(fill=tk.X, padx=30)
        
        tk.Label(service_frame, text="🎯 Vad Vill Du Fokusera På?", 
                font=self.header_font, bg='white', fg=self.colors['primary']).pack(anchor='w')
        
        tk.Label(service_frame, text="Välj det område där AI kan ha störst impact för ditt företag:",
                font=self.normal_font, bg='white', fg=self.colors['text_light']).pack(anchor='w', pady=(5,15))
        
        services = [
            ("🤖 Intelligent Kundservice", "Automatisera kundinteraktioner med AI-chatbots", "Spara 40+ timmar/vecka"),
            ("📊 Smart Dataanalys", "Förvandla data till actionable insights", "Öka beslutskvalitet med 200%"),
            ("⚡ Processautomatisering", "Automatisera repetitiva uppgifter", "Frigör tid för strategiskt arbete"),
            ("💡 Skräddarsydd AI-lösning", "Helt anpassad efter dina behov", "Maximal ROI för ditt företag")
        ]
        
        self.service_var = tk.StringVar()
        
        for i, (title, description, benefit) in enumerate(services):
            service_container = tk.Frame(service_frame, bg='white', relief=tk.SOLID, bd=1)
            service_container.pack(fill=tk.X, pady=5)
            
            radio_btn = tk.Radiobutton(service_container, text=title, font=self.normal_font,
                                     variable=self.service_var, value=title,
                                     bg='white', fg=self.colors['text_dark'],
                                     selectcolor=self.colors['primary'], anchor='w')
            radio_btn.pack(fill=tk.X, padx=15, pady=(10,5))
            
            tk.Label(service_container, text=description, font=self.small_font,
                    bg='white', fg=self.colors['text_light'], anchor='w').pack(fill=tk.X, padx=35)
            
            benefit_label = tk.Label(service_container, text=f"💰 {benefit}", 
                                   font=font.Font(size=9, weight="bold"),
                                   bg='white', fg=self.colors['secondary'], anchor='w')
            benefit_label.pack(fill=tk.X, padx=35, pady=(2,10))

    def create_contact_form(self):
        """Enhanced contact form with validation"""
        contact_frame = tk.Frame(self.content_frame, bg='white', pady=20)
        contact_frame.pack(fill=tk.X, padx=30)
        
        tk.Label(contact_frame, text="📝 Dina Kontaktuppgifter", 
                font=self.header_font, bg='white', fg=self.colors['primary']).pack(anchor='w')
        
        tk.Label(contact_frame, text="Vi behöver dessa uppgifter för att skicka kalenderinbjudan:",
                font=self.normal_font, bg='white', fg=self.colors['text_light']).pack(anchor='w', pady=(5,15))
        
        # Form fields with enhanced styling
        fields = [
            ("Namn", "Ditt fullständiga namn"),
            ("E-post", "Din e-postadress för kalenderinbjudan"),
            ("Telefon", "Ditt telefonnummer (valfritt)"),
            ("Företag", "Ditt företags namn"),
            ("Befattning", "Din roll i företaget")
        ]
        
        self.form_entries = {}
        
        for field_name, placeholder in fields:
            field_frame = tk.Frame(contact_frame, bg='white')
            field_frame.pack(fill=tk.X, pady=8)
            
            tk.Label(field_frame, text=f"{field_name}:", font=self.normal_font,
                    bg='white', fg=self.colors['text_dark']).pack(anchor='w')
            
            entry = tk.Entry(field_frame, font=self.normal_font, bg=self.colors['bg_light'],
                           relief=tk.FLAT, bd=5)
            entry.pack(fill=tk.X, pady=(5,0))
            entry.insert(0, placeholder)
            entry.bind('<FocusIn>', lambda e, entry=entry, ph=placeholder: self.on_entry_focus(entry, ph))
            entry.bind('<FocusOut>', lambda e, entry=entry, ph=placeholder: self.on_entry_unfocus(entry, ph))
            
            self.form_entries[field_name] = entry

    def create_action_buttons(self):
        """Create action buttons with enhanced styling"""
        button_frame = tk.Frame(self.content_frame, bg='white', pady=30)
        button_frame.pack(fill=tk.X, padx=30)
        
        # Main booking button
        self.book_button = tk.Button(button_frame, text="🚀 Bekräfta Min AI-Konsultation",
                                   font=font.Font(size=14, weight="bold"),
                                   bg=self.colors['secondary'], fg='white',
                                   relief=tk.FLAT, padx=30, pady=15,
                                   command=self.confirm_booking)
        self.book_button.pack(fill=tk.X, pady=10)
        
        # Secondary buttons
        button_row = tk.Frame(button_frame, bg='white')
        button_row.pack(fill=tk.X, pady=10)
        
        tk.Button(button_row, text="📞 Ring Oss Istället", font=self.normal_font,
                 bg=self.colors['bg_light'], fg=self.colors['text_dark'],
                 relief=tk.FLAT, padx=20, pady=8,
                 command=self.show_contact_info).pack(side=tk.LEFT, padx=(0,10))
        
        tk.Button(button_row, text="❌ Avbryt", font=self.normal_font,
                 bg=self.colors['bg_light'], fg=self.colors['text_dark'],
                 relief=tk.FLAT, padx=20, pady=8,
                 command=self.close_modal).pack(side=tk.RIGHT)

    def auto_populate_demo_data(self):
        """Automatically populate demo data for demonstration"""
        demo_data = {
            "Namn": "Anna Andersson",
            "E-post": "anna.andersson@företag.se", 
            "Telefon": "070-123 45 67",
            "Företag": "Innovativa Lösningar AB",
            "Befattning": "VD"
        }
        
        # Populate after a delay for demo effect
        def populate():
            time.sleep(2)
            for field_name, value in demo_data.items():
                if field_name in self.form_entries:
                    entry = self.form_entries[field_name]
                    entry.delete(0, tk.END)
                    entry.insert(0, value)
                    entry.configure(fg=self.colors['text_dark'])
                    self.window.update()
                    time.sleep(0.3)
        
        threading.Thread(target=populate, daemon=True).start()

    def animate_header_text(self):
        """Animate header text with color transitions"""
        def animate():
            colors = ['#ffffff', '#ccddff', '#99bbff', '#ffffff']
            while True:
                for color in colors:
                    try:
                        self.title_label.configure(fg=color)
                        self.window.update()
                        time.sleep(0.5)
                    except:
                        break
        
        threading.Thread(target=animate, daemon=True).start()

    def animate_button_appear(self, widget):
        """Animate button appearance with scale effect"""
        original_bg = widget.cget('bg')
        widget.configure(bg=self.colors['primary'])
        self.window.update()
        
        def restore():
            time.sleep(0.2)
            try:
                widget.configure(bg=original_bg)
                self.window.update()
            except:
                pass
        
        threading.Thread(target=restore, daemon=True).start()

    def select_date(self, date):
        """Handle date selection with visual feedback"""
        self.selected_date = date
        self.update_progress(25, f"Steg 2 av 4: Valt datum {date.strftime('%d %B')}")
        print(f"📅 Valt datum: {date.strftime('%A, %d %B %Y')}")

    def select_time(self, time, title):
        """Handle time selection with visual feedback"""
        self.selected_time = (time, title)
        self.update_progress(50, f"Steg 3 av 4: Vald tid {time}")
        print(f"⏰ Vald tid: {time} - {title}")

    def update_progress(self, value, text):
        """Update progress bar and text"""
        self.progress_var.set(value)
        self.progress_label.configure(text=text)
        self.window.update()

    def on_entry_focus(self, entry, placeholder):
        """Handle entry field focus"""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.configure(fg=self.colors['text_dark'])

    def on_entry_unfocus(self, entry, placeholder):
        """Handle entry field unfocus"""
        if not entry.get():
            entry.insert(0, placeholder)
            entry.configure(fg=self.colors['text_light'])

    def show_contact_info(self):
        """Show contact information popup"""
        messagebox.showinfo("Kontakta Oss", 
                          "📞 Telefon: 08-123 456 78\n"
                          "📧 E-post: info@axiestudio.se\n"
                          "🌐 Webb: www.axiestudio.se\n\n"
                          "Vi svarar inom 2 timmar!")

    def confirm_booking(self):
        """Enhanced booking confirmation with validation"""
        # Validate required fields
        required_fields = ["Namn", "E-post", "Företag"]
        for field in required_fields:
            entry = self.form_entries[field]
            if not entry.get() or entry.get() in ["Ditt fullständiga namn", "Din e-postadress för kalenderinbjudan", "Ditt företags namn"]:
                messagebox.showerror("Ofullständig Information", 
                                   f"Vänligen fyll i {field.lower()}")
                entry.focus()
                return
        
        if not self.selected_date or not self.selected_time:
            messagebox.showerror("Ofullständig Bokning", 
                               "Vänligen välj både datum och tid")
            return
        
        # Update progress
        self.update_progress(100, "Bokning bekräftad! 🎉")
        
        # Show success animation
        self.show_success_animation()

    def show_success_animation(self):
        """Show animated success confirmation"""
        success_window = tk.Toplevel(self.window)
        success_window.title("Bokning Bekräftad!")
        success_window.geometry("500x400")
        success_window.configure(bg='#00cc66')
        success_window.attributes('-alpha', 0.0)
        
        # Center the success window
        success_window.transient(self.window)
        success_window.grab_set()
        
        # Success content
        tk.Label(success_window, text="🎉", font=font.Font(size=48),
                bg='#00cc66', fg='white').pack(pady=30)
        
        tk.Label(success_window, text="Fantastiskt!", 
                font=font.Font(size=20, weight="bold"),
                bg='#00cc66', fg='white').pack()
        
        name = self.form_entries["Namn"].get()
        tk.Label(success_window, text=f"Tack {name}!", 
                font=font.Font(size=16),
                bg='#00cc66', fg='white').pack(pady=10)
        
        date_str = self.selected_date.strftime('%A, %d %B')
        time_str = self.selected_time[0]
        
        tk.Label(success_window, 
                text=f"Din AI-konsultation är bokad:\n{date_str} kl {time_str}",
                font=font.Font(size=12), bg='#00cc66', fg='white',
                justify=tk.CENTER).pack(pady=20)
        
        tk.Label(success_window, 
                text="📧 Kalenderinbjudan skickas inom 5 minuter\n"
                     "📞 Vi ringer 5 minuter före mötet\n"
                     "🚀 Förbered dig på en fantastisk AI-resa!",
                font=font.Font(size=10), bg='#00cc66', fg='white',
                justify=tk.CENTER).pack(pady=20)
        
        tk.Button(success_window, text="Perfekt! Stäng", 
                 font=font.Font(size=12, weight="bold"),
                 bg='white', fg='#00cc66', padx=30, pady=10,
                 command=lambda: [success_window.destroy(), self.close_modal()]).pack(pady=30)
        
        # Animate success window appearance
        def animate_success():
            alpha = 0.0
            while alpha < 1.0:
                alpha += 0.1
                try:
                    success_window.attributes('-alpha', alpha)
                    time.sleep(0.05)
                except:
                    break
        
        threading.Thread(target=animate_success, daemon=True).start()

    def start_entrance_animation(self):
        """Animate modal entrance"""
        def animate():
            alpha = 0.0
            while alpha < 1.0:
                alpha += 0.1
                try:
                    self.window.attributes('-alpha', alpha)
                    time.sleep(0.05)
                except:
                    break
        
        threading.Thread(target=animate, daemon=True).start()

    def close_modal(self):
        """Close modal with exit animation"""
        def animate_exit():
            alpha = 1.0
            while alpha > 0:
                alpha -= 0.1
                try:
                    self.window.attributes('-alpha', alpha)
                    time.sleep(0.03)
                except:
                    break
            try:
                self.window.destroy()
            except:
                pass
        
        threading.Thread(target=animate_exit, daemon=True).start()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

class SuperAutomatedChatbot:
    """Super automated chatbot with advanced Python features and minimal CSS/JS"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Axie Studio AI-Assistent - Automatisk Demo")
        
        # Enhanced window configuration
        self.root.configure(bg='#f0f2f5')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 500
        window_height = 700
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Advanced fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.message_font = font.Font(family="Helvetica", size=11)
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Enhanced color scheme
        self.colors = {
            'primary': '#0066cc',
            'secondary': '#00cc66', 
            'accent': '#ff6b35',
            'bot_bg': '#0066cc',
            'user_bg': '#e3f2fd',
            'bot_text': '#ffffff',
            'user_text': '#1565c0',
            'bg_main': '#f0f2f5',
            'bg_chat': '#ffffff',
            'text_primary': '#212529',
            'text_secondary': '#6c757d'
        }
        
        # Conversation state
        self.current_conversation = 0
        self.message_index = 0
        self.is_demo_running = False
        self.conversations = self.setup_multiple_conversations()
        
        # UI Setup
        self.setup_advanced_ui()
        self.setup_auto_features()
        
        # Start super automation
        self.start_super_automation()

    def setup_multiple_conversations(self):
        """Setup multiple conversation scenarios for variety"""
        return [
            # Conversation 1: Enthusiastic startup
            [
                ("bot", "🤖 Hej! Välkommen till Axie Studio - Sveriges ledande AI-byrå!"),
                ("bot", "Vi hjälper företag att öka produktiviteten med 300% genom intelligenta AI-lösningar! 🚀"),
                ("user", "Hej! Det låter fantastiskt. Vi är ett startup som behöver automatisera vår kundservice."),
                ("bot", "Perfekt! Startups är våra favoriter! 💡 Vi kan implementera en AI-chatbot som hanterar 80% av era kundförfrågningar automatiskt."),
                ("bot", "En av våra startup-kunder minskade sina supportkostnader med 70% på bara 3 veckor! 📊"),
                ("user", "Wow! Hur snabbt kan ni implementera något liknande för oss?"),
                ("bot", "För startups har vi en speciallösning som kan vara igång på 5 arbetsdagar! ⚡"),
                ("bot", "Vill du boka en kostnadsfri 30-minuters demo där jag visar exakt hur det fungerar?"),
                ("user", "Ja, absolut! Det låter som precis vad vi behöver."),
                ("bot", "Fantastiskt! Jag öppnar vårt bokningssystem så du kan välja en tid som passar. Detta kommer att förändra ert företag! 🎯"),
                ("system", "OPEN_BOOKING_MODAL")
            ],
            
            # Conversation 2: Established company
            [
                ("bot", "🤖 Välkommen till Axie Studio! Vi revolutionerar företag med AI-teknik."),
                ("bot", "Sedan 2020 har vi hjälpt över 200 företag att automatisera sina processer och öka effektiviteten dramatiskt! 📈"),
                ("user", "Hej! Vi är ett etablerat företag med 50 anställda. Kan AI verkligen hjälpa oss?"),
                ("bot", "Absolut! Etablerade företag ser ofta de största fördelarna! 🏢 Ni har redan processer som kan optimeras."),
                ("bot", "Ett liknande företag sparade 25 timmar per vecka genom att automatisera sin orderhantering med vår AI-lösning."),
                ("user", "Det låter intressant. Vilka andra områden kan ni hjälpa med?"),
                ("bot", "Vi specialiserar oss på: 📋\n• Intelligent dokumenthantering\n• Automatisk dataanalys\n• Prediktiv underhåll\n• Smart personalplanering"),
                ("bot", "Vad säger du om en djupgående konsultation där vi analyserar era specifika behov?"),
                ("user", "Ja, det vore värdefullt. När kan vi träffas?"),
                ("bot", "Perfekt! Låt mig öppna vårt bokningssystem så du kan välja en tid som passar era scheman. 🗓️"),
                ("system", "OPEN_BOOKING_MODAL")
            ],
            
            # Conversation 3: Skeptical customer
            [
                ("bot", "🤖 Hej och välkommen till Axie Studio! Vi gör AI tillgängligt för alla företag."),
                ("bot", "Oavsett bransch eller storlek kan vi hjälpa er att dra nytta av AI:s kraft! 💪"),
                ("user", "Hej. Jag är lite skeptisk till AI. Är det verkligen värt investeringen?"),
                ("bot", "Jag förstår din skepsis helt! 🤔 Många av våra mest nöjda kunder var skeptiska från början."),
                ("bot", "Därför erbjuder vi alltid en kostnadsfri analys först. Inga löften - bara konkreta siffror på vad AI kan göra för ert företag."),
                ("user", "Okej, det låter rimligt. Men hur vet jag att ni kan leverera?"),
                ("bot", "Bra fråga! Vi har en 100% nöjd-kund-garanti. 🛡️ Om ni inte ser resultat inom 30 dagar får ni pengarna tillbaka."),
                ("bot", "Plus att vi kan visa er exakt ROI innan ni investerar en krona. Vill du se hur?"),
                ("user", "Ja, det skulle övertyga mig. Hur gör vi det?"),
                ("bot", "Perfekt! Jag bokar in en ROI-analys där vi räknar på era specifika siffror. Helt kostnadsfritt! 📊"),
                ("system", "OPEN_BOOKING_MODAL")
            ]
        ]

    def setup_advanced_ui(self):
        """Setup advanced UI with enhanced styling"""
        
        # Animated header
        self.create_animated_header()
        
        # Chat area with advanced features
        self.create_advanced_chat_area()
        
        # Enhanced input area
        self.create_enhanced_input_area()
        
        # Status and controls
        self.create_status_controls()

    def create_animated_header(self):
        """Create animated header with company branding"""
        header = tk.Frame(self.root, bg=self.colors['primary'], height=90)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Logo and company info
        header_content = tk.Frame(header, bg=self.colors['primary'])
        header_content.pack(expand=True, fill=tk.BOTH, padx=20)
        
        # Company logo (animated)
        try:
            logo_url = "https://www.axiestudio.se/logo.jpg"
            logo_response = requests.get(logo_url, timeout=3)
            logo_image = Image.open(BytesIO(logo_response.content))
            logo_image = logo_image.resize((60, 60), Image.Resampling.LANCZOS)
            
            # Add glow effect
            glow = logo_image.filter(ImageFilter.GaussianBlur(radius=2))
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            
            self.logo_label = tk.Label(header_content, image=self.logo_photo, bg=self.colors['primary'])
            self.logo_label.pack(side=tk.LEFT, pady=15)
        except:
            self.logo_label = tk.Label(header_content, text="🤖", font=font.Font(size=32), 
                                     bg=self.colors['primary'], fg='white')
            self.logo_label.pack(side=tk.LEFT, pady=15)
        
        # Company text with animation
        text_frame = tk.Frame(header_content, bg=self.colors['primary'])
        text_frame.pack(side=tk.LEFT, padx=15, pady=15)
        
        self.company_label = tk.Label(text_frame, text="Axie Studio AI-Assistent", 
                                    font=self.title_font, bg=self.colors['primary'], fg='white')
        self.company_label.pack(anchor='w')
        
        self.status_label = tk.Label(text_frame, text="🟢 Automatisk Demo Aktiv", 
                                   font=self.small_font, bg=self.colors['primary'], fg='#ccddff')
        self.status_label.pack(anchor='w')
        
        # Animate header
        self.animate_header()

    def create_advanced_chat_area(self):
        """Create advanced chat area with smooth scrolling"""
        chat_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Canvas for smooth scrolling
        self.chat_canvas = tk.Canvas(chat_frame, bg=self.colors['bg_chat'], 
                                   highlightthickness=0, bd=0)
        self.chat_scrollbar = ttk.Scrollbar(chat_frame, orient=tk.VERTICAL, 
                                          command=self.chat_canvas.yview)
        self.chat_content = tk.Frame(self.chat_canvas, bg=self.colors['bg_chat'])
        
        self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)
        
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.chat_window = self.chat_canvas.create_window((0, 0), window=self.chat_content, anchor="nw")
        
        # Bind events
        self.chat_content.bind('<Configure>', self.on_chat_configure)
        self.chat_canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Welcome message
        self.add_welcome_message()

    def create_enhanced_input_area(self):
        """Create enhanced input area with typing simulation"""
        input_frame = tk.Frame(self.root, bg=self.colors['bg_main'], height=70)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        input_frame.pack_propagate(False)
        
        # Input container
        input_container = tk.Frame(input_frame, bg='white', relief=tk.SOLID, bd=1)
        input_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Message input
        self.message_var = tk.StringVar()
        self.input_field = tk.Entry(input_container, textvariable=self.message_var,
                                  font=self.message_font, bg='white', relief=tk.FLAT,
                                  bd=10, fg=self.colors['text_primary'])
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Send button with animation
        self.send_button = tk.Button(input_container, text="🚀", font=font.Font(size=16),
                                   bg=self.colors['primary'], fg='white', relief=tk.FLAT,
                                   bd=0, padx=15, command=self.simulate_send)
        self.send_button.pack(side=tk.RIGHT, pady=5, padx=5)

    def create_status_controls(self):
        """Create status and control panel"""
        control_frame = tk.Frame(self.root, bg=self.colors['bg_main'], height=40)
        control_frame.pack(fill=tk.X, padx=10, pady=(0,5))
        control_frame.pack_propagate(False)
        
        # Demo controls
        tk.Label(control_frame, text="Demo Status:", font=self.small_font,
                bg=self.colors['bg_main'], fg=self.colors['text_secondary']).pack(side=tk.LEFT, padx=5)
        
        self.demo_status = tk.Label(control_frame, text="Kör automatiskt", font=self.small_font,
                                  bg=self.colors['secondary'], fg='white', padx=10, pady=2)
        self.demo_status.pack(side=tk.LEFT, padx=5)
        
        # Conversation counter
        self.conv_counter = tk.Label(control_frame, text="Konversation 1/3", font=self.small_font,
                                   bg=self.colors['bg_main'], fg=self.colors['text_secondary'])
        self.conv_counter.pack(side=tk.RIGHT, padx=5)

    def setup_auto_features(self):
        """Setup automatic features and behaviors"""
        # Auto-scroll behavior
        self.auto_scroll_enabled = True
        
        # Message timing
        self.typing_speed = 0.05  # Seconds per character
        self.message_delay = 2.0  # Seconds between messages
        self.conversation_delay = 5.0  # Seconds between conversations
        
        # Visual effects
        self.enable_message_animations = True
        self.enable_typing_indicators = True

    def add_welcome_message(self):
        """Add animated welcome message"""
        welcome_frame = tk.Frame(self.chat_content, bg=self.colors['bg_chat'])
        welcome_frame.pack(fill=tk.X, pady=20)
        
        welcome_text = tk.Label(welcome_frame, 
                              text="🎯 Automatisk AI-Demo Startar\n\nDu kommer att se olika kundscenarier som visar hur vår AI-assistent hanterar olika typer av förfrågningar.",
                              font=self.message_font, bg=self.colors['bg_chat'], 
                              fg=self.colors['text_secondary'], justify=tk.CENTER,
                              wraplength=400)
        welcome_text.pack(pady=10)

    def animate_header(self):
        """Animate header elements"""
        def animate():
            colors = [self.colors['primary'], '#0052a3', '#003d7a', self.colors['primary']]
            while True:
                for color in colors:
                    try:
                        # Animate logo background
                        self.logo_label.configure(bg=color)
                        self.company_label.configure(bg=color)
                        self.status_label.configure(bg=color)
                        self.root.update()
                        time.sleep(1.0)
                    except:
                        break
        
        threading.Thread(target=animate, daemon=True).start()

    def add_message_with_animation(self, text, is_bot, animate_typing=True):
        """Add message with advanced animations"""
        # Create message container
        msg_container = tk.Frame(self.chat_content, bg=self.colors['bg_chat'])
        msg_container.pack(fill=tk.X, padx=15, pady=8)
        
        # Message bubble
        if is_bot:
            bubble_frame = tk.Frame(msg_container, bg=self.colors['bg_chat'])
            bubble_frame.pack(anchor='w')
            
            # Bot avatar
            avatar = tk.Label(bubble_frame, text="🤖", font=font.Font(size=16),
                            bg=self.colors['bg_chat'])
            avatar.pack(side=tk.LEFT, padx=(0,10))
            
            # Message content
            content_frame = tk.Frame(bubble_frame, bg=self.colors['bot_bg'], 
                                   relief=tk.FLAT, bd=0)
            content_frame.pack(side=tk.LEFT)
            
            message_label = tk.Label(content_frame, text="", font=self.message_font,
                                   bg=self.colors['bot_bg'], fg=self.colors['bot_text'],
                                   wraplength=350, justify=tk.LEFT, padx=15, pady=10)
            message_label.pack()
            
        else:
            bubble_frame = tk.Frame(msg_container, bg=self.colors['bg_chat'])
            bubble_frame.pack(anchor='e')
            
            # Message content
            content_frame = tk.Frame(bubble_frame, bg=self.colors['user_bg'], 
                                   relief=tk.FLAT, bd=0)
            content_frame.pack(side=tk.RIGHT)
            
            message_label = tk.Label(content_frame, text="", font=self.message_font,
                                   bg=self.colors['user_bg'], fg=self.colors['user_text'],
                                   wraplength=350, justify=tk.LEFT, padx=15, pady=10)
            message_label.pack()
            
            # User avatar
            avatar = tk.Label(bubble_frame, text="👤", font=font.Font(size=16),
                            bg=self.colors['bg_chat'])
            avatar.pack(side=tk.RIGHT, padx=(10,0))
        
        # Animate text appearance
        if animate_typing:
            self.animate_text_typing(message_label, text)
        else:
            message_label.configure(text=text)
        
        # Add timestamp
        timestamp = tk.Label(msg_container, text=datetime.now().strftime("%H:%M"),
                           font=font.Font(size=8), bg=self.colors['bg_chat'],
                           fg=self.colors['text_secondary'])
        timestamp.pack(anchor='e' if is_bot else 'w', padx=15)
        
        # Auto-scroll
        if self.auto_scroll_enabled:
            self.root.after(100, self.scroll_to_bottom)

    def animate_text_typing(self, label, text):
        """Animate text typing with realistic speed"""
        def type_text():
            words = text.split(' ')
            current_text = ""
            
            for word in words:
                current_text += word + " "
                label.configure(text=current_text.strip())
                self.root.update()
                
                # Variable typing speed based on word length
                delay = len(word) * self.typing_speed + random.uniform(0.1, 0.3)
                time.sleep(delay)
        
        threading.Thread(target=type_text, daemon=True).start()

    def simulate_user_typing(self, text):
        """Simulate realistic user typing"""
        self.message_var.set("")
        
        # Show typing in input field
        for i, char in enumerate(text):
            self.message_var.set(text[:i+1])
            self.root.update()
            
            # Realistic typing delays
            if char == ' ':
                time.sleep(0.2)
            elif char in '.,!?':
                time.sleep(0.3)
            else:
                time.sleep(random.uniform(0.05, 0.15))
        
        # Simulate send button press
        self.animate_send_button()
        time.sleep(0.5)
        self.message_var.set("")

    def animate_send_button(self):
        """Animate send button press"""
        original_bg = self.send_button.cget('bg')
        self.send_button.configure(bg=self.colors['secondary'])
        self.root.update()
        time.sleep(0.2)
        self.send_button.configure(bg=original_bg)

    def simulate_send(self):
        """Simulate send button functionality"""
        pass  # Disabled during demo

    def scroll_to_bottom(self):
        """Smooth scroll to bottom"""
        self.chat_canvas.yview_moveto(1.0)

    def start_super_automation(self):
        """Start the super automated demo"""
        def automation_loop():
            while True:
                for conv_index, conversation in enumerate(self.conversations):
                    self.current_conversation = conv_index
                    self.conv_counter.configure(text=f"Konversation {conv_index + 1}/{len(self.conversations)}")
                    
                    # Clear chat for new conversation
                    self.clear_chat()
                    time.sleep(1)
                    
                    # Run conversation
                    for sender, message in conversation:
                        if sender == "system" and message == "OPEN_BOOKING_MODAL":
                            time.sleep(1.5)
                            self.root.after(0, lambda: AdvancedBookingModal(self.root))
                            time.sleep(10)  # Wait for booking interaction
                            break
                        elif sender == "bot":
                            self.add_message_with_animation(message, True)
                            time.sleep(self.message_delay)
                        else:
                            self.simulate_user_typing(message)
                            self.add_message_with_animation(message, False, animate_typing=False)
                            time.sleep(self.message_delay)
                    
                    # Pause between conversations
                    time.sleep(self.conversation_delay)
        
        # Start automation thread
        automation_thread = threading.Thread(target=automation_loop, daemon=True)
        automation_thread.start()

    def clear_chat(self):
        """Clear chat content for new conversation"""
        for widget in self.chat_content.winfo_children():
            widget.destroy()
        self.add_welcome_message()

    def on_chat_configure(self, event=None):
        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.chat_canvas.itemconfig(self.chat_window, width=event.width)

def main():
    """Main application entry point"""
    root = tk.Tk()
    
    # Enhanced window configuration
    root.configure(bg='#f0f2f5')
    root.resizable(True, True)
    root.minsize(400, 500)
    
    # Set window icon
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    # Create application
    app = SuperAutomatedChatbot(root)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()