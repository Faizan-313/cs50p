Facebook Scraping

Description:
This Python program is a data scraper for Facebook, making use of Selenium WebDriver and BeautifulSoup. Its basic function is the collection of data from the Facebook profile of a given user, which contains information of his posts, friends, and store this information into CSV files.

The functioning of the program is segmented into several phases:

    1. Set WebDriver and Login: The program starts with setting up the Chrome WebDriver via Selenium. It also customizes the options so that alerts would not appear. After that it prompts the user with their Facebook credentials (email and password) for login to their Facebook accounts.

    2. Get the Profile Page: After successfully login into the account, the user's Facebook profile page is obtained by the WebDriver. After waiting for the page to load, the HTML content is extracted from this page. It is at  that time BeautifulSoup  ensures the HTML data is parsed.

    3. Scrape Data of the Posts: The program starts extracting data related to the posts of the user. A defined algorithm has been applied to identify and retrieve data for all posts, including texts, likes, and comments from the HTML structure. The accumulated data is systematically organized and saved in a CSV file named "facebook_post_data.csv".

    4. Scrape the Friend List: After the program scrapes the post related data form the profile page, the program navigates to the friend list page of Facebook. The web page will be effectively pulled through a scrolling effect enabled by JavaScript, whose execution is managed by the WebDriver. The user then performs thorough data extraction from HTML content to get the names and profile links of his friends. This data is then  saved in another CSV file called "facebook_friend_list.csv".

    5. Clean Up: After completing scraping tasks, the program provides a response to the user by printing "Done!" to show successful completion. It then shuts down the WebDriver , ensuring its respective cleanup and resource management.

This project, other than the main project file contains two other files:

    1. test_project.py.
    Description:
        This is a Python script for running tests on a Facebook web scraper program designed to retrieve personal user information from Facebook. The script imports necessary libraries and modules, such as unittest for testing, selenium for browser automation, and BeautifulSoup for HTML parsing, which offers utilities for file operations and browser configuration.

        TestFacebookScraper Class:This class has some test cases that are testing functionalities of the web scraping program.

        setUpClass: This class method sets up the testing environment, such as setting preferences and navigating to the login page for Facebook. This script will run once before every test.

        tearDownClass: This method cleans up the testing environment, which quits the WebDriver. It runs once after all the tests are performed.

        setUp: This method is called before each test case and logs in to Facebook with the provided credentials.

        Test Methods: The test methods validate various aspects of the web scraping program:

        test_profile: Tests the function that is responsible for the extraction of profile information from Facebook.

        test_No_of_likes_and_comments: Tests the function that extracts the likes and comments of a Facebook post.

        test_post_text: Tests the function that extracts the text of Facebook posts.

        test_friend_list: Tests the function which extracts a list of friends from Facebook.

        Main Block:
        The unittest.main() function runs the test cases in the TestFacebookScraper class.


    2. requirements.txt
    Description:
        It has the information about the requirements needed for this project
