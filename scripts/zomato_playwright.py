from playwright.sync_api import sync_playwright
import time
import os
import sys
import shutil

# Import the robust email OTP fetcher
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from email_system import EmailOTPFetcher

EMAIL = "kthewok@gmail.com"
APP_PASS = "svsn olug djum ljen"

RAW_DIR = r"D:\food\raw"
FINAL_DIR = r"D:\food\final"
REJECTED_DIR = r"D:\food\intake\rejected"

def setup_directories():
    os.makedirs(FINAL_DIR, exist_ok=True)
    os.makedirs(REJECTED_DIR, exist_ok=True)

def verify_images():
    setup_directories()
    raw_images = [f for f in os.listdir(RAW_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    
    if not raw_images:
        print("No images found in D:\\food\\raw to verify.")
        return

    print(f"Found {len(raw_images)} images to verify on Zomato.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Zomato Partner portal...")
        page.goto("https://www.zomato.com/partners/login")
        
        print("Waiting for you to initiate the login process (Click Login with Email, enter kthewok@gmail.com, and click Send OTP).")
        print("Once you click Send OTP on the website, this script will automatically fetch it from Gmail!")
        
        # We wait for the OTP input box to appear roughly
        try:
            # We fetch OTP aggressively
            print("Fetching OTP from Email System in the background...")
            fetcher = EmailOTPFetcher(EMAIL, APP_PASS)
            otp = fetcher.fetch_otp(wait_timeout=60)
            
            if otp:
                print(f"✅ OTP Extracted: {otp}")
                print(">>> PLEASE ENTER THIS OTP IN THE BROWSER NOW AND NAVIGATE TO THE 'MENU EDITOR' <<<")
            else:
                print("❌ Failed to fetch OTP. Please request a new one or enter manually.")
                
            print(f">>> Navigate to an item in the Menu Editor and open the 'Map photos' modal. <<<")
            print("You have 45 seconds to get to the 'Map photos' modal.")
            time.sleep(45)

            # Verification Loop
            print("--- STARTING IMAGE VERIFICATION LOOP ---")
            # Testing the first few images to prove the logic as requested
            for img_name in raw_images[:5]:
                img_path = os.path.join(RAW_DIR, img_name)
                print(f"\nEvaluating: {img_name}")
                
                try:
                    file_input = page.locator("input[type='file']")
                    if file_input.count() > 0:
                        file_input.first.set_input_files(img_path)
                        print("Uploaded to DOM. Waiting 4 seconds for Zomato processing...")
                        time.sleep(4)
                        
                        # Check for red errors
                        error_text = page.locator("text=resolution too low|Invalid aspect ratio|error|exceeds maximum")
                        is_rejected = error_text.count() > 0
                        
                        if is_rejected:
                            print(f"❌ REJECTED by Zomato UI. Moving '{img_name}' to intake/rejected.")
                            shutil.move(img_path, os.path.join(REJECTED_DIR, img_name))
                        else:
                            print(f"✅ ACCEPTED by Zomato UI. Moving '{img_name}' to final.")
                            shutil.move(img_path, os.path.join(FINAL_DIR, img_name))
                            
                        # CRITICAL: Zomato allows max 3 images. We must remove 1 by 1.
                        print("Attempting to auto-remove the uploaded image to clear the slot...")
                        try:
                            # Targeting common remove selectors in Zomato
                            remove_btn = page.locator("button:has-text('Remove'), button[aria-label*='Remove'], button[aria-label*='Delete']").last
                            if remove_btn.count() > 0:
                                remove_btn.click()
                                time.sleep(2)
                                print("Image removed from DOM.")
                            else:
                                input("⚠️ Auto-remove selector failed. Please click 'Remove/Delete' on the image in the browser, then press ENTER here to test the next one...")
                        except Exception:
                            input("⚠️ Please click 'Remove/Delete' on the image in the browser, then press ENTER here to test the next one...")
                            
                    else:
                        print("Could not find file input on page. Make sure the Map Photos modal is open!")
                        break
                        
                except Exception as loop_e:
                    print(f"Error evaluating {img_name}: {loop_e}")
                    
        except Exception as e:
            print(f"Critical Automation Error: {e}")
            
        print("\nAll verification complete. Keeping browser open for observation.")
        time.sleep(600)
        browser.close()

if __name__ == "__main__":
    verify_images()
