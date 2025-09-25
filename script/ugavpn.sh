#!/bin/sh

{
  read -r USERNAME
  read -r PASSWORD
} < ~/ensimag/credentials.txt

echo $PASSWORD | sudo openconnect -u $USERNAME --passwd-on-stdin --authgroup="Etudiants de Grenoble INP" vpn.grenet.fr
