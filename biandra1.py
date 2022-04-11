import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split("\n")
profiles = [i.split(":")[1][1:-1]for i in data if "All User Profile" in i]
for i in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split("\n")
        result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
        try:
            print ("{:<40}| {:<}".format(i, result[0]))
        except IndexError:
            print ("{:<40}| {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<40}| {:<}".format(i, "ENCODING ERROR"))
input('')