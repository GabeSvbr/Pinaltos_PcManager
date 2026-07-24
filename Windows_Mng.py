import os, subprocess, time, webbrowser


# little def's

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_option():
    while True:
        opc = input("    \033[1;38;5;208mOption: \033[0m").strip()
        if opc == "":
            return 0
        try:
            return int(opc)
        except ValueError:
            valid()
def confirmation():
    resposta = input("     \033[32mcontinue...\033[0m")
def valid():
    print("  \033[31mSelect Valid Option...\033[0m");
    time.sleep(0.5)


def menu_spacing():
    print("\033[1m |                                                      |\033[0m")
def bar():
    print("\033[1m#========================================================#\033[0m")

#  Intro

def intro():
    print("\n\033[1;38;2;124;77;255m Pinalto's Manager  '\033[0m")
    for i in range(4):
        clear_console();    bar();      print(f"\033[1m |\033[1;34mLoading Windows Version{'.' * i}\033[0m");       bar()
        time.sleep(0.15)

#  Windows Section

def windows_main_menu_print():
    clear_console();
    print(f"\033[1;38;2;124;77;255m  ----< {time.strftime('%H:%M')} >----< Pinalto's Windows Manager >-------\033[0m");                                 bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜\033[0m \033[1;38;2;216;200;255mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜\033[0m \033[1;38;2;216;200;255mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜\033[0m \033[1;38;2;216;200;255mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜\033[0m \033[1;38;2;216;200;255mLink Manager\033[0m                                    |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m9 ➜\033[0m \033[1;38;2;216;200;255mShutdown /s /f /t 0\033[0m                             |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜\033[0m \033[1;38;2;255;107;107mQuit\033[0m                                            |\033[0m");    bar()


# Option 1 System Update

def update():
    t = time.time();    clear_console()
    print("             ----- Updating System -----  ");        bar()
    cmd = (
        'winget upgrade --all --silent --accept-source-agreements --accept-package-agreements && '
        'DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase && '
        'cleanmgr /sagerun:1'
    )
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("[ok] update + cleanup")
    except subprocess.CalledProcessError:
        print("[erro] update + cleanup")

    bar();  print(f"\033[1;93mElapsed time: {time.time() - t:.4f}\033[0m");     bar();      confirmation()


# Option 2 Setup Options
def windows_opc3_menu_print():
    clear_console();    print(f"\033[1;38;2;124;77;255m                 Setup Menu...\033[0m");     bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜\033[0m \033[1;38;2;216;200;255mDownload Utilities Packages\033[0m                    |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜\033[0m \033[1;38;2;216;200;255mDownload Gaming Packages\033[0m                       |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜\033[0m \033[1;38;2;216;200;255mDownload Work Tools Packages\033[0m                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜\033[0m \033[1;38;2;216;200;255mDownload All Packages\033[0m                          |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m5 ➜\033[0m \033[1;38;2;216;200;255mPackages Info\033[0m                                  |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜\033[0m \033[1;38;2;255;107;107mLeave\033[0m                                         |\033[0m");  bar()


def install(package_id):
    subprocess.run([
        "winget", "install",
        "--accept-source-agreements",
        "--accept-package-agreements",
        "-e", "--id", package_id
    ])


def windows_download_utilitaries():
    install("Python.Python.3.13");  install("Git.Git");      install("python.Python.3.12")
    install("RARLab.WinRAR");       install("VideoLAN.VLC"); install("Microsoft.PowerToys")
    install("ImputNet.Helium");     install("Brave.Brave");  install("Rufus.Rufus")
    install("AntibodySoftware.WizTree");                     install("KDE.Kate")


def windows_download_gaming():
    install("Valve.Steam");     install("Discord.Discord");     install("PrismLauncher.PrismLauncher")
    install("CPUID.CPU-Z");     install("YoutubeMusicDesktopApp.YoutubeMusicDesktopApp")
    install("MullvadVPN.MullvadVPN");                           install("Logitech.GHUB")
    install("Guru3D.Afterburner");                              install("EpicGames.EpicGamesLauncher")
    install("WeMod.WeMod")


def windows_download_worktools():
    install("GNU.Wget2");   install("Microsoft.VisualStudioCode")
    install("OBSProject.OBSStudio");    install("HandBrake.HandBrake")
    install("TheDocumentFoundation.LibreOffice")

def windows_download_all():
    windows_download_utilitaries();     windows_download_worktools();       windows_download_gaming();      update()

def windows_show_packages():
    print("\033[1;38;2;124;77;255m         === UTILITIES ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Git, Python, WinRAR, LibreOffice, VLC, Helium Browser, Brave Browser, WizTree, Rufus, Kate\033[0m")
    print("\n\033[1;38;2;124;77;255m         === GAMING ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Steam, Prism Launcher, CPU-Z, YouTube Music Desktop, Mullvad VPN, Playnite, WeMod, Epic Games, Discord\033[0m")
    print("\n\033[1;38;2;124;77;255m        === WORK TOOLS ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Visual Studio Code, Git, Python, Wget, OBS Studio, Nmap, HandBrake\033[0m")


def windows_setup():
    while True:
        windows_opc3_menu_print()
        try:
            opc = get_option()
        except ValueError:
            valid();    continue
        if opc == 1:    windows_download_utilitaries()
        elif opc == 2:  windows_download_gaming()
        elif opc == 3:  windows_download_worktools()
        elif opc == 4:  windows_download_all()
        elif opc == 5:  windows_show_packages(); confirmation()
        else:
            break


# Option 3 Components Listing

def windows_list_components():
    clear_console();    print("\n\033[1;38;2;124;77;255m                  --- COMPONENTS ---                          \033[0m");        bar()
    time_start = time.time()

    result = subprocess.run(
        "systeminfo",
        capture_output=True,
        text=True,
        shell=True
    )
    text = result.stdout
    print(text)

    #Copies Output to tray
    subprocess.run("clip", input=result.stdout, text=True, shell=True)

    time_end = time.time()
    bar();  print(f" \033[1;93mElapsed time: {time_end - time_start:.4f}\033[0m\n  \033[1;92mCopied Text Output to Clipboard...\033[0m");   bar();confirmation()


# Option 4 Link Manager

def links_manager_print():
    clear_console();    print(f"\033[1;38;2;124;77;255m                Link Manager...\033[0m");    bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜\033[0m \033[1;38;2;216;200;255mPinalto's PcManager\033[0m                             |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜\033[0m \033[1;38;2;216;200;255mFsOS Homepage\033[0m                                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜\033[0m \033[1;38;2;216;200;255mSilent Hill Native PC (Linux/Win) (.ISO needed)\033[0m |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜\033[0m \033[1;38;2;216;200;255mSteam Achievement Unlocker\033[0m                      |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m5 ➜\033[0m \033[1;38;2;216;200;255mHelium Browser\033[0m                                  |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜\033[0m \033[1;38;2;255;107;107mLeave\033[0m                                          |\033[0m")
    bar()


def links_manager():
    while True:
        links_manager_print()
        opc = get_option()
        if opc == 1:
            webbrowser.open("https://github.com/GabeSvbr/Pinaltos_PcManager")
        elif opc == 2:
            webbrowser.open("https://fsosx.com/")
        elif opc == 3:
            webbrowser.open("https://github.com/SlickAmogus/silent-hill-pc-nightly")
        elif opc == 4:
            webbrowser.open("https://github.com/asdfghj1237890/SteamAchievementManager-Enhanced")
        elif opc == 5:
            webbrowser.open("https://github.com/imputnet/helium-windows")
        else:
            break


# Option 9 Full-Shutdown
def shutdown():
    os.system("shutdown /s /f /t 0")

# Main Navigator

def menu_windows():
    cont1 = 0
    intro()
    while cont1 == 0:
        windows_main_menu_print()
        try:
            opc = get_option()
        except ValueError:
            valid(); continue
        if opc == 1:    update()
        elif opc == 2:  windows_setup()
        elif opc == 3:  windows_list_components()
        elif opc == 4:  links_manager()
        elif opc == 9:  shutdown()
        else:
            cont1 += 1; clear_console()

#    -MAIN-

def main():
    menu_windows()


# ===================================================== RUN ====================================================#"
main()
