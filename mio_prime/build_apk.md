# How to Build MIO PRIME APK

Since MIO PRIME is built with **Flet** (Python), you can easily package it into an Android APK.

## Prerequisites
- A GitHub account.
- No local Android Studio required (we will use GitHub Actions).

## Steps

1.  **Push Code to GitHub**
    - Create a new repository on GitHub.
    - Upload all files from the `mio_prime` folder to this repository.
    - Ensure `requirements.txt` exists and contains:
        ```
        flet
        ```

2.  **Setup GitHub Actions**
    - In your repository, go to **Actions**.
    - Search for a workflow or create a new one.
    - Use the standard **Flet Build** workflow. Create a file `.github/workflows/build.yml` with this content:

    ```yaml
    name: Build APK
    on: [push]
    jobs:
      android:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Setup Python
            uses: actions/setup-python@v2
            with:
              python-version: 3.11
          - name: Install Dependencies
            run: pip install flet
          - name: Build APK
            run: |
              flet build apk --project mio_prime
          - name: Upload APK
            uses: actions/upload-artifact@v2
            with:
              name: mio_prime_apk
              path: build/app/outputs/flutter-apk/app-release.apk
    ```
    *(Note: This is a simplified example. The official Flet documentation has the most up-to-date workflow template.)*

3.  **Download APK**
    - Once the Action finishes, go to the **Summary** page of the run.
    - Download the `mio_prime_apk` artifact.
    - Install it on your phone!

## Local Testing
- Run `python gui.py` on your computer to test the interface before building.
