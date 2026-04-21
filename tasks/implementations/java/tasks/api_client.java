import java.nio.file.*;
import java.util.regex.*;

class ApiClient {
    public static void run(String size, String fixturesRoot) throws Exception {
        String text = Files.readString(Path.of(fixturesRoot, "mocks", "public_api_" + size + ".json"));
        Matcher matcher = Pattern.compile("\\\"id\\\":\\s*(\\d+),\\s*\\\"name\\\":\\s*\\\"([^\\\"]+)\\\",\\s*\\\"value\\\":\\s*(\\d+)").matcher(text);
        long total = 0;
        while (matcher.find()) total += Integer.parseInt(matcher.group(1)) + Integer.parseInt(matcher.group(3)) + matcher.group(2).length();
        System.out.println(total);
    }
}
