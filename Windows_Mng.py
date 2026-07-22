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


#  Windows Section

def windows_main_menu_print():
    clear_console();        print(f"\033[1;38;5;208m  ----< {time.strftime('%H:%M')} >----< Pinalto's Windows Manager >-------\033[0m");    bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mGithub Repos\033[0m                                    |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPower Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mQuit\033[0m                                            |\033[0m");  bar()


# Option 1 System Update

def update():
    
    t = time.time()
    cmenu_in(); clear_console(); orange("             ----- Updating System -----  "); bar(); time.sleep(0.4)
    cmd = (
        'winget upgrade --all --silent --accept-source-agreements --accept-package-agreements && '
        'DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase && '
        'cleanmgr /sagerun:1'
    )
    try:
        subprocess.run(cmd, shell=True, check=True)
        green("[ok] update + cleanup")
    except subprocess.CalledProcessError:
        red("[erro] update + cleanup")
    
    bar(); print(f"\033[1;93mElapsed time: {time.time() - t:.4f}\033[0m")
    bar(); confirmation()

# Option 2 Setup Options
def windows_opc3_menu_print():
    clear_console();        print(f"\033[1;38;5;208m                 Setup Menu...\033[0m"); bar()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mDownload Utilitaries Packages\033[0m                   |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mDownload Gaming Packages\033[0m                        |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mDownload Worktools Packages\033[0m                     |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mDownload All Packages\033[0m                           |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPackages Info:\033[0m                                  |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");   bar()


def install(package_id):
    subprocess.run([
        "winget", "install",
        "--accept-source-agreements",
        "--accept-package-agreements",
        "-e", "--id", package_id
    ])
    

def windows_download_utilitaries():
    install("Git.Git")
    install("python.Python.3.12")
    install("RARLab.WinRAR")
    install("TheDocumentFoundation.LibreOffice")
    install("VideoLAN.VLC")
    install("Microsoft.PowerToys")
    install("ImputNet.Helium")
    install("Brave.Brave")
    install("Rufus.Rufus")
    install("AntibodySoftware.WizTree")
    install("KDE.Kate")


def windows_download_gaming():
    install("Valve.Steam")
    install("PrismLauncher.PrismLauncher")
    install("CPUID.CPU-Z")
    install("YoutubeMusicDesktopApp.YoutubeMusicDesktopApp")
    install("MullvadVPN.MullvadVPN")
    install("Discord.Discord")
    install("Logitech.GHUB")
    install("Guru3D.Afterburner")
    install("EpicGames.EpicGamesLauncher")
    install("WeMod.WeMod")
    install("Playnite.Playnite")


def windows_download_worktools():
   install("GNU.Wget2")
   install("Microsoft.VisualStudioCode")
   install("OBSProject.OBSStudio")
   install("Insecure.Nmap")
   install("HandBrake.HandBrake")


def windows_download_all():
    windows_download_utilitaries()
    windows_download_worktools()
    windows_download_gaming()
    update()


def windows_show_packages():
    orange("         === UTILITARIES ===")
    green("--> winget: Git, Python, 7zip, LibreOffice, VLC, Speedtest, PowerToys, Bazaar, Helium Browser")
    orange("\n       === GAMING ===")
    green("--> winget: Steam, PrismLauncher, MangoHud, YouTube Music Desktop, ProtonVPN")
    orange("\n       === WORKTOOLS ===")
    green("--> winget: VSCode, Git, Python, Wget, Vim, OBS Studio, Krita, Nmap, Vesktop, PyCharm Community, VirtualBox")


def windows_setup():
    cmenu_in()
    while True:
        cachy_opc3_menu_print()
        try:
            opc = get_option()
        except ValueError:
            valid(); continue
        if opc == 1: windows_download_utilitaries(); all_done()
        elif opc == 2: windows_download_gaming(); all_done()
        elif opc == 3: windows_download_worktools(); all_done()
        elif opc == 4: windows_download_all()
        elif opc == 5: windows_show_packages(); confirmation()
        else: cmenu_out(); break

# Option 3 Components Listing

def windows_list_components():
    clear_console()
    orange("                  --- COMPONENTS ---                          ")
    bar()
    time_start = time.time()
    os.system('powershell -Command "Get-ComputerInfo"')
    time_end = time.time()
    bar()
    print(f"\033[1;93mElapsed time: {time_end - time_start:.4f}\033[0m")
    bar()
    confirmation()


# Option 4 Repo Manager

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
        else: break

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

def menu_windows():
    cont1 = 0
    cmenu_in2()
    while cont1 == 0:
        windows_main_menu_print()
        try: opc = get_option()
        except ValueError: valid(); continue
        if opc == 1:
            t = time.time(); clear_console(); Syu()
            bar(); print(f"\033[1;93mElapsed time: {time.time() - t:.4f}\033[0m")
            bar(); confirmation();cmenu_out()
        elif opc == 2: windows_setup()
        elif opc == 3: windows_list_components()
        elif opc == 4: repo_manager()
        elif opc == 5: linux_power_menu()
        elif opc == 99: menu_debug()
        else: cont1 += 1; clear_console()

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
    menu_windows()

#===================================================== RUN ====================================================#"
main()
