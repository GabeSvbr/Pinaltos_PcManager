import os, sys, subprocess, time, webbrowser, winreg, ctypes,  urllib.request
version = "Version 1.77"

# Utilities
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


#   Windows Main_Menu Print
def windows_main_menu_print():
    clear_console();
    print(f"\033[1;38;2;124;77;255m  ----< {time.strftime('%H:%M')} >----< Pinalto's Windows Manager >-------\033[0m");                                 bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜ \033[0m \033[1;38;2;216;200;255mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜ \033[0m \033[1;38;2;216;200;255mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜ \033[0m \033[1;38;2;216;200;255mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜ \033[0m \033[1;38;2;216;200;255mFun Links\033[0m                                       |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m5 ➜ \033[0m \033[1;38;2;216;200;255mRefresh Windows\033[0m                                 |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m7 ➜ \033[0m \033[1;38;2;255;165;0mCustom Windows Setup (private)\033[0m                  |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m8 ➜ \033[0m \033[1;38;2;255;165;0mCustom Windows Setup (comercial)\033[0m                |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m9 ➜ \033[0m \033[1;38;2;180;0;0mShutdown /s /f /t 0\033[0m                             |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜ \033[0m \033[1;38;2;255;107;107mQuit\033[0m                                            |\033[0m");    bar()
#   System Update
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

#   Setup Options
#       Install Via Winget
def install(package_id):
    print(f"\033[1;38;2;124;77;255m>>  Now Installing ➜  \033[1;38;2;255;105;180m({package_id})\033[0m")
    subprocess.run([
        "winget", "install",
        "--accept-source-agreements",
        "--accept-package-agreements",
        "-e", "--id", package_id
    ])
#       Setup Print
def windows_setup_menu_print():
    clear_console();    print(f"\033[1;38;2;124;77;255m                     --> Setup Menu <-- \033[0m");     bar()
    print("\033[1m |    \033[1;38;2;124;77;255m1 ➜ \033[0m \033[1;38;2;216;200;255mDownload Utilities Packages\033[0m                  |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m2 ➜ \033[0m \033[1;38;2;216;200;255mDownload Gaming Packages\033[0m                     |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m3 ➜ \033[0m \033[1;38;2;216;200;255mDownload Work-Tools Packages\033[0m                 |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m4 ➜ \033[0m \033[1;38;2;216;200;255mDownload All Packages\033[0m                        |\033[0m")
    print("\033[1m |    \033[1;38;2;124;77;255m5 ➜ \033[0m \033[1;38;2;216;200;255mPackages Info\033[0m                                |\033[0m")
    print("\033[1m |    \033[1;38;2;255;107;107m0 ➜ \033[0m \033[1;38;2;255;107;107mLeave\033[0m                                        |\033[0m");  bar()
#       Download Packages From Download Menu
def windows_download_utilitaries():
    install("Python.Python.3.13");install("ImputNet.Helium")
    install("RARLab.WinRAR");install("VideoLAN.VLC");install("Brave.Brave")
    install("Klocman.BulkCrapUninstaller");install("KDE.Kate");install("AntibodySoftware.WizTree")
def windows_download_gaming():
    install("Valve.Steam");     install("Discord.Discord");     install("PrismLauncher.PrismLauncher")
    install("WeMod.WeMod");     install("Vendicated.Vencord");  install("th-ch.YouTubeMusic")
def windows_download_worktools():
    install("AnyDesk.AnyDesk");     install("Microsoft.VisualStudioCode");          install("OBSProject.OBSStudio")
    install("Rufus.Rufus")
    install("TheDocumentFoundation.LibreOffice");   install("Guru3D.Afterburner");  install("HandBrake.HandBrake")
def windows_download_all():
    windows_download_utilitaries();     windows_download_worktools();       windows_download_gaming();      update()
def windows_show_packages():
    print("\033[1;38;2;124;77;255m         === UTILITIES ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Python 3.13, Helium Browser, WinRAR, VLC, Brave Browser, Bulk Crap Uninstaller, Kate, WizTree\033[0m")
    print("\n\033[1;38;2;124;77;255m          === GAMING ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: Steam, Discord, Prism Launcher, WeMod, Vencord, YouTube Music Desktop\033[0m")
    print("\n\033[1;38;2;124;77;255m        === WORK TOOLS ===\033[0m")
    print("\033[1;38;2;216;200;255m--> winget: AnyDesk, Visual Studio Code, OBS Studio, Rufus, LibreOffice, MSI Afterburner, HandBrake\033[0m")
#windows  setup menu
def windows_setup():
    while True:
        windows_setup_menu_print()
        try:
            opc = get_option()
        except ValueError:
            valid()
            continue

        if opc == 1:    windows_download_utilitaries()
        elif opc == 2:  windows_download_gaming()
        elif opc == 3:  windows_download_worktools()
        elif opc == 4:  windows_download_all()
        elif opc == 5:  windows_show_packages();    confirmation()
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
    subprocess.run("clip", input=result.stdout, text=True, shell=True)
    time_end = time.time()
    bar();  print(f" \033[1;93mElapsed time: {time_end - time_start:.4f}\033[0m\n  \033[1;92m           Copied Text Output to Clipboard...\033[0m");   bar();confirmation()

#   Link Manager
#       Link manager print
def links_manager_print():
    clear_console();    print(f"\033[1;38;2;124;77;255m                Link Manager...\033[0m");    bar()
    print("\033[1m |  \033[1;38;2;124;77;255m1 ➜\033[0m \033[1;38;2;216;200;255mPinalto's PcManager Github Repo\033[0m                 |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m2 ➜\033[0m \033[1;38;2;216;200;255mFsOS Homepage\033[0m                                   |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m3 ➜\033[0m \033[1;38;2;216;200;255mSilent Hill Native PC (Linux/Win) (.ISO needed)\033[0m |\033[0m")
    print("\033[1m |  \033[1;38;2;124;77;255m4 ➜\033[0m \033[1;38;2;216;200;255mSteam Achievement Unlocker\033[0m                      |\033[0m")
    print("\033[1m |  \033[1;38;2;255;107;107m0 ➜\033[0m \033[1;38;2;255;107;107mLeave\033[0m                                           |\033[0m"); bar()
#       link manager menu Navigator
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
        else:
            break

#   CUSTOM WINDOWS SETUP (Commercial and Private)
def log(m): print(f"\033[1;38;2;124;77;255m>>\033[1;38;2;255;105;180m {m}\033[0m")

def set_reg(hive,path,name,tipo,valor):
    try:
        k=winreg.CreateKeyEx(hive,path,0,winreg.KEY_ALL_ACCESS);winreg.SetValueEx(k,name,0,tipo,valor);winreg.CloseKey(k);return True
    except PermissionError: print(f"Sem permissão para gravar {name} em {path}")
    except OSError as e: print(f"Falha ao gravar {name} em {path}: {e}")
    return False
#       Restart Explorer
def restart_explorer():
    log("Restarting Explorer")
    subprocess.run(["taskkill","/F","/IM","explorer.exe"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    subprocess.Popen(["explorer.exe"])
#       Align Taskbar to the left
def align_taskbar_left():
    log("Aligning Taskbar to the left")
    set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","TaskbarAl",winreg.REG_DWORD,0)
#       Debloat Windows
def debloat_windows():
    log("Debloating Windows")
    if not ctypes.windll.shell32.IsUserAnAdmin():
        params = " ".join(f'"{arg}"' for arg in sys.argv)
        if ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        ) <= 32:
            return
        sys.exit()

    ps_script = r'''
$packages = "Microsoft.3DBuilder","Microsoft.BingNews","Microsoft.BingSearch","Microsoft.BingWeather","Microsoft.GetHelp","Microsoft.Getstarted","Microsoft.GamingApp","Microsoft.Microsoft3DViewer","Microsoft.MicrosoftEdge.Stable","Microsoft.MicrosoftOfficeHub","Microsoft.MicrosoftSolitaireCollection","Microsoft.MicrosoftStickyNotes","Microsoft.MixedReality.Portal","Microsoft.NotePad","Microsoft.Office.OneNote","Microsoft.OneDrive","Microsoft.MSPaint","Microsoft.OutlookForWindows","Microsoft.Paint","Microsoft.People","Microsoft.PowerAutomateDesktop","Microsoft.SkypeApp","Microsoft.Todos","Microsoft.Wallet","Microsoft.Whiteboard","Microsoft.WindowsAlarms","Microsoft.WindowsCamera","Microsoft.Windows.DevHome","Microsoft.WindowsFeedbackHub","Microsoft.WindowsMaps","Microsoft.WindowsSoundRecorder","Microsoft.YourPhone","Microsoft.AAD.BrokerPlugin","Microsoft.Advertising.Xaml","Microsoft.Cortana","Microsoft.Services.Store.Engagement","Microsoft.Windows.Cortana","Microsoft.Win32WebViewHost","Microsoft.WindowsCommunicationsApps","Microsoft.Windows.ContentDeliveryManager","Microsoft.Windows.NarratorQuickStart","Microsoft.Windows.ParentalControls","Microsoft.Windows.PeopleExperienceHost","Microsoft.Windows.PinningConfirmationDialog","Microsoft.Windows.SecureAssessmentBrowser","Microsoft.Windows.XGpuEjectDialog","Microsoft.Windows.OOBENetworkCaptivePortal","Microsoft.Windows.OOBENetworkConnectionFlow"

foreach ($p in $packages) {
    Get-AppxPackage -AllUsers | Where-Object Name -like $p | Remove-AppxPackage -AllUsers -Confirm:$false -ErrorAction SilentlyContinue
    $pn = (Get-AppxProvisionedPackage -Online | Where-Object DisplayName -like $p).PackageName
    if ($pn) { dism.exe /Online /Remove-ProvisionedAppxPackage /PackageName:$pn *> $null }
}

"msedge","edgeupdate","edgewebview2","edgecore" | ForEach-Object { Stop-Process -Name $_ -Force -ErrorAction SilentlyContinue }
Start-Sleep 2
"msedge","edgeupdate","edgewebview2","edgecore" | ForEach-Object { Stop-Process -Name $_ -Force -ErrorAction SilentlyContinue }

"C:\Program Files (x86)\Microsoft\Edge","C:\Program Files (x86)\Microsoft\EdgeUpdate","C:\Program Files (x86)\Microsoft\EdgeWebView","C:\Program Files (x86)\Microsoft\EdgeCore","C:\Program Files\Microsoft\Edge","C:\Program Files\Microsoft\EdgeUpdate","$env:LOCALAPPDATA\Microsoft\Edge","$env:PROGRAMDATA\Microsoft\Edge" | ForEach-Object {
    if (Test-Path $_) {
        takeown /f $_ /r /d Y *> $null
        icacls $_ /grant Administrators:F /t /c /l /q *> $null
        Remove-Item $_ -Recurse -Force -ErrorAction SilentlyContinue
    }
}

New-Item "HKLM:\SOFTWARE\Microsoft\EdgeUpdate" -Force | Out-Null
New-ItemProperty "HKLM:\SOFTWARE\Microsoft\EdgeUpdate" -Name DoNotUpdateToEdgeWithChromium -Value 1 -PropertyType DWord -Force | Out-Null
"edgeupdate","edgeupdatem" | ForEach-Object { Get-Service -Name $_ -ErrorAction SilentlyContinue | Set-Service -StartupType Disabled -ErrorAction SilentlyContinue; Stop-Service -Name $_ -Force -ErrorAction SilentlyContinue }
"\Microsoft\EdgeUpdate\EdgeUpdateTaskMachineCore","\Microsoft\EdgeUpdate\EdgeUpdateTaskMachineUA" | ForEach-Object { schtasks /Change /TN $_ /Disable *> $null }
New-Item "HKLM:\SOFTWARE\Policies\Microsoft\EdgeUpdate" -Force | Out-Null
New-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\EdgeUpdate" -Name InstallDefault -Value 0 -PropertyType DWord -Force | Out-Null

"DiagTrack","dmwappushservice","Wecsvc","RemoteRegistry" | ForEach-Object { Stop-Service $_ -Force -ErrorAction SilentlyContinue; Set-Service $_ -StartupType Disabled -ErrorAction SilentlyContinue }

reg add "HKLM\Software\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f >nul 2>&1

reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v CortanaConsent /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f >nul 2>&1

reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v ContentDeliveryAllowed /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v OemPreInstalledAppsEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v PreInstalledAppsEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SilentInstalledAppsEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SystemPaneSuggestionsEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SubscribedContent-338393Enabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\CloudContent" /v DisableWindowsSpotlightFeatures /t REG_DWORD /d 1 /f >nul 2>&1
'''
    script_path = os.path.join(os.getenv("TEMP", "."), "debloat_temp.ps1")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(ps_script)
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", script_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    finally:
        if os.path.exists(script_path):
            os.remove(script_path)
#       Download and apply Wallpaper (Through Github Repos)
def download_and_apply_wallpaper(url):
    log(f"Applying Custom Wallpaper from {url}")
    if "github.com" in url and "/blob/" in url:
        url=url.replace("https://github.com/","https://raw.githubusercontent.com/").replace("/blob/","/")
    wp=os.path.join(os.environ["TEMP"],"wallpaper.jpg")
    urllib.request.urlretrieve(url,wp)
    ctypes.windll.user32.SystemParametersInfoW(20,0,wp,3)
#       Disable Widgets and Disable search box
def disable_widgets_and_search_box():
    log("Disabling Windows Widgets")
    log("Disabling Search Box")
    try:
        chave_path = r"SOFTWARE\Policies\Microsoft\Dsh"
        chave = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, chave_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(chave, "AllowNewsAndInterests", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(chave)
    except Exception as e:
        pass
    try:
        chave_path_user = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        chave = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, chave_path_user, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(chave, "TaskbarDa", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(chave)
    except Exception as e:
        pass

    set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Search","SearchboxTaskbarMode",winreg.REG_DWORD,0)
#       Show file extensions (.exe | .py | .txt)
def show_file_extensions():
    log("Show File Extensions")
    set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","HideFileExt",winreg.REG_DWORD,0)
    set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced","Hidden",winreg.REG_DWORD,1)
#       Enable ending task Through Taskbar function
def enable_end_task():
    log("Enabling Taskbar End Task")
    set_reg(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\TaskbarDeveloperSettings",
        "TaskbarEndTask",
        winreg.REG_DWORD,
        1
    )
#       Enable windows dark mode
def enable_dark_mode():
    log("Enabling Dark Mode")
    for v in ("AppsUseLightTheme","SystemUsesLightTheme"):
        set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",v,winreg.REG_DWORD,0)
#       Disable Windows Telemetry
def disable_telemetry():
    log("Disabling Telemtry")
    set_reg(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Policies\Microsoft\Windows\DataCollection","AllowTelemetry",winreg.REG_DWORD,0)
    ps="""Set-Service -Name DiagTrack -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name DiagTrack -Force -ErrorAction SilentlyContinue
    Set-Service -Name dmwappushservice -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name dmwappushservice -Force -ErrorAction SilentlyContinue"""
    subprocess.run(["powershell","-NoProfile","-ExecutionPolicy","Bypass","-Command",ps])
#       Clear Taskbar
def clear_taskbar():
    log("Cleaning Taskbar")
    ps=r'''$shell=New-Object -ComObject Shell.Application
    $apps=$shell.Namespace("shell:::{4234d49b-0245-4df3-b780-3893943456e1}").Items()
    $manter=@("File Explorer","Files","Explorador de Arquivos","Configurações","Terminal","Helium","Steam","Discord","VS Code","Kate")
    foreach($item in $apps){if($manter -contains $item.Name){$item.InvokeVerb("taskbarpin")}else{$item.InvokeVerb("taskbarunpin")}}'''
    subprocess.run(["powershell","-NoProfile","-ExecutionPolicy","Bypass","-Command",ps])
#       Set power plan to high performance
def power_plan_high_performance():
    log("Energy Plan to High Performance")
    guid="8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
    subprocess.run(["powercfg","-duplicatescheme",guid],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    subprocess.run(["powercfg","/setactive",guid])
#       Disable Startup Delay
def disable_startup_delay():
    log("Disabling Startup Delay")
    set_reg(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize","StartupDelayInMSec",winreg.REG_DWORD,0)
#       Clear Startup Menu
def reset_pins():
    log("Reseting pinned apps")
    la = os.getenv("LOCALAPPDATA")
    for p in ("explorer.exe", "StartMenuExperienceHost.exe"):
        subprocess.run(["taskkill", "/f", "/im", p], capture_output=True)
    time.sleep(1)
    s2 = f"{la}\\Packages\\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\\LocalState\\start2.bin"
    if os.path.isfile(s2): os.remove(s2)
    def rm_key(hive, path):
        try: k = winreg.OpenKey(hive, path, 0, winreg.KEY_ALL_ACCESS)
        except FileNotFoundError: return
        while True:
            try: rm_key(hive, f"{path}\\{winreg.EnumKey(k, 0)}")
            except OSError: break
        winreg.CloseKey(k); winreg.DeleteKey(hive, path)
    rm_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\CloudStore")

#   Download Commercial and Private
def download_pinalto():
    install("Python.Python.3.13");install("ImputNet.Helium");install("Discord.Discord")
def download_commercial():
    install("ImputNet.Helium")

#   Script Responsible for activating all def's
def windows_cleanup():
    align_taskbar_left();clear_taskbar();   power_plan_high_performance()
    disable_widgets_and_search_box();   enable_dark_mode();reset_pins()
    disable_startup_delay();    enable_end_task()
    debloat_windows(); disable_telemetry(); show_file_extensions(); reset_pins()
    restart_explorer()

def windows_custom_setup_commercial():
    clear_console(); log("It is advised NOT to interact with the terminal until process is finished.")
    download_commercial()
    windows_cleanup()
    download_and_apply_wallpaper("https://github.com/GabeSvbr/Pinaltos_PcManager/blob/a0fba0363c59bfc7f5815231d33a403329f5927f/Wallpapers/martin-martz-X5fEKadz0Xc-unsplash.jpg")
    log("Process Finished!"); confirmation()

def windows_custom_setup_pinalto():
    clear_console(); log("It is advised NOT to interact with the terminal until process is finished.")
    download_pinalto()
    windows_cleanup()
    download_and_apply_wallpaper("https://github.com/GabeSvbr/Pinaltos_PcManager/blob/main/Wallpapers/wallpaper%201.jpg")
    log("Process Finished!"); confirmation()

#Option 5 Windows Refresh
import ctypes, os, subprocess, time

CREATE_NO_WINDOW = 0x08000000
def _rodar(cmd):
    subprocess.run(cmd, shell=True, capture_output=True, text=True,
                    creationflags=CREATE_NO_WINDOW)
def reiniciar_explorer():
    _rodar("taskkill /f /im explorer.exe")
    time.sleep(1.5)
    subprocess.Popen("explorer.exe")
def reiniciar_driver_video():
    user32 = ctypes.windll.user32
    KEYEVENTF_KEYUP = 0x0002
    teclas = [0x11, 0x10, 0x5B, 0x42]  # Ctrl, Shift, Win, B
    for t in teclas:
        user32.keybd_event(t, 0, 0, 0); time.sleep(0.03)
    time.sleep(0.15)
    for t in reversed(teclas):
        user32.keybd_event(t, 0, KEYEVENTF_KEYUP, 0); time.sleep(0.03)
def limpar_cache_icones():
    _rodar("taskkill /f /im explorer.exe")
    time.sleep(1)
    cache = os.path.expandvars(r"%LocalAppData%\Microsoft\Windows\Explorer")
    _rodar(f'del /a /q "{cache}\\iconcache_*.db"')
    time.sleep(1)
    subprocess.Popen("explorer.exe")
def flush_dns():
    _rodar("ipconfig /flushdns")
def reiniciar_audio():
    _rodar("sc stop audiosrv")
    time.sleep(1)
    _rodar("sc start audiosrv")
def windows_refresh():
    reiniciar_audio(); reiniciar_driver_video(); flush_dns(); limpar_cache_icones()

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
        elif opc == 5:  windows_refresh()
        elif opc == 7:  windows_custom_setup_pinalto()
        elif opc == 8:  windows_custom_setup_commercial()
        elif opc == 9:  shutdown()
        else:
            cont1 += 1; clear_console()

#    -MAIN-

def main():
    menu_windows()

# ===================================================== RUN ====================================================#"
main()
