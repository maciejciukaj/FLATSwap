import os
import string
from optparse import OptionParser
from random import random
import time

from selenium.webdriver.chrome import webdriver


def initialize_parser():
    """Initialize the command line parser and return options."""
    parser = OptionParser()

    if os.name == "nt":
        print("You are running a Windows-based platform ...")
        parser.add_option("-b", "--binary-location", dest="bloc",
                          default=r"C:\Program Files\Mozilla Firefox\firefox.exe", help="Firefox Binary Location")
        parser.add_option("-w", "--webdriver-location", dest="wloc", default=r"geckodriver.exe",
                          help="Geckodriver Binary Location")
    else:
        print("You are running a POSIX-based platform ...")
        parser.add_option("-b", "--binary-location", dest="bloc", default=r"firefox", help="Firefox Binary Location")
        parser.add_option("-w", "--webdriver-location", dest="wloc", default=r"geckodriver",
                          help="Geckodriver Binary Location")

    # Add other options as before
    parser.add_option("-n", "--username", dest="uname", default="websdrrec_" + "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(6)), help="Username")
    parser.add_option("-f", "--frequency", dest="f", default="4625", help="Tuning Frequency (kHz)")
    parser.add_option("-m", "--mode", dest="m", default="usb", help="Tuning Mode (default: usb)")
    parser.add_option("-t", "--recordtime", dest="t", default="10", help="Record Length (s) (default: 10s)")
    parser.add_option("-u", "--upper", dest="hf", default="0", help="High-Frequency Cut-Off (kHz) (optional)")
    parser.add_option("-l", "--lower", dest="lf", default="0", help="Low-Frequency Cut-Off (kHz) (optional)")
    parser.add_option("-o", "--output-directory", dest="dld", default=os.getcwd(),
                      help="File Download Directory (default: current working directory)")
    parser.add_option("-z", "--headless", dest="z", default=1, help="Headless Mode (default: 1)")

    return parser.parse_args()


def configure_browser(options):
    """Configure the Firefox WebDriver and return the browser instance."""
    opts = webdriver.firefox.options.Options()
    opts.binary_location = options.bloc
    if options.z == 1:
        opts.add_argument("--headless")
    opts.set_preference("browser.download.folderList", 2)
    opts.set_preference("browser.download.manager.showWhenStarting", False)
    opts.set_preference("browser.download.dir", options.dld)
    opts.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    return webdriver.Firefox(options=opts)


def set_sdr_params(browser, options):
    """Set the WebSDR parameters like username, frequency, and mode."""
    browser.get("http://websdr.ewi.utwente.nl:8901/")  # Hard coded URL
    time.sleep(5)  # Delay for page load
    browser.execute_script("soundapplet.audioresume();")  # Start Audio
    time.sleep(0.1)
    browser.execute_script("setview(3);")

    unfield = browser.find_element(webdriver.common.by.By.NAME, "username")
    unfield.send_keys(str(options.uname))  # Set username
    unfield.send_keys(webdriver.common.keys.Keys.RETURN)
    time.sleep(1)

    frfield = browser.find_element(webdriver.common.by.By.NAME, "frequency")
    frfield.send_keys(webdriver.common.keys.Keys.CONTROL + "a")
    frfield.send_keys(str(options.f))  # Set frequency
    frfield.send_keys(webdriver.common.keys.Keys.RETURN)
    time.sleep(1)

    browser.execute_script("set_mode('" + str(options.m) + "');")  # Set mode
    time.sleep(1)

    if not (options.hf == "0" or options.lf == "0"):
        browser.execute_script(f"window.lo={options.lf};")
        browser.execute_script(f"window.hi={options.hf};")
        browser.execute_script("updbw();")  # Set filter parameters
        time.sleep(1)