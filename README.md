# LigaCryptoBouncer

<img src="icon.png" alt="LigaCryptoBouncer Logo" width="200"/>

## Overview

LigaCryptoBouncer is a project designed to interact with YouTube's API to manage and retrieve information about channel memberships.  
Leveraging such info, it manages access/removal of members according to membership tiers.

## Current Features

- ✅ Authenticate with YouTube API using OAuth 2.0
- ✅ List membership levels of a YouTube channel

## Future Features

- ⬜ Add support for retrieving channel member details
- ⬜ Distinguish members according to their member tier
- ⬜ Retrieving Telegram group members
- ⬜ Associating Telegram group members according to their Youtube IDs
- ⬜ For now, exporting a list of Telegram members that _should_ be purged in sheet format
- ⬜ In a near future, exporting membership list extraction onto a SQLite db so it can be compared in a sorta incremental routine

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/mai0li/LigaCryptoBouncer.git
   cd LigaCryptoBouncer
   ```

2. Create and activate a Python virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Place your client_secret.json file in the secrets directory.

5. Run the script to authenticate and list membership levels:

   ```sh
   python tests/membership_extract.py
   ```

## Usage

- Ensure you have the necessary credentials and permissions to access the YouTube API.
- Follow the setup instructions to configure your environment.
- Use the provided functions to interact with the YouTube API.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.