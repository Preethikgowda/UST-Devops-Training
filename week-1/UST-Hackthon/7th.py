import subprocess
import difflib
import datetime

SNAPSHOT_FILE = "system_snapshot.txt"


def get_system_snapshot():
    snapshot_data = []

   
    snapshot_data.append(f"Snapshot taken at: {datetime.datetime.now()}\n")

    
    snapshot_data.append("=== Installed Python Packages ===\n")
    pip_output = subprocess.getoutput("pip list")
    snapshot_data.append(pip_output + "\n")

    
    snapshot_data.append("=== Environment Variables ===\n")
    env_output = subprocess.getoutput("printenv")
    snapshot_data.append(env_output + "\n")

    
    snapshot_data.append("=== Active Users ===\n")
    users_output = subprocess.getoutput("who")
    snapshot_data.append(users_output + "\n")

    return snapshot_data

def save_snapshot(snapshot_data):
    with open(SNAPSHOT_FILE, "w") as f:
        f.writelines(snapshot_data)

def compare_snapshots(old_data, new_data):
    diff = difflib.unified_diff(
        old_data,
        new_data,
        fromfile="Old Snapshot",
        tofile="New Snapshot",
        lineterm=""
    )

    print("\n=== System Changes (Diff) ===\n")
    for line in diff:
        print(line)

if __name__ == "__main__":

    new_snapshot = get_system_snapshot()

    try:
        with open(SNAPSHOT_FILE, "r") as f:
            old_snapshot = f.readlines()

      
        compare_snapshots(old_snapshot, new_snapshot)

    except FileNotFoundError:
        print("No previous snapshot found. Creating initial snapshot...")

   
    save_snapshot(new_snapshot)

    print("\nSnapshot saved successfully.")
