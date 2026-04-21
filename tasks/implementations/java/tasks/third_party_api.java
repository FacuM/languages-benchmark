import java.nio.file.*;
import java.util.regex.*;

class ThirdPartyApi {
    public static void run(String size, String fixturesRoot) throws Exception {
        String text = Files.readString(Path.of(fixturesRoot, "mocks", "twitter_like_" + size + ".json"));
        Matcher matcher = Pattern.compile("\\\"id\\\":\\s*\\\"([^\\\"]+)\\\",\\s*\\\"text\\\":\\s*\\\"([^\\\"]+)\\\",\\s*\\\"likes\\\":\\s*(\\d+)").matcher(text);
        long total = 0;
        while (matcher.find()) total += matcher.group(1).length() + matcher.group(2).length() + Integer.parseInt(matcher.group(3));
        System.out.println(total);
    }
}
