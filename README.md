# faucet_Claimer_Bot
##This Script Was Made By Mr_Pratik(https://t.me/Robindronath_tagore)

##Join My channel for latest updates(https://t.me/cryptocurrency_bangaadesh)

# SUI Faucet Claimer Bot

This is a simple Python script designed to automate the process of claiming tokens from the SUI faucet using specified wallet addresses and proxy servers. The script can be run on Windows, Linux, and Termux (Android). 

## Features
- Loads wallet addresses and proxy servers from text files.
- Requests tokens from the SUI faucet using the loaded wallet addresses.
- Implements a round-robin proxy usage strategy.
- Automatically checks for updates from the specified GitHub repository.
- Runs continuously, with a configurable interval between requests.

## Requirements
- Python 3.x
- Git (for updates)
- Required Python libraries:
  - `requests`

## Installation

### Windows and Linux

1. **Install Python 3**: Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Install Git**: Follow the installation instructions for your operating system:
   - [Git for Windows](https://git-scm.com/download/win)
   - [Git for Linux](https://git-scm.com/download/linux)

3. **Clone the repository**:
   ```bash
   git clone https://github.com/Pro-Tik/sui-faucet-claimer.git
   cd sui-faucet-claimer
   ```

4. **Install required libraries**:
   ```bash
   pip install requests
   ```

5. **Create the required text files**:
   - **proxies.txt**: Add your proxy addresses (one per line).
   - **wallet.txt**: Add your wallet addresses (one per line).

### Termux (Android)

1. **Update Termux**:
   ```bash
   pkg update && pkg upgrade
   ```

2. **Install Python and Git**:
   ```bash
   pkg install python git
   ```

3. **Install required libraries**:
   ```bash
   pip install requests
   ```

4. **Clone the repository**:
   ```bash
   git clone https://github.com/Pro-Tik/sui-faucet-claimer.git
   cd sui-faucet-claimer
   ```

5. **Create the required text files**:
   ```bash
   nano proxies.txt  # Add your proxy addresses and save
   nano wallet.txt   # Add your wallet addresses and save
   ```

## Usage

Run the script using Python:
```bash
python faucet.py
```

### Important Notes
- The script will exit if it is not running from the specified GitHub repository.
- The script requests tokens every 10 minutes for each wallet address specified in `wallet.txt`.
- Ensure that your `proxies.txt` and `wallet.txt` files are correctly formatted with one address per line.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- SUI Faucet team for providing the API.
- OpenAI for assistance with the development.
