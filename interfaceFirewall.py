#!/usr/bin/python
# -*- coding: utf-8 -*-
# Start Gateway: start gw
# Restart Gateway: restart gw
 # Stop Gateway: stop gw

import os
import json

if __name__ == '__main__':
    ruleslist = {"nodes":[]}
    abspath = os.getcwd()
    file = open(abspath + "/firewall_conf.json", "a+")
    sizefile = os.path.getsize(abspath + "/firewall_conf.json")
    datafile = "";
   

    commands = """
    Adiciona dispositivos a White List:  add *deviceAddress* white
    Adiciona dispositivos a Black List:  add *deviceAddress* black
    Adiciona dispositvos a Hosts.deny:  add *deviceAddress* deny
    Adiciona dispositvos a Hosts.allow:  add *deviceAddress* allow

    Remover regra:  remove *deviceAddress* 
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
            rule_parse = command.lower().split(" ");
            ruleslist["nodes"].append({ "addr": rule_parse[1], "rule": rule_parse[2] })

        if  "exit" in command:
            if sizefile > 0:
                datafile = json.loads(file.read())
                file.truncate(0);
                for rule in ruleslist["nodes"]:
                    datafile["firewall_conf"]["nodes"].append(rule)
            else:
                datafile = {"firewall_conf": {
		                        "nodes":   ruleslist["nodes"]
	                            }}
            json.dump(datafile, file, indent = 6)
            file.close();
            print("powerby bobramixx")
            break;