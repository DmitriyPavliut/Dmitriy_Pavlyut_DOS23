import os

def check_ping(ip_list, output_file):
    with open(output_file, "w") as file:
        for ip in ip_list:
            response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
            if response == 0:
                result = f"{ip} доступен"
            else:
                result = f"{ip} недоступен"
            print(result)
            file.write(result + "\n")


