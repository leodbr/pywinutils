from os import system
from pystyle import Write, Colors
from time import sleep
from pyuac import isUserAdmin, runAsAdmin

keys = ['W269N-WFGWX-YVC9B-4J6C9-T83GX', 'MH37W-N47XK-V7XM9-C7227-GCQG9', 'NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J', '9FNHH-K3HBT-3W4TD-6383H-6XYWF', '6TP4R-GNPTD-KYYHQ-7B7DP-J447Y', 'YVWGF-BXNMC-HTQYQ-CPQ99-66QFC', 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2', '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ', 'NPPR9-FWDCX-D2C8J-H872K-2YT43', 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4', 'YYVX9-NTFWV-6MDM3-9PT4T-4M68B', '44RPN-FTY23-9VTTB-MP9BX-T84FV']
servers = ['kms.digiboy.ir', 'hq1.chinancce.com', '54.223.212.31', 'kms.cnlic.com', 'kms.chinancce.com', 'kms.ddns.net', 'franklv.ddns.net', 'k.zpale.com', 'm.zpale.com', 'mvg.zpale.com', 'kms.shuax.com', 'kensol263.imwork.net:1688', 'xykz.f3322.org', 'kms789.com', 'dimanyakms.sytes.net:1688', 'kms.03k.org:1688']

def countdown(arg, time) :
    for i in range(time, 0, -1) :
        print(f'The program will {arg} in {i} seconds...')
        sleep(1)

def global_choice() :
    choice = int(Write.Input("""Hi, welcome to pywinactivor!\nSelect your choice :\n
    〚0〛Github Repository
    〚1〛Windows Activation
    \nYour choice : """, Colors.green, interval=0.005))
    if not 0 <= choice <= 1 :
        print("Your choice isn't between 0 and 1, try again in 5 seconds.\n")
        countdown("end", 5)
        main()
    return(choice)

def choice_key() :
    system('CLS')
    choice = int(Write.Input("""All the Windows 10/11 versions :\n
    〚0〛See your Windows Version
    〚1〛Windows 10/11 Pro
    〚2〛Windows 10/11 Pro N
    〚3〛Windows 10/11 Pro for Workstations
    〚4〛Windows 10/11 Pro for Workstations N
    〚5〛Windows 10/11 Professional Education
    〚6〛Windows 10/11 Professional Education
    〚7〛Windows 10/11 Education
    〚8〛Windows 10/11 Education N
    〚9〛Windows 10/11 Enterprise
    〚10〛Windows 10/11 Enterprise N
    〚11〛Windows 10/11 Enterprise G
    〚12〛Windows 10/11 Enterprise G N
    \nSelect your Windows version : """, Colors.green, interval=0.005))
    if not 0 <= choice <= 12 :
        system('CLS')
        print("Your choice for your Windows version isn't between 0 and 12, try again in 5 seconds.\n")
        countdown('restart', 5)
        main()
    return(choice)

def choice_server() :
    system('CLS')
    choice = int(Write.Input("All Online KMS Servers :\n\n"+"\n".join([f"    〚{i+1}〛{server}" for i, server in enumerate(servers)])+"\n\nSelect the KMS Server you want : ", Colors.green, interval=0.005))
    if not 1 <= choice <= 16 :
        system('CLS')
        print("Your choice for the KMS Server isn't between 1 and 16, try again in 5 seconds.\n")
        countdown('restart', 5)
        main()
    return(choice)

def enable_windows(key, server) :
    system('CLS')
    print(f'Your key : {key} will be activated on {server} KMS server.\nWait for 20-30 seconds and Windows should be activated.')
    system(f'slmgr /ipk {key}')
    system(f'slmgr /skms {server}')
    system('slmgr /ato')
    sleep(5)
    system('taskkill /f /im explorer.exe')
    sleep(5)
    system('start explorer.exe')

def main() :
    system('CLS')
    Colors.green
    choice = global_choice()
    if choice == 0 :
        system("start https://github.com/leodbr")
    elif choice == 1 :
        Colors.green
        choice = choice_key()
        if choice == 0 :
            system('CLS')
            print("Check the first line of the info box that will open, and the program will restart 5 seconds after you close the info box.\n")
            sleep(5)
            system('msinfo32.exe')
            countdown('restart', 5)
            main()
        else :
            key = keys[choice-1]
            server = servers[choice_server()-1]
            enable_windows(key, server)
            system('CLS')
            print("Windows is successfully enabled, please close any dialog boxes that are open.")
            countdown('end', 10)
        exit()

if __name__ == "__main__":
    if not isUserAdmin():
        system('CLS')
        print("CMD not in admin mode, restarting as admin")
        runAsAdmin()
    else:        
        main()
