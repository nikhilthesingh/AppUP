import subprocess
import sys
import time
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.align import Align
from rich.rule import Rule

console = Console()

# ======================== UI ENHANCEMENTS ======================== #

def typewriter(text, style="", delay=0.03, center=True):
    """Simulate typing effect for terminal text with improved pacing"""
    temp_text = Text()
    for char in str(text):
        temp_text.append(char, style=style)
        if center:
            console.print(Align.center(temp_text), end="\r")
        else:
            console.print(temp_text, end="\r")
        time.sleep(delay * random.uniform(0.8, 1.2))  # Variable speed for natural feel
    console.print()

def type_effect(text, style=None, speed=0.03, random_speed=True):
    """Simulate typing effect character by character"""
    for char in text:
        console.print(char, style=style, end='')
        time.sleep(speed * (0.5 + random.random() if random_speed else 1))
        sys.stdout.flush()
    console.print()

def dramatic_spinner(text):
    """Enhanced spinner with random style"""
    spinner_types = ["dots", "dots12", "line", "bouncingBar", "arc", "circleHalves", "circleQuarters"]
    with console.status(f"[dim]{text}[/]", spinner=random.choice(spinner_types), speed=random.uniform(0.6, 0.9)):
        time.sleep(random.uniform(0.8, 1.5))

def show_banner():
    """Minimalist professional banner with impactful animations"""
    console.print("\n")
    dramatic_spinner("Initializing core systems")
    typewriter("LOADING", style="bold sea_green3", delay=0.05)
    banner_text = Text()
    banner_text.append("APPLICATION UPDATE ", style="bold light_goldenrod1")
    banner_text.append("CONTROL CENTER", style="bold misty_rose1")
    banner_panel = Panel.fit(
        banner_text,
        border_style="khaki1",
        subtitle="[dim]v1.0.0 | © Nikhil Kumar[/dim]",
        padding=(1, 2),
        box=box.DOUBLE_EDGE
    )
    console.print(Align.center(banner_panel))
    contact_line = Text()
    contact_line.append("└── ", style="khaki1 dim")
    contact_line.append("Click to ", style="bold dim")
    contact_line.append(
        "Contact",
        style="underline bright_blue link https://linktr.ee/the_nikhil"
    )
    contact_line.append(" ──┘", style="khaki1 dim")  
    console.print(Align.center(contact_line))
    console.print()
    #console.print(Align.center(Rule(style="grey50")))
    dramatic_spinner("Establishing secure repository connection")
    typewriter("CONNECTION ESTABLISHED", style="bold spring_green2", delay=0.03)
    console.print("\n")

def show_status(message, status="info"):
    """Uniform status messages with consistent styling"""
    status_styles = {
        "info": "bold cadet_blue",
        "success": "bold medium_spring_green",
        "warning": "bold light_goldenrod1",
        "error": "bold red",
        "system": "bold light_sky_blue1"
    }
    prefix = {
        "info": "⎹ INFO",
        "success": "⎹ SUCCESS",
        "warning": "⎹ WARNING",
        "error": "⎹ ERROR",
        "system": "⎹ SYSTEM"
    }
    console.print(f"{prefix[status]} [{status_styles[status]}]{message}[/]", justify="left")

def display_apps(apps):
    """Redesigned apps table with better colors"""
    if not apps:
        return

    console.print(Align.center(Rule("[bold orchid]PACKAGE UPDATES AVAILABLE[/]", style="grey50")))
    table = Table(
        title="[cornsilk1]🔄 AppUp Updates[/]",
        box=box.ROUNDED,
        header_style="bold light_sky_blue1",
        border_style="grey35",
        #row_styles=["none", "dim"],   #to alter the dim effect in the table
        title_style="on dark_slate_gray"
    )
    table.add_column("Index", justify="right", width=6, style="bold sky_blue2")
    table.add_column("Application", style="light_steel_blue1", no_wrap=False, max_width=38)
    table.add_column("Current", style="light_salmon1", no_wrap=True)
    table.add_column("Available", style="pale_green1", no_wrap=True)

    for idx, (name, current, new, _) in enumerate(apps, 1):
        table.add_row(str(idx), name, current, new)

    console.print(Align.center(table))
    console.print(Align.center(Rule(style="grey50")))
    console.print(Align.center("[dim]Note: Truncated names will upgrade correctly via App ID[/]"))
    console.print()

def upgrade_progress(app_name, current, new, app_id):
    """Clean version: show download/install as spinners based on real Winget output"""
    from threading import Thread

    console.print(f"\n⎹ SYSTEM [bold cornflower_blue]PROCESSING: {app_name}[/]")
    console.print(f"⎹ [dim]Current: {current} → Target: [bold pale_green1]{new}[/]\n")

    # Show license info (mimicking Winget)
    console.print("[dim yellow] License Notice:[/]")
    console.print("[dim] This application is licensed to you by its owner.[/]")
    console.print("[dim] Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.[/]\n")

    try:
        process = subprocess.Popen(
            ["winget", "upgrade", "--id", app_id, "--accept-package-agreements", "--accept-source-agreements"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        downloading_done = False
        installing_shown = False

        def monitor_output():
            nonlocal downloading_done, installing_shown
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                line = line.strip().lower()

                if "Downloading http" in line and not downloading_done:
                    downloading_done = True
                elif ("installing" in line or "Starting package install" in line) and not installing_shown:
                    installing_shown = True

        monitor_thread = Thread(target=monitor_output)
        monitor_thread.start()

        # Wait for download detection
        with console.status("[bold light_sky_blue1]Downloading application package...[/]", spinner="arc"):
            while not downloading_done and process.poll() is None:
                time.sleep(0.1)

        # Wait for install detection
        with console.status("[bold spring_green2]Installing the package...[/]", spinner="bouncingBar"):
            while not installing_shown and process.poll() is None:
                time.sleep(0.1)

        monitor_thread.join()

        # Final status check
        if process.wait() == 0:
            show_status(f"{app_name} updated successfully", "success")
            return True
        else:
            show_status(f"Failed to update {app_name} (exit code {process.returncode})", "error")
            return False

    except Exception as ex:
        show_status(f"Unexpected error: {str(ex)}", "error")
        return False


# ======================== CORE LOGIC ======================== #

def check_winget_installed():
    """Check if winget is available"""
    try:
        subprocess.run(["winget", "--version"], check=True, capture_output=True, text=True)
        return True
    except FileNotFoundError:
        show_status("winget is not installed. Please install it from the Microsoft Store or enable it in Windows settings.", "error")
        show_status("Visit https://learn.microsoft.com/en-us/windows/package-manager/winget/ for instructions.", "info")
        return False
    except subprocess.CalledProcessError:
        show_status("winget is installed but failed to run. Please ensure it's properly configured.", "error")
        return False

def check_winget_ready():
    """Check if winget is ready for use"""
    try:
        result = subprocess.run(["winget", "list"], capture_output=True, text=True, timeout=10)
        return "must be accepted" not in result.stderr.lower()
    except subprocess.SubprocessError:
        return False

def handle_first_time_setup():
    """Guide user through initial winget setup"""
    show_status("First-time configuration required", "system")
    with console.status("[dim]Configuring package manager...[/]", spinner="bouncingBar"):
        try:
            result = subprocess.run(
                ["winget", "upgrade", "--accept-source-agreements"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                show_status("Package manager configured successfully", "success")
                return True
        except subprocess.SubprocessError:
            pass
        show_status("Manual configuration required.", "warning")
        show_status("Open the Windows Terminal (search for 'Terminal' in Start menu).", "info")
        show_status("Copy and paste the following command, then press Enter:", "info")
        console.print("[bold yellow]winget upgrade --accept-source-agreements[/]")
        return False

def get_upgradable_apps():
    """Fetch list of upgradable apps using winget"""
    with console.status("[dim]Scanning the system for installed packages...[/]", spinner="dots", speed=0.8):
        time.sleep(4)
    try:
        result = subprocess.run(["winget", "upgrade"], capture_output=True, text=True, timeout=30)
        if result.stderr and ("must be accepted" in result.stderr.lower() or "source agreements" in result.stderr.lower()):
            handle_first_time_setup()
        if result.returncode != 0:
            console.print(f"[red]Error running update engine: {result.stderr or result.stdout}[/red]")
            sys.exit(1)
        lines = result.stdout.splitlines()
        apps = []
        parsing = False
        col_positions = {}
        for idx, line in enumerate(lines):
            if line.strip().startswith("Name"):
                parsing = True
                header = line
                col_positions['name'] = header.index("Name")
                col_positions['id'] = header.index("Id")
                col_positions['version'] = header.index("Version")
                col_positions['available'] = header.index("Available")
                continue
            if not parsing or line.strip() == "" or "---" in line or line.strip().startswith("Source"):
                continue
            try:
                name = line[col_positions['name']:col_positions['id']].strip()
                app_id = line[col_positions['id']:col_positions['version']].strip()
                current_version = line[col_positions['version']:col_positions['available']].strip()
                available_version = line[col_positions['available']:].strip().split()[0]
                if name and current_version and available_version and app_id:
                    apps.append((name, current_version, available_version, app_id))
            except Exception:
                continue
        return apps
    except subprocess.SubprocessError as e:
        console.print(f"[red]Error running update engine: {e}[/red]")
        sys.exit(1)

def prompt_and_upgrade(apps):
    """Handle user selection and perform upgrades"""
    if not apps:
        return
    console.print(Align.center(Panel(
        "[bold]Select applications to upgrade:[/]\n\n"
        "[deep_sky_blue1]• Enter index numbers (e.g. '1,3')\n"
        "[pale_green1]• Enter 'a' to upgrade all\n"
        "[light_goldenrod1]• Enter 'q' to quit[/]",
        border_style="medium_purple1" ,
        box=box.ROUNDED
    )))

    while True:
        try:
            choice = console.input("\n⎹ [cornsilk1]Selection:[/] ").strip().lower()
            if choice == 'q':
                show_status("Operation cancelled", "warning")
                return
            if choice == 'a':
                selected = apps
                show_status(f"Confirmed: FULL SYSTEM UPDATE ({len(selected)} targets)", "system")
                break
            indices = [int(x.strip()) - 1 for x in choice.split(",") if x.strip().isdigit()]
            selected = [apps[i] for i in indices if 0 <= i < len(apps)]
            if selected:
                show_status(f"Confirmed: TARGETED UPDATE ({len(selected)} targets)", "system")
                break
            console.print("[light_coral]Invalid selection - try again[/]")
        except ValueError:
            console.print("[light_coral]Invalid input format - try again[/]")

    success_count = 0
    for name, current, new, app_id in selected:
        if upgrade_progress(name, current, new, app_id):
            success_count += 1

    console.print()
    if success_count == len(selected):
        show_status(f"All {success_count} packages updated successfully", "success")
    elif success_count > 0:
        show_status(f"Updated {success_count}/{len(selected)} packages", "success")
    else:
        show_status("No packages were successfully upgraded", "warning")

    console.print(Align.center(Rule("[bold]OPERATION COMPLETE[/]", style="bright_blue")))

# ======================== MAIN EXECUTION ======================== #

if __name__ == "__main__":
    type_effect("Starting AppUp Update Engine...", style="bold light_sky_blue1", speed=0.03)
    console.print()
    show_banner()
    
    # Verify winget availability
    if not check_winget_installed():
        sys.exit(1)

    # Check if ready to use
    if not check_winget_ready():
        if not handle_first_time_setup():
            show_status("Setup incomplete - cannot continue", "error")
            sys.exit(1)

    # Get upgradable apps
    apps = get_upgradable_apps()
    if apps:
        type_effect(f"> Found {len(apps)} outdated package{'s' if len(apps) != 1 else ''} :", "bold magenta")
    else:
        type_effect("No Upgradable Apps Found", style="bold green", speed=0.03)
    console.print()
    display_apps(apps)

    # Start upgrade process
    if apps:
        prompt_and_upgrade(apps)

    console.print()
    contact_text = Text("Feedback? Contact: ", style="dim")
    contact_text.append(
        "linktr.ee/the_nikhil", 
        style="bold bright_blue underline link https://linktr.ee/the_nikhil"  
    )
    console.print(Align.center(contact_text))
    console.print()
    console.input(Align.center(Text(">>> Press Enter to Exit <<<", style="light_sky_blue1")))
    console.print()
    type_effect("Shutting Down AppUp Update Engine...", style="bold cornflower_blue", speed=0.03)
    dramatic_spinner("Securing system state")
    console.print(Align.center("[grey50]───── AppUp Update Engine Terminated ─────[/]"))
    console.print(Align.center(
    Text("───── A project by ", style="dim") + 
    Text("NIKHIL KUMAR", style="light_salmon1") + 
    Text(" ─────", style="dim")
    ))