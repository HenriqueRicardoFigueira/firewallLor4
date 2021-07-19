#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file = open("/etc/FirewallLora/hosts_denied.txt", "a+")
    commands = """
    Gateway não transmite pacotes vindos deste dispositovo:  add INPUT  *deviceAddress*  DROP
    Gateway não recebe pacotes vindos deste dispositovo:  add OUTPUT  *deviceAddress*  DROP
    Remover regra:  remove *deviceAddress* 
    Start Gateway: start gw
    Restart Gateway: restart gw
    Stop Gateway: stop gw
    Sair do programa: exit
    Exibir comandos novamente: help
    """
    print("Firewall for Gateways LoraWAN")
    print(commands)

    while True:
        command = raw_input(' ')

        if  "help" in command:
            print(commands)
        
        if "add" in command:
            rule = command.lower().strip(" ");
            file.write(rule);

        if  "exit" in command:
            file.close();
            print("powerby bobramixx")
            break;