import os, subprocess, time, webbrowser

#Sounds

def play_sound(file, vol=100):
    if os.path.exists(file):
        subprocess.Popen(
            ["paplay", f"--volume={vol*65536//100}", file],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
def cmenu_in():
    play_sound("/usr/share/sounds/ocean/stereo/complete-media-burn.oga",75)
def cmenu_in2():
    play_sound("/usr/share/sounds/ocean/stereo/service-logout.oga",80)
def cmenu_out():
    play_sound("/usr/share/sounds/ocean/stereo/game-over-loser.oga",85)
def cmenu_out2():
    play_sound("/usr/share/sounds/ocean/stereo/completion-fail.oga")
def cdots():
    play_sound("/usr/share/sounds/ocean/stereo/completion-success.oga",70)

# Colors
  
def green(text): print(f"\033[1;38;5;120m{text}\033[0m")
def orange(text):print(f"\033[1;38;5;208m{text}\033[0m")
def red(text):print(f"\033[31m{text}\033[0m")

# little def's

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
def get_option():
    val = int(input("    \033[1;38;5;208mOption: \033[0m")or 0)
    return val
def confirmation():
    resposta = input("     \033[32mcontinue...\033[0m")
def bar():
    print("\033[1m#========================================================#\033[0m")
def leave_menu():
    print("\033[1;32mReturning...\033[0m"); time.sleep(0.25)

def confirmation_power():
    return input("\033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m").lower() == "y"
def all_done():
    print("\033[32mAll Done!\033[0m");         time.sleep(0.25)
def valid():
    print("  \033[31mSelect Valid Option...\033[0m");   time.sleep(0.5)
def menu_spacing():
    print("\033[1m |                                                      |\033[0m")
def fastfetch():
    os.system("fastfetch")


#  CachyOS Section
def cachy_main_menu_print():
    clear_console();        print(f"\033[1;38;5;208m  ----< {time.strftime('%H:%M')} >----< Pinalto's CachyOS Manager >-------\033[0m");    bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mNetwork Tools\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPower Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m6 ➜\033[0m \033[1;36mAnime Player\033[0m                                    |\033[0m")
    print("\033[1m |  \033[38;5;208m7 ➜\033[0m \033[1;36mTerminal/Fastfetch Options\033[0m                      |\033[0m")
    print("\033[1m |  \033[38;5;208m8 ➜\033[0m \033[1;36mGithub Repos\033[0m                                    |\033[0m")
    print("\033[1m |  \033[38;5;208m9 ➜\033[0m \033[1;36mSSH Options\033[0m                                     |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mQuit\033[0m                                            |\033[0m");  bar()


# Option 1 System Update

def Syu():
    cmenu_in(); clear_console(); orange("             ----- Updating System -----  "); bar(); time.sleep(0.4)
    cmd = "yay -Syu --noconfirm && flatpak update -y && yay -Scc --noconfirm && sudo pacman -Scc --noconfirm && sudo pacman -Rns $(pacman -Qtdq 2>/dev/null)"
    try:
        subprocess.run(cmd, shell=True, check=True)
        green("[ok] update + cleanup")
    except subprocess.CalledProcessError:
        red("[erro] update + cleanup")

# Option 2 Network Options
def network_menu_print():
    cmenu_in();  clear_console();        print(f"\033[1;38;5;208m                 Configuration Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mNetwork Speedtest\033[0m                               |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mRestart Wifi Network\033[0m                            |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mShow Local IP\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m"); bar()

def speedtest_cli():
    subprocess.run("pacman -Qq speedtest-cli >/dev/null || sudo pacman -S --noconfirm speedtest-cli", shell=True)
    subprocess.run(["speedtest-cli"]);      confirmation()

def restart_network():
    green(" Restarting Network Manager...")
    subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"]);      confirmation()

def ip_info():
    green("--- IP INFO ---")
    try:
        ip = subprocess.check_output(r"ip route get 1.1.1.1 | grep -oP 'src \K\S+'", shell=True).decode().strip()
        host = subprocess.check_output("hostname", shell=True, text=True).strip()
        print(f"➜ Hostname: {host}");  print(f"➜ Local IP: {ip}");    confirmation()
    except: red("Unable to get local IP.")

def cachy_network_options():
        cmenu_in()
        while True:
            network_menu_print()
            try: opc = get_option()
            except ValueError: valid(); continue
            if opc == 1: speedtest_cli()
            elif opc == 2: restart_network()
            elif opc == 3: ip_info()
            else: cmenu_out(); break

# Option 3 Setup Options
def cachy_opc3_menu_print():
    clear_console();        print(f"\033[1;38;5;208m                 Setup Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mDownload Utilitaries Packages\033[0m                   |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mDownload Gaming Packages\033[0m                        |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mDownload Worktools Packages\033[0m                     |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mDownload All Packages\033[0m                           |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPackages Info:\033[0m                                  |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");   bar()

def cachy_download_utilitaries():
    comando = '''
    sudo pacman -S --needed yay git curl openssh python python-pip xorg-server flatpak zip fuse2 nemo libreoffice-fresh vlc speedtest-cli &&
    yay -S --needed helium-browser-bin bazaar &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub com.github.tchx84.Flatseal it.mijorus.gearlever'''

    try:
        subprocess.run(comando, shell=True, check=True);        green("Instalation Over.")
    except subprocess.CalledProcessError:
        red("Error Durring Instalation.")

def cachy_download_gaming():
    comando = '''
    sudo pacman -S --needed steam gamemode mangohud protonup-qt plasma-x11-session kwin-x11 prismlauncher gnome-mines protonup-qt
    yay -S --needed ytmdesktop &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub com.protonvpn.www
    '''

    try:
        subprocess.run(comando, shell=True, check=True);    green("Instalation Over.")
    except subprocess.CalledProcessError:
        red("Error Durring Instalation.")

def cachy_download_worktools():
    comando = '''
    sudo pacman -S --needed yay python python-pip wget code vim obs-studio krita nmap vesktop &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install -y flathub com.rtosta.zapzap io.gitlab.adhami3310.Impression io.github.brunofin.Cohesion
    '''

    try:
        subprocess.run(comando, shell=True, check=True);    green("Instalation Over.")
    except subprocess.CalledProcessError:
        red("Error During Installation.")

def cachy_download_all(): cachy_download_utilitaries();cachy_download_worktools();cachy_download_gaming(); Syu()

def cachy_show_packages():
    orange("         === UTILITARIES ===");green("--> pacman: yay, SSH ,python, xorg-server, curl,missioncenter ,libreoffice-fresh, git, python-pip, thunderbird, nemo, vlc, flatpak, zip, fuse2")
    green("--> yay: shortwave, brave-bin, helium-browser-bin,, youtube music desktop,bazaar\n--> flatpak: Cohesion, localsend, Impression")
    orange("\n       === GAMING ===");green("--> pacman: steam, mangohud, gamemode, prismlauncher, plasma-x11-session, kwin-x11")
    orange("\n       === WORKTOOLS ===");green("--> pacman: vscode, yay, python, wget, python-pip, nmap, krita, neofetch, obs-studio, vim, vesktop, pycharm-community-edition, virtualbox, virtualbox-host-modules-arch")
    green("--> yay: google-earth-pro\n--> flatpak: it.mijorus.gearlever, com.github.tchx84.Flatseal")

def cachy_setup():
    cmenu_in()
    while True:
        cachy_opc3_menu_print()
        try: opc = get_option()
        except ValueError: valid(); continue
        if opc == 1: cachy_download_utilitaries(); all_done()
        elif opc == 2: cachy_download_gaming(); all_done()
        elif opc == 3: cachy_download_worktools(); all_done()
        elif opc == 4: cachy_download_all()
        elif opc == 5: cachy_show_packages(); confirmation()
        else: cmenu_out();break

# Option 4 Components Listing

def linux_list_components():
    cmenu_in();     clear_console();                orange("                  --- COMPONENTS ---                          ");  bar()
    time_start= time.time();    os.system("inxi -F");   time_end=time.time();
    bar();print(f"\033[1;93mElapsed time: {time_start - time_end:.4f}\033[0m");bar();confirmation();cmenu_out()

# Option 5 Power Menu
def power_menu_print():
    clear_console();        print("\033[38;5;208m             ----- Power Options -----  \033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mPower Off\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mReboot\033[0m                                          |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSuspend\033[0m                                         |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()

def linux_power_menu():
    cmenu_in();
    while True:
        power_menu_print()
        try:    opc = get_option()
        except ValueError:      valid();        continue
        if opc == 1:
            opc = input("      \033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m")
            if opc == "y":      os.system("shutdown now")
            else:       clear_console();    leave_menu()
        elif opc == 2:
            opc = input("      \033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m")
            if opc == "y":      os.system("reboot")
            else:       clear_console();    leave_menu()
        elif opc == 3:      os.system("systemctl suspend")
        else: cmenu_out();   break

# Option 6 Anime Player

def cachy_run_ani_cli():
    try:
        subprocess.run(["ani-cli"], check=True)
    except FileNotFoundError:
        red("\033[1;31mError: ani-cli not installed.\033[0m");time.sleep(0.8)
        inst_ask = input("   \033[1;32mWould you like to install Ani=cli? (y/N)\033[0m\n:")
        if inst_ask.lower() == "y":
            subprocess.run(["yay", "-S", "ani-cli"])
        else:
            green("Returning...");time.sleep(0.9)
    except subprocess.CalledProcessError:
        print("\033[1;31mUnable to run ani-cli.\033[0m")
        print("\033[1;32mReturning...\033[0m");time.sleep(0.9)

def fix_ani_cli():
    subprocess.run("sudo ani-cli -U", shell=True)

# Option 7 Terminal/Fastfetch

def cachy_terminal_menu_print():
    clear_console();    print(f"\033[1;38;5;208m             Terminal Menu...(Fish)\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mOpen Fish Terminal.conf\033[0m                         |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mSetup Custom Fish Terminal Config\033[0m               |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mFastFetch\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mSetup Fastfetch json\033[0m                            |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mSetup Fastfetch Ascii Art\033[0m                       |\033[0m");
    print("\033[1m |  \033[38;5;208m6 ➜\033[0m \033[1;36mOpen Fastfetch.json\033[0m                             |\033[0m");
    print("\033[1m |  \033[38;5;208m7 ➜\033[0m \033[1;36mOpen Ascii art.txt\033[0m                              |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()

def update_config_fish():
            caminho = "/usr/share/cachyos-fish-config/cachyos-config.fish"
            linha = """alias central="python $HOME/update.py"
alias centralc="kate $HOME/update.py"
alias update='sudo pacman -Syu && sudo pacman -Sc && sudo pacman -Rns (pacman -Qtdq) && sudo journalctl --vacuum-time=7d && sudo fstrim -av'
alias audio='alsamixer'
alias anime='ani-cli'
alias reb='reboot'
alias off='poweroff'
alias config_fish="kate /usr/share/cachyos-fish-config/cachyos-config.fish"
alias config_neofetch='kate ~/.config/neofetch/config.conf'
alias config_fastfetch='kate ~/.config/fastfetch/config.jsonc'
alias componentes="inxi -F"
"""
            with open(caminho, "r") as f:
                linhas = [l.strip() for l in f.readlines()]
            if linha not in linhas:
                subprocess.run(
                    ["sudo", "tee", "-a", caminho],
                    input=linha + "\n",
                    text=True
                )

def create_fastfetch():
    caminho_dir = os.path.expanduser("~/.config/fastfetch")
    os.makedirs(caminho_dir, exist_ok=True)

    caminho_arquivo = os.path.join(caminho_dir, "config.jsonc")

    conteudo = """{
    "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
    "logo": {
        "source": "~/.config/fastfetch/ascii.txt",
        "color": {
            "1": "0"
        }
    },
    "modules": [
        {
            "type": "os",
            "key": "OS  ",
            "keyColor": "red"  // = color1
        },
        {
            "type": "wm",
            "key": "WM  ",
            "keyColor": "32"
        },
        {
            "type": "cpu",
            "format": "{1} ({3}) @ {7} GHz",
            "key": "CPU ",
            "keyColor": "blue"
        },
        {
            "type": "gpu",
            "format": "{1} {2} @ {12} GHz",
            "key": "GPU ",
            "keyColor": "33"
        },
        {
            "type": "memory",
            "key": "MEM ",
            "keyColor": "cyan"
        }
    ]
}"""
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

def create_new_ascii():
    caminho = os.path.expanduser("~/.config/fastfetch/ascii.txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    arte = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ▄▀ ▄▀
      ▀  ▀
    █▀▀▀▀▀█▄
    █░░░░░█ █
    ▀▄▄▄▄▄▀▀
⠀
"""
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(arte)

def open_ascii_config():
    os.system("xdg-open ~/.config/fastfetch/ascii.txt")
def open_fastfetch_config():
    os.system("xdg-open ~/.config/fastfetch/config.jsonc")

def cachy_terminal():
    cmenu_in()
    while True:
                cachy_terminal_menu_print()
                try: opc = get_option()
                except ValueError: valid(); continue
                if opc == 1: subprocess.run(["kate", "/usr/share/cachyos-fish-config/cachyos-config.fish"])
                elif opc == 2: update_config_fish(); all_done()
                elif opc == 3: os.system("fastfetch");confirmation();
                elif opc == 4: create_fastfetch()
                elif opc == 5: create_new_ascii()
                elif opc == 6: open_fastfetch_config()
                elif opc == 7: open_ascii_config()
                else: cmenu_out(); break

# Option 8 Repo Manager 

def repo_manager_print():
    clear_console();    print(f"\033[1;38;5;208m                Github Repos...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mSilent Hill Native PC (linux/win)(.iso needed)\033[0m  |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mSteam Achivement Unlocker\033[0m                       |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mPinalto's PcManager\033[0m                             |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()
def repo_manager():
    cmenu_in()
    while True:
        repo_manager_print()
        opc = get_option()
        if opc == 1:    webbrowser.open("https://github.com/SlickAmogus/silent-hill-pc-nightly")
        elif opc == 2:  webbrowser.open("https://github.com/asdfghj1237890/SteamAchievementManager-Enhanced")
        elif opc == 3:  webbrowser.open("https://github.com/GabeSvbr/Pinaltos_PcManager")
        else: cmenu_out();break

# Option 9 SSH

def cachy_ssh_print():
    clear_console();    print(f"\033[1;38;5;208m                SSH Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mStatus SSH\033[0m                                      |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mStart SSH\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mStop SSH\033[0m                                        |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mRestart SSH\033[0m                                     |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mShow Machine IP\033[0m                                 |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()

def cachy_ssh():
    cmenu_in();
    while True:
                cachy_ssh_print()
                try: opc = get_option()
                except ValueError: valid(); continue
                if opc == 1: os.system("systemctl status sshd"); confirmation()
                elif opc == 2: os.system("sudo systemctl start sshd"); confirmation()
                elif opc == 3: os.system("sudo systemctl stop sshd"); confirmation()
                elif opc == 4: os.system("sudo systemctl restart sshd")
                elif opc == 5: clear_console(); ip_info()
                else: cmenu_out(); break

#  Debug menu

def menu_debug():
    while True:
        clear_console();print(f"1 - cmenu_in\n2 - cmenu_in2\n3 - cmenu_out\n4 - cmenu_out2\n5 - cdots")
        opc=get_option()
        if opc == 1: cmenu_in()
        elif opc == 2: cmenu_in2()
        elif opc == 3: cmenu_out()
        elif opc == 4: cmenu_out2()
        elif opc == 5: cdots()
        else: cmenu_out();break

# Main Navigator 

def menu_cachyos():
    cont1 = 0
    cmenu_in2()
    while cont1 == 0:
        cachy_main_menu_print()
        try: opc = get_option()
        except ValueError: valid(); continue
        if opc == 1:
            t = time.time(); clear_console(); Syu()
            bar(); print(f"\033[1;93mElapsed time: {time.time() - t:.4f}\033[0m")
            bar(); confirmation();cmenu_out()
        elif opc == 2: cachy_network_options()
        elif opc == 3: cachy_setup()
        elif opc == 4: linux_list_components()
        elif opc == 5: linux_power_menu()
        elif opc == 6: cachy_run_ani_cli()
        elif opc == 7: cachy_terminal()
        elif opc == 8: repo_manager()
        elif opc == 9: cachy_ssh()
        elif opc == 99: menu_debug()
        elif opc == 66: fix_ani_cli()
        else: cont1 += 1; clear_console(); cmenu_out2()

#    -MAIN- 

def main():
    orange("Pinalto's Manager...\n")
    for i in range(4):
        clear_console()
        bar()
        print(f"\033[1m |\033[1;34mLoading CachyOS Version{'.' * i}\033[0m")
        bar()
        cdots()
        time.sleep(0.20)
    menu_cachyos()

#===================================================== RUN ====================================================#"
main()
