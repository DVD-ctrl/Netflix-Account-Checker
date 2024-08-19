
Netflix Account Checker

This script verifies the validity of Netflix accounts using Selenium WebDriver. It logs in to accounts provided in a file and checks if the login is successful.

🚀 Features

- Account Verification: The script logs into Netflix accounts using provided email and password.
- Parallel Execution: Supports multiple threads to perform checks simultaneously.
- Valid Account Logging: Valid accounts are saved to a `valid.txt` file.

📦 Requirements

- Python 3.x
- Selenium
- Colorama
- ChromeDriver

🔧 Installation

1. Clone the repository:

   ```
   git clone https://github.com/DVD-ctrl/Netflix-Account-Checker
   cd netflix-account-checker
   ```

2. **Install dependencies:**

   ```bash
   pip install selenium colorama


3. **Download ChromeDriver** compatible with your version of Google Chrome [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place the executable in the same directory as the script.

## 📋 Usage

1. **Prepare your accounts file:** Create a file named `combo.txt` with each account in the format `email:password`.

2. **Run the script:**

   ```bash
   python script.py
   ```

3. **Choose the scan speed:** After starting the script, you will be prompted to choose a scan speed. Select a value from 1 to 5, where 1 is slower and 5 is faster.

4. **Monitor the progress:** The script will print whether accounts are valid or invalid to the console and save valid accounts to `valid.txt`.

## 🔧 Example Usage

```plaintext
Choose the scan speed (1 to 5): 3
Attempting login with: example@email.com
Valid account: example@email.com
```

## ⚠️ Warnings

- Using multiple threads may overload the Netflix server. Use responsibly.
- The script may be blocked if used excessively or abusively.

## 📝 Contributions

Feel free to contribute to this project. Submit pull requests or open issues if you find any bugs.


## 📞 Contact

If you have questions or need support, contact me via [Discord](https://discord.gg/bjdY9S96M3) or [GitHub](https://github.com/DVD-ctrl).


