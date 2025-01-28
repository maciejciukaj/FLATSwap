from selenium import webdriver
import time

from Utils.recording_utils import initialize_parser, configure_browser, set_sdr_params


def start_recording(browser, options):
    """Start recording WebSDR audio."""
    browser.execute_script("record_click();")  # Start recording
    recbegin = time.time()

    if not (options.hf == "0" or options.lf == "0"):
        print(
            f"Recording started ... {options.f} kHz {options.m} mode {options.lf}-{options.hf} kHz passband by {options.uname} for {options.t}s.")
    else:
        print(
            f"Recording started ... {options.f} kHz {options.m} mode default passband by {options.uname} for {options.t}s.")

    while time.time() < recbegin + float(options.t):
        time.sleep(1)


def stop_recording_and_save(browser):
    """Stop the recording and save the file."""
    browser.execute_script("record_click();")  # End recording
    print("Recording stopped ...")
    svfield = browser.find_element(webdriver.common.by.By.LINK_TEXT, 'save')
    svfield.click()  # Click Save Button
    print("Saving recording ... ")
    time.sleep(5)  # Delay for save to complete


def close_browser(browser):
    """Close the browser and complete the task."""
    print("Closing down ...")
    browser.close()
    browser.quit()
    print("Job Done!")


def main():
    """Main function to execute the steps."""
    options, args = initialize_parser()
    print("Launching Browser ...")
    browser = configure_browser(options)

    set_sdr_params(browser, options)
    start_recording(browser, options)
    stop_recording_and_save(browser)
    close_browser(browser)


if __name__ == "__main__":
    main()
