import java.nio.file.*;
import java.util.regex.*;

class WebScraper {
    public static void run(String size, String fixturesRoot) throws Exception {
        Path base = Path.of(fixturesRoot, "mock_site", size);
        String index = Files.readString(base.resolve("index.html"));
        Pattern linkPattern = Pattern.compile("href=\"([^\"]+)\"");
        Pattern titlePattern = Pattern.compile("<h2>(.*?)</h2>");
        Pattern bodyPattern = Pattern.compile("<p>(.*?)</p>");
        Matcher linkMatcher = linkPattern.matcher(index);
        long total = 0;
        int idx = 0;
        while (linkMatcher.find()) {
            String page = Files.readString(base.resolve(linkMatcher.group(1)));
            String title = titlePattern.matcher(page).results().findFirst().get().group(1);
            String body = bodyPattern.matcher(page).results().findFirst().get().group(1);
            total += (long) (idx + 1) * (title.length() + body.length());
            idx++;
        }
        System.out.println(total);
    }
}
