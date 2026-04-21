import java.nio.file.*;

class ImageResizing {
    public static void run(String size, String fixturesRoot) throws Exception {
        String[] tokens = Files.readString(Path.of(fixturesRoot, "generated", "image", size + ".ppm")).trim().split("\\s+");
        int width = Integer.parseInt(tokens[1]);
        int height = Integer.parseInt(tokens[2]);
        long checksum = 0;
        for (int y = 0; y < height / 2; y++) {
            for (int x = 0; x < width / 2; x++) {
                int idx = 4 + (((y * 2) * width + (x * 2)) * 3);
                checksum += Integer.parseInt(tokens[idx]) + Integer.parseInt(tokens[idx + 1]) + Integer.parseInt(tokens[idx + 2]);
            }
        }
        System.out.println(checksum);
    }
}
