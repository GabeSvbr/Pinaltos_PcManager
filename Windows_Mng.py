import os, subprocess, time, webbrowser, winreg
version = "Version 1.37"

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
        clear_console();bar()
        print(f"\033[1m |\033[1;34m --> {version}\033[0m")
        print(f"\033[1m |\033[1;34m Loading Windows Version{'.' * i}\033[0m");       bar()
        time.sleep(0.25)

#  Windows Section

def windows_main_menu_print():
    clear_console();
    print(f"\033[1;38;2;124;77;255m  ----< {time.strftime('%H:%M')} >----< Pinalto's Windows Manager >-------\033[0m");                                 bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜ \033[0m \033[1;38;2;216;200;255mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜ \033[0m \033[1;38;2;216;200;255mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜ \033[0m \033[1;38;2;216;200;255mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜ \033[0m \033[1;38;2;216;200;255mLink Manager\033[0m                                    |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m9 ➜ \033[0m \033[1;38;2;180;0;0mShutdown /s /f /t 0\033[0m                                 |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜ \033[0m \033[1;38;2;255;107;107mQuit\033[0m                                            |\033[0m");    bar()


# Option 1 System Update

def update():
    t = time.time();    clear_console()
    print("\n\033[1;38;2;124;77;255m                  --- Updating ---                          \033[0m");        bar()
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

    bar();  print(f"\033[1;93mElapsed time: {time.time() - t:.4f}\033[0m");     bar()


# Option 2 Setup Options
def windows_setup_menu_print():
    clear_console();    print(f"\033[1;38;2;124;77;255m                     --> Setup Menu <-- \033[0m");     bar()
    print("\033[1m |    \033[1;38;2;124;77;255m1 ➜ \033[0m \033[1;38;2;216;200;255mDownload Utilities Packages\033[0m                  |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m2 ➜ \033[0m \033[1;38;2;216;200;255mDownload Gaming Packages\033[0m                     |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m3 ➜ \033[0m \033[1;38;2;216;200;255mDownload Work-Tools Packages\033[0m                 |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m4 ➜ \033[0m \033[1;38;2;216;200;255mDownload All Packages\033[0m                        |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m5 ➜ \033[0m \033[1;38;2;216;200;255mPackages Info\033[0m                                |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m6 ➜ \033[0m \033[1;38;2;255;165;0mCustom Windows Setup\033[0m                         |\033[0m")
    print("\033[1m |    \033[1;38;2;255;107;107m0 ➜ \033[0m \033[1;38;2;255;107;107mLeave\033[0m                                        |\033[0m");  bar()


def install(package_id):
    print(f"\033[1;38;2;124;77;255m>>  Now Installing ➜  \033[1;38;2;255;105;180m({package_id})\033[0m")
    subprocess.run([
        "winget", "install",
        "--accept-source-agreements",
        "--accept-package-agreements",
        "-e", "--id", package_id
    ])


def windows_download_utilitaries():
    install("Microsoft.PowerToys");install("Python.Python.3.13");install("ImputNet.Helium")
    install("RARLab.WinRAR");install("VideoLAN.VLC");install("Brave.Brave")
    install("Rufus.Rufus");install("KDE.Kate");install("AntibodySoftware.WizTree")


def windows_download_gaming():
    install("Valve.Steam");     install("Discord.Discord");     install("PrismLauncher.PrismLauncher")
    install("WeMod.WeMod");     install("Vendicated.Vencord");  install("th-ch.YouTubeMusic")


def windows_download_worktools():
    install("AnyDesk.AnyDesk");     install("Microsoft.VisualStudioCode");          install("OBSProject.OBSStudio")
    install("TheDocumentFoundation.LibreOffice");   install("Guru3D.Afterburner");  install("HandBrake.HandBrake")

def windows_download_all():
    windows_download_utilitaries();     windows_download_worktools();       windows_download_gaming();      update()

def windows_show_packages():
    print("\033[1;38;2;124;77;255m         === UTILITIES ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: PowerToys, Python 3.13, Helium Browser, WinRAR, VLC, Brave Browser, Rufus, Kate, WizTree\033[0m")

    print("\n\033[1;38;2;124;77;255m         === GAMING ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Steam, Discord, Prism Launcher, WeMod, Vencord, YouTube Music Desktop\033[0m")

    print("\n\033[1;38;2;124;77;255m        === WORK TOOLS ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: AnyDesk, Visual Studio Code, OBS Studio, LibreOffice, MSI Afterburner, HandBrake\033[0m")


#   CUSTOM WINDOWS SETUP

def align_taskbar_left():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
    winreg.SetValueEx(k, "TaskbarAl", 0, winreg.REG_DWORD, 0);  k.Close()
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
    subprocess.Popen(["explorer.exe"])

def download_pinalto():
    install("Python.Python.3.13");install("ImputNet.Helium");install("Vendicated.Vencord")
def clear_taskbar():
    ps_script = r'''
    $shell = New-Object -ComObject Shell.Application
    $apps = $shell.Namespace("shell:::{4234d49b-0245-4df3-b780-3893943456e1}").Items()
    $manter = @("File Explorer", "Explorador de Arquivos", "Configurações", "Terminal", "Helium","Steam")
    foreach ($item in $apps) {
        if ($manter -contains $item.Name) {
            $item.InvokeVerb("taskbarpin")
        } else {
            $item.InvokeVerb("taskbarunpin")
        }
    }
    '''
    subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script])
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
    subprocess.Popen("explorer.exe")

def remove_bloatware():
    APPS = [
        "Microsoft.3DBuilder", "Microsoft.BingNews", "Microsoft.BingWeather",
        "Microsoft.BingFinance", "Microsoft.BingSports", "Microsoft.GetHelp",
        "Microsoft.Getstarted", "Microsoft.MicrosoftOfficeHub",
        "Microsoft.MicrosoftSolitaireCollection", "Microsoft.MixedReality.Portal",
        "Microsoft.OneConnect", "Microsoft.People", "Microsoft.Print3D",
        "Microsoft.SkypeApp", "Microsoft.WindowsAlarms", "Microsoft.WindowsFeedbackHub",
        "Microsoft.WindowsMaps", "Microsoft.WindowsSoundRecorder", "Microsoft.XboxApp",
        "Microsoft.Xbox.TCUI", "Microsoft.XboxGameOverlay", "Microsoft.XboxGamingOverlay",
        "Microsoft.XboxIdentityProvider", "Microsoft.XboxSpeechToTextOverlay",
        "Microsoft.YourPhone", "Microsoft.ZuneMusic", "Microsoft.ZuneVideo",
        "Microsoft.Todos", "Clipchamp.Clipchamp", "MicrosoftTeams",
        "Microsoft.549981C3F5F10",
    ]
    for app in APPS:
        print(f"Removendo {app}...")
        subprocess.run(
            ["powershell", "-Command",
            f"Get-AppxPackage -AllUsers -Name '*{app}*' | Remove-AppxPackage -AllUsers"],
            capture_output=True
        )

def disable_widgets():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
    winreg.SetValueEx(k, "TaskbarDa", 0, winreg.REG_DWORD, 0)  # remove ícone de Widgets
    k.Close()

def disable_search_box():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
    winreg.SetValueEx(k, "SearchboxTaskbarMode", 0, winreg.REG_DWORD, 0)  # 0=oculto, 1=ícone, 2=caixa
    k.Close()

def disable_chat_icon():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
    winreg.SetValueEx(k, "TaskbarMn", 0, winreg.REG_DWORD, 0)  # remove ícone de Chat/Teams

def show_file_extensions():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced")
    winreg.SetValueEx(k, "HideFileExt", 0, winreg.REG_DWORD, 0)  # mostra extensões de arquivo
    winreg.SetValueEx(k, "Hidden", 0, winreg.REG_DWORD, 1)       # mostra arquivos ocultos

def enable_dark_mode():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    winreg.SetValueEx(k, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(k, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 0)
    k.Close()

def classic_context_menu():
    # restaura o menu de contexto clássico do Win10 no Win11
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32")
    winreg.SetValueEx(k, "", 0, winreg.REG_SZ, "")
    k.Close()
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
    subprocess.Popen("explorer.exe")

def disable_telemetry():
    ps = '''
    Set-Service -Name DiagTrack -StartupType Disabled
    Stop-Service -Name DiagTrack -Force
    '''
    subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps])

def power_plan_high_performance():
    subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])

def disable_startup_delay():
    k = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize")
    winreg.SetValueEx(k, "StartupDelayInMSec", 0, winreg.REG_DWORD, 0)
    k.Close()


def windows_custom_setup():

    align_taskbar_left();disable_widgets();disable_chat_icon();disable_search_box();disable_startup_delay()

    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
    subprocess.Popen("explorer.exe")
    clear_taskbar()

    remove_bloatware(); download_pinalto(); disable_telemetry()


def windows_setup():
    while True:
        windows_setup_menu_print()
        try:
            opc = get_option()
        except ValueError:
            valid();    continue
        if opc == 1:    windows_download_utilitaries()
        elif opc == 2:  windows_download_gaming()
        elif opc == 3:  windows_download_worktools()
        elif opc == 4:  windows_download_all()
        elif opc == 5:  windows_show_packages(); confirmation()
        elif opc == 6:  windows_custom_setup()
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
    bar();  print(f" \033[1;93mElapsed time: {time_end - time_start:.4f}\033[0m\n  \033[1;92m           Copied Text Output to Clipboard...\033[0m");   bar();confirmation()


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
        if opc == 1:    update(); confirmation()
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

