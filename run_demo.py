#!/usr/bin/env python3
"""
Quick launcher for the enhanced chatbot demo
Run this file to start the super automated demo
"""

import sys
import os

def main():
    print("🚀 Starting Axie Studio AI Chatbot Demo...")
    print("=" * 50)
    print("Features:")
    print("• Multiple conversation scenarios")
    print("• Advanced booking modal")
    print("• Automatic demo loop")
    print("• Enhanced Python automation")
    print("• Minimal CSS/JS dependencies")
    print("=" * 50)
    
    try:
        # Import and run the enhanced chatbot
        from enhanced_chatbot import main as run_chatbot
        run_chatbot()
    except ImportError:
        print("❌ Error: Could not import enhanced_chatbot module")
        print("Make sure enhanced_chatbot.py is in the same directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting demo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()