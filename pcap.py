#!/bin/python3.9
import os
import signal
import subprocess

def main_menu():
    print(50 * "-")
    print("Welcome to the saving packets section")
    print(50 * "-")
    input("Press any key to start...")
    os.system("clear")
    print(50 * "-")
    print("Welcome to the main menu")
    print(50 * "-")
    print("What do you want to do?")
    print(50 * "-")
    print("tcpdump (1)")
    print("tcpreplay (2)")
    print("Exit (3)")
    print(50 * "-")
    choice = input("Please enter your choice:" + " ")
    if choice == "1":
        tcpdump()
    elif choice == "2":
        tcpreplay()
    elif choice == "3":
        os.system("clear")
        print(50 * "-")
        print("Exiting program!")
        print(50 * "-")
        input("Press any key to exit...")
        os.system("clear")
        exit()

def tcpreplay():
    print(50 * "-")
    print("Welcome to the tcpreplay section")
    print("Here you can send saved packets to calculate the bit-rate")
    print(50 * "-")
    print("Steps:")
    print("1: Open in a a new terminal 'sniffer.py'")
    print("2: Input the name of the '.pcap file' you want to send")
    print("3: Check 'sniffer.py' for the outcome (bit-rate calculation)")
    print(50 * "-")
    file_name = input("Please enter the '.pcap' file name: " + "")
    final = "/home/kali/PycharmProjects/Network/pcaps/" + file_name
    interface = input("Please enter the interface you want to send the packet to: " + "")
    command = "tcpreplay -i " + interface + " " + final
    print(command)
    print("Starting process....")
    subprocess.run(command, timeout=20, shell=True)
    print(50 * "-")
    print("Done!")
    print(50 * "-")
    print("What do you want to do?")
    print(50 * "-")
    print("Go back to the main menu (1)")
    print("Exit (2)")
    print(50 * "-")
    choice = input("Please enter your choice: " + " ")
    if choice == "1":
        os.system("clear")
        main_menu()
    elif choice == "2":
        print(50 * "-")
        print("Exiting program!")
        print(50 * "-")
        input("Press any key to exit...")
        os.system("clear")
        exit()



def tcpdump():
    print("Printing current working directory...")
    os.system("pwd")
    print(50 * "-")
    print("Please input the following variables:")
    file_name = input("Please enter the path & file name: ")
    final_address = "/home/kali/PycharmProjects/Network/pcaps/" + file_name
    interface = input("Please select and interface to listen to: " + " ")
    dst_host = input("Please enter the destination host:" + " ")
    command = "tcpdump -s 0" + " dst host " + dst_host + " -i " + interface + " -w " + final_address
    print(command)
    print(50 * "-")
    print("The file name, path and interface to listen to are:")
    print(final_address)
    print(interface)
    print(type(dst_host))
    print(command)
    print(50 * "-")
    print("Starting process...")
    try:
        subprocess.run(command, timeout=20, shell=True)
    except subprocess.TimeoutExpired:
        proces_name = "tcpdump"
        proc = subprocess.Popen(["pgrep", proces_name], stdout=subprocess.PIPE)
        # "ps ax | grep " + process_name + " | grep -v grep"
        for line in proc.stdout:
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGTERM)
            print(50 * "-")
            print("Killed process")
            print(50 * "-")
            # Check if the process that we killed is alive.
        print(50 * "-")
        print("What do you want to do?")
        print(50 * "-")
        print("Go back to the main menu (1)")
        print("Exit (2)")
        print(50 * "-")
        choice = input("Please enter your choice: " + " ")
        if choice == "1":
            os.system("clear")
            main_menu()
        elif choice == "2":
            print(50 * "-")
            print("Exiting program!")
            print(50 * "-")
            input("Press any key to exit...")
            os.system("clear")
            exit()

main_menu()
