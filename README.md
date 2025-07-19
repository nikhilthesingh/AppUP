Ever noticed how the Microsoft Store effortlessly updates its pre-installed apps with a single click, but leaves apps like Chrome, Capcut, Zoom, or VLC out in the cold? <br>
Now tired of manually checking for updates or downloading installers for each application?

The solution you've been waiting for:

  ## 🚀 Overview
  <table>
    <tr>
      <td>
        <b>AppUP</b> is a retro matrix-styled, Python-based CLI tool that updates most of the known apps on your PC which you may have installed outside the store.<br>
            It automates the process of checking for and updating most of the applications that are ignored by the Microsoft Store, saving you time and hassle.<br>
            With AppUP, you can keep all your essential software up to date—effortlessly.<br>
          <br>
          <sub>Built by Nikhil Kumar, CSE student</sub>
      </td>
      <td align="right" valign="top" width="120">
        <img src="icon.ico" alt="AppUP Logo" width="100"/>
      </td>
    </tr>
  </table>

## ✨ Features
   - Automatically checks for updates for popular apps not available on the Microsoft Store (e.g., Chrome, Zoom, VLC, Capcut, and over 1500 additional apps)
  - Shows both the current version and the available update version for each app
  - Update all apps at once with a single click, or choose specific apps to update individually
  - Python-based CLI for easy extensibility
  - Notifies successful updates and alerts if something goes wrong
  - Retro-styled hacking vibe—play it cool in front of friends and feel like you're in a sci-fi movie!

---

## 🏁 Getting Started

### 🖥️ <ins>For Users Running the Executable</ins> (Recommended)
<div align="left">
<kbd style="background:#ffe066; color:#222; padding:6px 12px; border-radius:6px; font-size:1.1em;">�️ <b>Prerequisites</b></kbd>
</div>

<ul style="background:#fffbe6; border-left:4px solid #ffe066; padding:8px 16px;">
  <li><i>Windows 11 or 10 version 1809 (build 17763) or later.</i></li>
</ul>

1. Download `appup-update-engine.exe` from the `bin/` folder in this repository or from GitHub Releases.

     > 🛡️ **Virus Scanned**: This executable was scanned with VirusTotal  
     > [[Click Here To See Reports]](https://www.virustotal.com/gui/file/0dc9936776f9f39a2a2c882385de0736df1cd83eba3ceec68510cadd5126a371)  
     > ✅ 68 out of 72 antivirus engines marked it **clean**. A few AI-based engines raised false positives, which is common for Python-based `.exe` files built with PyInstaller.

2. Right-click `AppUp.exe` and select **Run as administrator** for a seamless update experience.  
     *Note: Running without administrator privileges may trigger Windows permission pop-ups during updates.*

3. Run `AppUP.exe`.

4. AppUP automatically performs a first-time setup to configure the Windows Package Manager (winget) on your system.

5. Wait a few seconds for AppUP to scan and display a table of available updates, showing each app’s current version and the latest available version.

6. Select apps to update:  
     - Enter numbers (e.g., `1,3`) to update specific apps.  
     - Enter `a` to update all apps.  
     - Enter `q` to abort and exit.

7. Sit back while AppUP downloads and installs the selected packages.  
     *Note: Download times may vary depending on your internet speed and the size of each update.*

8. Receive notifications for successful updates or alerts if any issues occur.

<br>

### 🐍 <ins>For Users Running the Python Script</ins>
<div align="left">
<kbd style="background:#b3e6ff; color:#222; padding:6px 12px; border-radius:6px; font-size:1.1em;">� <b>Python Script Prerequisites</b></kbd>
</div>

<ul style="background:#e6f7ff; border-left:4px solid #b3e6ff; padding:8px 16px;">
  <li><i>Python 3.10 or higher</i></li>
  <li><i>A code editor installed on your PC</i></li>
</ul>

<span style="color:#0077b6; font-style:italic;">⚠️ These prerequisites are only needed if you plan to run the Python script manually. If you use the AppUP.exe file, no additional installation is required.</span>



1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/appup-update-engine.git
   cd appup-update-engine
   ```

2. Install the required dependency:
   ```sh
   pip install rich
   ```

3. Run the script:
   ```sh
   python ver5_deep.py
   ```

4. Refer to <b>steps 4–8</b> in the section above to complete the update process.

<br>

---
## 🧰 Tech Stack
- **Python 3.x**: Core programming language.
- **rich**: Library for dynamic terminal UI with tables and animations.
- **Standard Libraries**: `subprocess`, `sys`, `time`, `random`, `threading`.
- **PyInstaller**: Generates the standalone executable.
- **Windows Package Manager**: For scanning the avilable updates.


## 🛠️ Troubleshooting

Here are solutions to some common problems you may encounter:
- **AppUP opens to a blank terminal window:**
  - Heavy background processes may slow down startup—try closing unnecessary programs.
  - Ensure both Microsoft Visual C++ 2015-2019 Redistributable [(x64)](https://aka.ms/vs/16/release/vc_redist.x64.exe) and [(x86)](https://aka.ms/vs/16/release/vc_redist.x86.exe) are installed, as these are required for many apps to run properly.

- **winget not found or not working:**
  - Ensure you are running Windows 10/11 with the Windows Package Manager installed. You can get it from the Microsoft Store if missing.

- **Python script fails with missing module error:**
  - Run `pip install rich` in your terminal to install the required dependency.

- **Updates fail or apps do not install:**
  - Check your internet connection.
  - Make sure you have administrator privileges.
  - Some apps may require you to close them before updating.
