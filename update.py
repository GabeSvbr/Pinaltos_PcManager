import os, subprocess, time

#================================================= COLORS =====================================================================#"
def green(text): print(f"\033[1;38;5;120m{text}\033[0m")
def orange_head(text):print(f"\033[1;38;5;208m{text}\033[0m")
def red_death(text):print(f"\033[31m{texto}\033[0m")
#============================================= DEF'S OPTION 1 =================================================================#"
def Syu():
    orange_head("             ----- Updating System -----  ")
    clear_console();orange_head("             ----- Updating System -----  "); bar(); time.sleep(0.4)
    comandos = [
    ("update + cleanup", "yay -Syu --noconfirm && flatpak update -y && yay -Scc --noconfirm && sudo pacman -Scc --noconfirm && sudo pacman -Rns $(pacman -Qtdq 2>/dev/null)")
    ]
    for nome, cmd in comandos:
        try:
            subprocess.run(cmd, shell=isinstance(cmd, str), check=True)
            print(f"[ok] {nome}")
        except subprocess.CalledProcessError:
            print(f"[erro] {nome}")
#============================================= DEF'S OPTION 2 =================================================================#"
def speedtest_cli():
    green(" Checking speedtest-cli Instalation...")
    subprocess.run("pacman -Qq speedtest-cli >/dev/null || sudo pacman -S --noconfirm speedtest-cli", shell=True)
    green(" Inicializing Speedtest...");time.sleep(0.5)
    subprocess.run(["speedtest-cli"]);      confirmation()
def restart_network():
    green(" Restarting Network Manager...")
    subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
    green(" Wifi conection restarted.");      confirmation()
def ip_info():
    green("--- IP INFO ---")
    try:
        ip = subprocess.check_output(r"ip route get 1.1.1.1 | grep -oP 'src \K\S+'", shell=True).decode().strip()
        host = subprocess.check_output("hostname", shell=True, text=True).strip()
        print(f"➜ Hostname: {host}")
        print(f"➜ Local IP: {ip}");
        confirmation()
    except: red_death("Local IP: Unable to get it.")
#============================================= DEF'S OPTION 3 =================================================================#"
def download_utilitaries():
    comando = '''
    sudo pacman -S --needed yay python xorg-server curl speedtest-cli libreoffice-fresh openssh git python-pip python thunderbird kitty nemo vlc flatpak zip fuse2 &&
    yay -S --needed shortwave helium-browser-bin bazaar brave-bin mission-center ytmdesktop &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub io.github.brunofin.Cohesion org.localsend.localsend_app com.rtosta.zapzap io.gitlab.adhami3310.Impression'''
    try:
        subprocess.run(comando, shell=True, check=True)
        green("Instalation Over.")
    except subprocess.CalledProcessError:
        green("Error Durring Instalation.")
def download_gaming():
    comando = '''
    sudo pacman -S --needed steam mangohud gamemode gnome-mines prismlauncher protonup-qt plasma-x11-session kwin-x11
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub com.protonvpn.www
    '''
    try:
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError:
        red_death("Error")
def download_worktools():
    comando = '''
    sudo pacman -S --needed yay python nmap wget python-pip krita neofetch obs-studio vim vesktop pycharm-community-edition virtualbox virtualbox-host-modules-arch code &&
    yay -S --needed google-earth-pro &&
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub it.mijorus.gearlever com.github.tchx84.Flatseal
    '''
    try:
        subprocess.run(comando, shell=True, check=True)
        green("Instalation Over.")
    except subprocess.CalledProcessError:
        red_death("Error During Installation.")
def download_all():
    download_utilitaries();     download_worktools();    download_gaming(); Syu()
def show_packages():
    orange_head("         === UTILITARIES ===");green("--> pacman: yay, SSH ,python, xorg-server, curl,missioncenter ,libreoffice-fresh, git, python-pip, thunderbird, kitty, nemo, vlc, flatpak, zip, fuse2")
    green("--> yay: shortwave, brave-bin, helium-browser-bin,, youtube music desktop,bazaar\n--> flatpak: Cohesion, localsend, Bazaar, Impression")
    orange_head("\n       === GAMING ===");green("--> pacman: steam, mangohud, gamemode, prismlauncher, plasma-x11-session, kwin-x11")
    orange_head("\n       === WORKTOOLS ===");green("--> pacman: vscode, yay, python, wget, python-pip, nmap, krita, neofetch, obs-studio, vim, vesktop, pycharm-community-edition, virtualbox, virtualbox-host-modules-arch")
    green("--> yay: google-earth-pro\n--> flatpak: it.mijorus.gearlever, com.github.tchx84.Flatseal")

#============================================= DEF'S OPTION 4 =================================================================#"
def list_components():
    clear_console();                orange_head("                  --- COMPONENTS ---                          ");  bar()
    time_start= time.time();    os.system("inxi -F");   time_end=time.time();
    bar();print(f"\033[1;93mElapsed time: {time_start - time_end:.4f}\033[0m");bar();confirmation()
#============================================= DEF'S OPTION 5 =================================================================#"
def power_menu():
    while True:
        opc5_menu_print()
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
        else:       leave_menu();   break
#============================================= DEF'S OPTION 6 =================================================================#"
def run_ani_cli():
    try:
        subprocess.run(["ani-cli"], check=True)
    except FileNotFoundError:
        red_death("\033[1;31mError: ani-cli not installed.\033[0m");time.sleep(0.5)
        inst_ask = input("   \033[1;32mWould you like to install Ani=cli? (y/N)\033[0m\n:")
        if inst_ask.lower() == "y":
            subprocess.run(["yay", "-S", "ani-cli"])
        else:
            green("Returning...");time.sleep(1)
    except subprocess.CalledProcessError:
        print("\033[1;31mUnable to run ani-cli.\033[0m")
        print("\033[1;32mReturning...\033[0m");time.sleep(1)
#============================================= DEF'S OTION 7 =================================================================#"
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

def configure_kitty(destino=None):
    caminho = os.path.expanduser("~/.config/kitty/kitty.conf")
    config = """confirm_os_window_close 0
cursor_trail 1
cursor_shape beam
cursor_beam_thickness 4
cursor_stop_blinking_after 0
cursor_shape_unfocused unchanged
font_size 11.0
cursor_blink_interval 0.5
window_padding_width 25
font_family JetBrainsMono Nerd Font
bold_font auto
italic_font auto
bold_italic_font auto
background_opacity 0.9
hide_window_decorations yes
include current-theme.conf
"""
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w") as f:  # 🔥 "w" apaga tudo
        f.write(config)
def open_kitty_conf():
    os.system("xdg-open ~/.config/kitty/kitty.conf")
#============================================= DEF'S OPTION 8 =================================================================#"
def create_fastfetch():
    caminho_dir = os.path.expanduser("~/.config/fastfetch")
    os.makedirs(caminho_dir, exist_ok=True)
#------------
    caminho_arquivo = os.path.join(caminho_dir, "config.jsonc")
#------------
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
#============================================= Menu's Print's =================================================================#"
def menu_spacing():
    print("\033[1m |                                                      |\033[0m")
def main_menu_print():
    clear_console();        print(f"\033[1;38;5;208m  ----< {time.strftime('%H:%M')} >----< Pinalto's CachyOS Manager >-------\033[0m");    bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mComplete System Update\033[0m                          |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mNetwork Tools\033[0m                                   |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSetup Options\033[0m                                   |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mList Machine Components\033[0m                         |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPower Options\033[0m                                   |\033[0m");
    print("\033[1m |  \033[38;5;208m6 ➜\033[0m \033[1;36mAnime Player\033[0m                                    |\033[0m");
    print("\033[1m |  \033[38;5;208m7 ➜\033[0m \033[1;36mTerminal Options\033[0m                                |\033[0m");
    print("\033[1m |  \033[38;5;208m8 ➜\033[0m \033[1;36mFastFetch Options\033[0m                               |\033[0m");
    print("\033[1m |  \033[38;5;208m9 ➜\033[0m \033[1;36mSSH Options\033[0m                                     |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mQuit\033[0m                                            |\033[0m");  bar()
def opc2_menu_print():
    clear_console();        print(f"\033[1;38;5;208m                 Configuration Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mNetwork Speedtest\033[0m                               |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mRestart Wifi Network\033[0m                            |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mShow Local IP\033[0m                                   |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m"); bar()
def opc3_menu_print():
    clear_console();        print(f"\033[1;38;5;208m                 Setup Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mDownload Utilitaries Packages\033[0m                   |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mDownload Gaming Packages\033[0m                        |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mDownload Worktools Packages\033[0m                     |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mDownload All Packages\033[0m                          |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPackages Info:\033[0m                                  |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");   bar()
def opc5_menu_print():
    clear_console();        print("\033[38;5;208m             ----- Power Options -----  \033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mPower Off\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mReboot\033[0m                                          |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSuspend\033[0m                                         |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()
def opc7_menu_print():
    clear_console();    print(f"\033[1;38;5;208m                 Terminal Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mOpen Fish Terminal.conf\033[0m                         |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mSetup Custom Fish Terminal Config\033[0m               |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mOpen Kitty Terminal Conf\033[0m                        |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mSetup Custom Kitty Terminal Conf\033[0m                |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mKitty Themes\033[0m                                    |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()
def opc8_menu_print():
    clear_console();    print(f"\033[1;38;5;208m                 FastFetch Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mFastFetch\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mOpen FastFetch Ascii.txt\033[0m                        |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSetup FastFetch Ascii Art\033[0m                       |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mOpen Fastfetch.json\033[0m                             |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mSetup Fastfetch json\033[0m                            |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()
def opc9_ssh_print():
    clear_console();    print(f"\033[1;38;5;208m                SSH Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mStatus SSH\033[0m                                      |\033[0m");
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mStart SSH\033[0m                                       |\033[0m");
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mStop SSH\033[0m                                        |\033[0m");
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mRestart SSH\033[0m                                     |\033[0m");
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mShow Machine IP\033[0m                                 |\033[0m");
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");  bar()
#============================================= Little DEF's ======================================================================
def bar():
    print("\033[1m#========================================================#\033[0m")
def clear_console():
    os.system("clear")
def fastfetch():
    os.system("fastfetch")
def confirmation():
    resposta = input("     \033[32mcontinue...\033[0m")
def confirmation_power():
    return input("\033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m").lower() == "y"
def leave_menu():
    print("\033[1;32mReturning...\033[0m"); time.sleep(0.25)
def all_done():
    print("\033[32mAll Done!\033[0m");         time.sleep(1)
def valid():
    print("  \033[31mSelect Valid Option...\033[0m");   time.sleep(0.5)
def get_option():
    val = int(input("    \033[1;38;5;208mOption: \033[0m")or 0)
    return val
#============================================= MAIN NAVIGATOR ====================================================================================
def main():
    cont1 = 0
    while cont1 == 0:
        main_menu_print()
        try:    opc = get_option()
        except ValueError:      valid();    continue
#===> menu option 1
        if opc == 1:
            time_start = time.time();       clear_console();        Syu()
            time_end = time.time();bar();         print(f"\033[1;93mElapsed time: {time_start - time_end:.4f}\033[0m")
            bar();  confirmation()
#===> menu option 2
        elif opc == 2:
            while True:
                opc2_menu_print()
                try:
                    opc = get_option()
                except ValueError:      valid()     ;continue
                if opc == 1:        speedtest_cli()
                elif opc == 2:      restart_network()
                elif opc == 3:      ip_info()
                else:       leave_menu();  break
#===> menu option 3
        elif opc == 3:
            while True:
                opc3_menu_print()
                try:
                    opc = get_option()
                except ValueError:      valid();continue
                if opc == 1:        download_utilitaries();     all_done()
                elif opc == 2:      download_gaming();      all_done()
                elif opc == 3:      download_worktools();   all_done()
                elif opc == 4:      download_all()
                elif opc == 5:      show_packages();    confirmation()
                else:       leave_menu();            break
#===> menu option 4
        elif opc == 4:      clear_console();  list_components()
#===> menu option 5
        elif opc == 5:      clear_console(); power_menu()
#===> menu option 6
        elif opc == 6:      run_ani_cli()
#===> menu option 7
        elif opc == 7:
            while True:
                opc7_menu_print();
                try:   opc = get_option()
                except ValueError:  valid();   continue
                if opc == 1:     subprocess.run(["kate", "/usr/share/cachyos-fish-config/cachyos-config.fish"])
                elif opc == 2:   update_config_fish();           all_done()
                elif opc == 3:  open_kitty_conf()
                elif opc == 4:  configure_kitty();          all_done()
                elif opc == 5: os.system("kitten themes");
                else: leave_menu() ;      break
#===> menu option 8
        elif opc == 8:
             while True:
                opc8_menu_print()
                try:    opc = get_option()
                except ValueError:      valid();                    continue
                home = os.path.expanduser("~")
                if opc == 1:    fastfetch();        open_close_tab = input(":")
                elif opc == 2:  open_ascii_config();      all_done()
                elif opc == 3:  create_new_ascii();     all_done()
                elif opc == 4:  open_fastfetch_config();    all_done()
                elif opc == 5:  create_fastfetch();     all_done()
                else:   leave_menu();  break
#===> SSH menu
        elif opc == 9:
            while True:
                opc9_ssh_print()
                try:    opc = get_option()
                except ValueError:      valid();                    continue
                if opc == 1: os.system("systemctl status sshd");confirmation()
                elif opc == 2:  os.system("sudo systemctl start sshd");confirmation()
                elif opc == 3:  os.system("sudo systemctl stop sshd");confirmation()
                elif opc == 4:  os.system("sudo systemctl restart sshd")
                elif opc == 5:  clear_console();ip_info()
                else: leave_menu();break

        else:   cont1 += 1; clear_console()
#===================================================== MAIN ====================================================#"
main()
