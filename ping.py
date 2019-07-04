# 1.0
import subprocess
print("Google DNS Test\n")

subprocess.run(["ping", "-c", "5", "8.8.8.8"])
subprocess.run(["traceroute", "www.google.com"])

