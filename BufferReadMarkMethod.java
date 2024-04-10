/*

In this snippet:

The buffer size is set to 8KB, (it's modifiable based on requirements and memory constraints)
After reading each chunk of data, the mark() method is called to mark the current position in the stream.
The stream is reset every 1GB (1 << 30 bytes) to prevent memory overflow and ensure efficient memory usage when dealing with large files.

*/

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class BufferReadMarkMethod {
    public static void main(String[] args) {
        String filePath = "path/to/your/large/file"; // Replace with your file path
        
        try (InputStream inputStream = new BufferedInputStream(new FileInputStream(filePath))) {
            // Set buffer size based on the size of the file (adjust as needed)
            byte[] buffer = new byte[8192]; // 8KB buffer size
            
            long totalBytesRead = 0;
            int bytesRead;
            
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                // Process or write the data as needed
                totalBytesRead += bytesRead;
                
                // Mark the current position in the stream
                inputStream.mark(Integer.MAX_VALUE);
                
                // Reset the stream every 1GB to prevent memory overflow
                if (totalBytesRead % (1L << 30) == 0) {
                    inputStream.reset();
                }
            }
            
            System.out.println("Total bytes read: " + totalBytesRead);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

