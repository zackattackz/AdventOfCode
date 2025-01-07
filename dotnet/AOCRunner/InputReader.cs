namespace AOCRunner;

public static class InputReader
{
    public static StreamReader Get(int year, int day)
    {
        return new StreamReader($"../inputs/{year}/{day}.txt");
    }
}
