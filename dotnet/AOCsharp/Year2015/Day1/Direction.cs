namespace AOCsharp.Year2015.Day1;

public static class Direction
{
    public static string ParseInput(TextReader input)
    {
        return input.ReadToEnd().Trim();
    }
    public static int GetFloorDelta(char direction)
    {
        return direction switch
        {
            '(' => 1,
            ')' => -1,
            _ => throw new Exception($"Invalid direction {direction}")
        };
    }
}
