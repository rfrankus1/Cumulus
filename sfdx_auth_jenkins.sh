export $(dbus-launch)
sfdx force:auth:jwt:grant -i 3MVG9nwRZX60mjQp0oSP00EQPP2hzp9zgpMx3PoX7O.iEPYYW.5e61_pWCv33Mzln8mk5xu4NSzSEw5.9QHjP -f ~/.ssh/server.key --setdefaultusername  -u rfrankus@sfdx-salesforce.org
sfdx force:config:set defaultdevhubusername=rfrankus@sfdx-salesforce.org
