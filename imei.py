import sys
import random
import os
import base64
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

ENCRYPTED_LIC_KEY = "Y29kZWRieW1ua3M=" 
SECRET_SALT = 0x5A
LOCK_FILE = ".sys_lock_dat"

def verify_code_integrity():
    if os.path.exists(LOCK_FILE):
        return False
    try:
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
        integrity_marker = 'ENCRYPTED_LIC_KEY = "Y29kZWRieW1ua3M="'
        if integrity_marker not in content:
            with open(LOCK_FILE, 'w') as lf:
                lf.write("LOCKED")
            return False
        return True
    except:
        return False

if not verify_code_integrity():
    print(f"\n{Fore.RED}[!!!] KEY CRACKING DETECTED! PROGRAM LOCKED PERMANENTLY.{Style.RESET_ALL}\n")
    sys.exit(1)

def checksum(number, alphabet='0123456789'):
    n = len(alphabet)
    number = tuple(alphabet.index(i) for i in reversed(str(number)))
    return (sum(number[::2]) + sum(sum(divmod(i * 2, n)) for i in number[1::2])) % n

def calc_check_digit(number, alphabet='0123456789'):
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]

def simulate_btk_status(tac):
    legacy_2g_3g = ["35343410", "35824909", "35569511"]
    high_risk_clone = ["86084004", "86311705", "86772204", "86337404"]
    premium_tax = ["35925406", "35483210", "35673209"]

    if tac in premium_tax:
        return f"{Fore.MAGENTA}[BTK: Premium Device - High Tax / 120 Days Temp Registration Active]"
    elif tac in high_risk_clone:
        return f"{Fore.RED}[BTK: High Clone Risk - Market Volume Dense / Monitor Closely]"
    elif tac in legacy_2g_3g:
        return f"{Fore.YELLOW}[BTK: Legacy Model - 2G/3G Grid Status / Low Clone Risk]"
    else:
        return f"{Fore.BLUE}[BTK: Custom/Standard Device - Regular Tax & Registration Cycle]"

def main_app():
    logo = f"""{Fore.CYAN}
 __  __             _       _     
|  \/  |  _ __     | | __  | | __ 
| |\/| | | '_ \ _  | |/ /  | |/ / 
| |  | | | | | | |_|   <   |_   _|
|_|  |_| |_| |_|\___/|_|\_\  |_|  
    """
    print(logo)
    print(f"{Fore.YELLOW}=== Türkiye İmei by Mnks) ==={Style.RESET_ALL}")
    
    brands = {
        1: {"name": "Apple", "tac": ["35925406", "35483210", "35673209"]},
        2: {"name": "Samsung", "tac": ["35569511", "35487609", "35234511"]},
        3: {"name": "Xiaomi", "tac": ["86084004", "86311705", "86772204"]},
        4: {"name": "Huawei", "tac": ["35343410", "35824909"]},
        5: {"name": "Oppo_Realme_POCO", "tac": ["86337404", "35212411"]}
    }

    print(f"{Fore.GREEN}Please select a brand (You can select multiple like 1,3):{Style.RESET_ALL}")
    for key, brand in brands.items():
        print(f"[{key}] {brand['name']}")
    print("[6] Mixed (Randomly from all brands)")
    print("[7] Custom TAC (Enter your own 8-digit TAC)")
    print("-" * 75)

    selected_tacs = []
    brand_file_name = ""
    
    while True:
        try:
            choice_input = input('Your choice: ').strip().replace(" ", "")
        except KeyboardInterrupt:
            print(f'\n{Fore.RED}Exit.')
            sys.exit()

        if not choice_input:
            continue

        if choice_input == '7':
            while True:
                custom_tac = input('Enter your 8-digit Custom TAC: ').strip()
                if custom_tac.isdigit() and len(custom_tac) == 8:
                    selected_tacs.append(custom_tac)
                    brand_file_name = "CustomTAC"
                    break
                print(f'{Fore.RED}*** Invalid TAC! Must be exactly 8 digits.{Style.RESET_ALL}\n')
            break
        elif choice_input == '6':
            for b in brands.values():
                selected_tacs.extend(b["tac"])
            brand_file_name = "Mixed"
            break
        else:
            try:
                choices = [int(x) for x in choice_input.split(',')]
                if all(1 <= x <= 5 for x in choices):
                    choices = list(set(choices))
                    for c in choices:
                        selected_tacs.extend(brands[c]["tac"])
                    brand_file_name = "_".join([brands[c]["name"] for c in choices])
                    break
            except ValueError:
                pass
            print(f'{Fore.RED}*** Invalid choice!{Style.RESET_ALL}\n')

    count = 0
    while True:
        try:
            count_input = input('How many UNIQUE IMEIs to generate?: ').strip()
        except KeyboardInterrupt:
            sys.exit()

        if count_input.isdigit() and int(count_input) > 0:
            count = int(count_input)
            break
        print(f'{Fore.RED}*** Invalid count!{Style.RESET_ALL}\n')

    generated_data = {}
    max_attempts = count * 100
    attempts = 0

    print(f'\n{Fore.YELLOW}--- Generating Unique IMEIs & Simulating BTK Network Status ---{Style.RESET_ALL}')
    
    while len(generated_data) < count and attempts < max_attempts:
        attempts += 1
        tac = random.choice(selected_tacs)
        imei = tac
        while len(imei) < 14:
            imei += str(random.randint(0, 9))
        imei += calc_check_digit(imei)
        generated_data[imei] = tac

    for imei, tac in generated_data.items():
        status_log = simulate_btk_status(tac)
        print(f"{Fore.GREEN}{imei}  {status_log}")

    print("-" * 75)

    while True:
        try:
            save_choice = input('Do you want to save the results to a .txt file? (y/n): ').strip().lower()
        except KeyboardInterrupt:
            sys.exit()

        if save_choice in ['y', 'yes']:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{brand_file_name}_{count}_{timestamp}.txt"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    for imei in generated_data.keys():
                        f.write(imei + '\n')
                print(f"{Fore.CYAN}|--> Success! Saved to: {filename}\n")
            except Exception as e:
                print(f"{Fore.RED}*** Error saving file: {e}\n")
            break
        elif save_choice in ['n', 'no']:
            break

if __name__ == '__main__':
    if not verify_code_integrity():
        print(f"\n{Fore.RED}[!!!] KEY CRACKING DETECTED! PROGRAM LOCKED PERMANENTLY.{Style.RESET_ALL}\n")
        sys.exit(1)

    print(f"{Fore.CYAN}[SYSTEM] Initializing secure handshake...")
    
    while True:
        try:
            user_key = input("Enter License Key to unlock software: ").strip()
        except KeyboardInterrupt:
            sys.exit()

        if user_key == "mnks":
            print(f"{Fore.GREEN}[SUCCESS] Access Granted. Welcome back.")
            main_app()
            break
        else:
            print(f"{Fore.RED}[!] Invalid License Key. Try again.\n")