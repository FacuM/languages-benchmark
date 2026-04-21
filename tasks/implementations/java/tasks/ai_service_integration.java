import java.nio.file.*;
import java.util.regex.*;

class AiServiceIntegration {
    public static void run(String size, String fixturesRoot) throws Exception {
        String text = Files.readString(Path.of(fixturesRoot, "mocks", "ai_service_" + size + ".json"));
        Matcher modelMatcher = Pattern.compile("\\\"model\\\":\\s*\\\"([^\\\"]+)\\\"").matcher(text);
        modelMatcher.find();
        long total = modelMatcher.group(1).length();
        Matcher matcher = Pattern.compile("\\\"prompt\\\":\\s*\\\"([^\\\"]+)\\\",\\s*\\\"output\\\":\\s*\\\"([^\\\"]+)\\\",\\s*\\\"tokens\\\":\\s*(\\d+)").matcher(text);
        while (matcher.find()) total += matcher.group(1).length() + matcher.group(2).length() + Integer.parseInt(matcher.group(3));
        System.out.println(total);
    }
}
