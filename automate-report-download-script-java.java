/*
Challenge: Write an automation script in java with following steps
            1. Navigate to a webpage
            2. Select latest date from the HTML drop down element
            3. Click on the Download button
            4. Save to target location
            5. Open the downloaded report file
/*

/*
We leverage Selenium WebDrive for webpage interactions
Java file operations, standard functions
*/

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class ReportDownloadAutomationScript {

    public static void main(String[] args) {
        // Set the path to your ChromeDriver executable.
        System.setProperty("webdriver.chrome.driver", "<path/to/chromedriver.exe>");
        
        // Initialize the WebDriver
        WebDriver driver = new ChromeDriver();

        try {
            // Step 1: Go to the webpage, give the url here
            driver.get("https://example.com");

            // Step 2: Select the latest date from the HTML drop down element
            WebElement dateDropdown = driver.findElement(By.id("ContentPlaceHolder1_ddlReportList"));
            Select dateSelect = new Select(dateDropdown);
            dateSelect.selectByIndex(0);  // Index 0 represents the latest date

            // Step 3: Click on the Download button
            WebElement downloadButton = driver.findElement(By.id("ContentPlaceHolder1_btnDownload"));
            downloadButton.click();

            // Step 4: Wait for the file to download (use a library like WebDriverWait)

            // Step 5: Assuming you want to open the file using the default system application
            // You can implement this based on your operating system (e.g., using Java's ProcessBuilder)
            String filePath = "<path/to/downloaded/file.ext>";
            openFile(filePath);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Close the WebDriver when you're done
            driver.quit();
        }
    }

    // Open the downloaded file using the system default application
    private static void openFile(String filePath) {
        try {
            // Replace this logic with platform-specific code as needed
            // For windows
            if (System.getProperty("os.name").toLowerCase().contains("win")) {
                Runtime.getRuntime().exec("cmd /c start " + filePath);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
