`health_checker.sh` is a Bash script that when executed, it displays and captures essential *System Information*.
### What's in the script?
  - `hostname`
  - `whoami`
  - `date`
  - `uname -r`
  - `uptime`
  - `df -h`
  - `free -h`
  - `systemctl is-active apache2`
  - `systemctl is-active ssh`
```
mkdir -p logs
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
logfile="logs/system_report_$timestamp.txt"
```
> [!Note]
> If you want to execute the actual file, then go to the [repo](https://github.com/Nur-Howell/linux-system-health-checker).
